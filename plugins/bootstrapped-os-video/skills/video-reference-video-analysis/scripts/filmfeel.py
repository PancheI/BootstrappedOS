#!/usr/bin/env python3
"""filmfeel.py — film-level craft stats (not layout): cuts/min, still fraction, motion energy, how smooth the motion is.
Compare ours vs a quality reference: python3 filmfeel.py a.mp4 b.mp4 ..."""
import subprocess, sys, numpy as np
def stats(p, fps=30):
	raw = subprocess.run(["ffmpeg","-v","error","-i",p,"-vf",f"fps={fps},scale=192:108","-pix_fmt","gray","-f","rawvideo","-"],capture_output=True).stdout
	F = np.frombuffer(raw,np.uint8).reshape(-1,108,192).astype(np.float32)
	d = np.r_[0,np.abs(np.diff(F,axis=0)).mean((1,2))]
	med = np.array([np.median(d[max(0,i-15):i+16]) for i in range(len(d))])
	cut = (d>12)&(d>4*med+4)
	mv = d[~cut]
	still = (mv<0.35).mean()                     # frames where nothing moves
	longest_still = max((len(s) for s in "".join('1' if x<0.35 else '0' for x in mv).split('0')), default=0)/fps
	smooth = np.median(np.abs(np.diff(mv)))/ (np.median(mv)+1e-6)   # jerkiness: frame-to-frame change of motion
	dur = len(d)/fps
	return dict(dur=dur, cuts_min=60*cut.sum()/dur, still=still, longest_still=longest_still, energy=np.median(mv), jerk=smooth)
print(f"{'video':42s} cuts/min  still%  longest-still  motion-energy  jerk")
for p in sys.argv[1:]:
	s = stats(p); print(f"{p.split('/')[-1][:42]:42s} {s['cuts_min']:7.1f}  {100*s['still']:5.0f}%  {s['longest_still']:9.2f}s  {s['energy']:11.2f}  {s['jerk']:5.2f}")
