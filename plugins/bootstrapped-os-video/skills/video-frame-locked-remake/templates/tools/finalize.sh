#!/usr/bin/env bash
# One-command finalize: stat mix → bundle → render → stat mix again (remux if it changed) → jump scan →
# master / web / X exports → open our video.
#   bash remake/tools/finalize.sh [name=film]
# Run from the project root (macOS: uses BSD stat and `open`; on Linux swap stat -f %m for stat -c %Y and skip the open).
# The jump scan reads remake/tools/stretches.json if present: [[S0,S1,EXT],...] or
# {"stretches": [[S0,S1,EXT],...], "cuts": [[C0,C1],...]}, equal to STRETCHES and CUTS in src/Remake/Remake.tsx.
set -euo pipefail
NAME="${1:-film}"; MIX=public/remake/mix.wav; B=remake/work/lead/fullbundle; OUT=out/remake; mkdir -p "$OUT" remake/out
m0=$(stat -f %m "$MIX"); echo "mix: $(stat -f %Sm "$MIX")"
npx tsc --noEmit -p . 2>&1 | grep -E "src/Remake|Root" && { echo "tsc errors — fix first"; exit 1; } || true
rm -rf "$B"; npx remotion bundle src/index.ts --out-dir "$B" >remake/out/bundle.log 2>&1 || { echo "bundle failed, see remake/out/bundle.log"; exit 1; }
npx remotion render "$B" Remake remake/out/remake.mp4 --codec=h264 --crf=16 --concurrency=4 --log=error >remake/out/render.log 2>&1 || { echo "render failed, see remake/out/render.log"; exit 1; }
m1=$(stat -f %m "$MIX")
newer=$(find src -newer "$B/index.html" -name "*.tsx" | head -5); [ -n "$newer" ] && echo "WARNING: source changed after bundling → re-run finalize: $newer"
if [ "$m1" != "$m0" ]; then echo "mix changed during render → remuxing"; ffmpeg -v error -y -i remake/out/remake.mp4 -i "$MIX" -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k -ar 48000 -shortest remake/out/_r.mp4 && mv remake/out/_r.mp4 remake/out/remake.mp4; fi
ffprobe -v error -show_entries stream=codec_type,nb_frames:format=duration -of compact remake/out/remake.mp4
python3 - <<'EOF'
import numpy as np, subprocess, json, os
raw=subprocess.run(['ffmpeg','-v','error','-i','remake/out/remake.mp4','-vf','scale=192:108','-pix_fmt','rgb24','-f','rawvideo','-'],capture_output=True).stdout
v=np.frombuffer(raw,np.uint8).reshape(-1,108,192,3).astype(np.float32)
d=np.abs(np.diff(v.mean(3),axis=0)).mean((1,2))
ref='remake/ref/diff.npy'; dr=np.load(ref) if os.path.exists(ref) else np.zeros(len(d))
cfg=json.load(open('remake/tools/stretches.json')) if os.path.exists('remake/tools/stretches.json') else []
if isinstance(cfg,list): cfg={'stretches':cfg,'cuts':[]}
ev=sorted([('s',a,b,e) for a,b,e in cfg.get('stretches',[])]+[('c',a,b,0) for a,b in cfg.get('cuts',[])],key=lambda x:x[1])
def refd(o):
  sh=0
  for k,a,b,e in ev:
    if k=='s':
      if o<a+sh: return dr[min(len(dr)-1,max(0,o-sh))]
      if o<=b+sh+e: return 2.0
      sh+=e
    else:
      if o<a+sh: return dr[min(len(dr)-1,max(0,o-sh))]
      if o==a+sh: return 99.0  # the cut itself is a jump by design
      sh-=b-a+1
  return dr[min(len(dr)-1,max(0,o-sh))]
bad=[(i+1,round(float(d[i]),1),round(float(refd(i)),1)) for i in range(len(d)) if d[i]>6 and d[i]>2.5*refd(i)+3]
print('JUMP SCAN:', 'clean' if not bad else bad)
EOF
cp remake/out/remake.mp4 "$OUT/$NAME-remake-1080p60.mp4"
ffmpeg -v error -y -i remake/out/remake.mp4 -vf fps=30 -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p -movflags +faststart -c:a aac -b:a 160k "$OUT/$NAME-remake-1080p30-web.mp4"
ffmpeg -v error -y -i remake/out/remake.mp4 -vf "fps=30,scale=1920:1080:flags=lanczos" -c:v libx264 -profile:v high -level 4.1 -preset slow -crf 20 -maxrate 8M -bufsize 16M -pix_fmt yuv420p -g 60 -movflags +faststart -c:a aac -b:a 128k -ar 48000 -ac 2 "$OUT/$NAME-x.mp4"
ls -la "$OUT"/*.mp4
open "$OUT/$NAME-remake-1080p60.mp4" 2>/dev/null || echo "open $OUT/$NAME-remake-1080p60.mp4 to watch it"
