"""sync.py OURS.mp4 OUT.mp4 — REF over remake, stacked, frame-locked (both 60fps, frame index burnt in), REF audio muted, ours kept."""
import sys, subprocess, os
# project root = PROJECT_ROOT or the current directory (run from your Remotion project root)
root = os.environ.get("PROJECT_ROOT", os.getcwd())
# multi-reference: REF=A → remake/ref/A/ (default remake/ref/); REF_DIR overrides the whole path
REFDIR = os.environ.get("REF_DIR") or (os.path.join(root, "remake", "ref", os.environ["REF"]) if os.environ.get("REF") else os.path.join(root, "remake", "ref"))
ours, out = sys.argv[1], sys.argv[2]
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{REFDIR}/reference.mp4", "-i", ours, "-filter_complex",
  "[0:v]fps=60,scale=960:540,setpts=N/60/TB[a];[1:v]fps=60,scale=960:540,setpts=N/60/TB[b];[a][b]vstack=inputs=2[v]",
  "-map", "[v]", "-map", "1:a?", "-c:v", "libx264", "-crf", "20", "-pix_fmt", "yuv420p", "-shortest", out], check=True)
print("→", out)
