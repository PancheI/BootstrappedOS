#!/usr/bin/env python3
"""pacing.py — cut rhythm of a video: hard cuts (frame-diff spikes vs local median), shot lengths, cuts/min,
and the shortest shots. Usage: pacing.py <video> [--fps 30] [--list]"""
import subprocess, sys, numpy as np
p = sys.argv[1]; fps = 30
raw = subprocess.run(["ffmpeg","-v","error","-i",p,"-vf",f"fps={fps},scale=192:108","-pix_fmt","gray","-f","rawvideo","-"],capture_output=True).stdout
F = np.frombuffer(raw,np.uint8).reshape(-1,108,192).astype(np.float32)
d = np.r_[0,np.abs(np.diff(F,axis=0)).mean((1,2))]
med = np.array([np.median(d[max(0,i-15):i+16]) for i in range(len(d))])
cuts = [i for i in range(1,len(d)) if d[i]>12 and d[i]>4*med[i]+4]
# merge cuts closer than 2 frames
m=[]; [m.append(c) for c in cuts if not m or c-m[-1]>2]; cuts=m
b=[0]+cuts+[len(d)]; L=np.diff(b)/fps
dur=len(d)/fps
print(f"{p.split('/')[-1]}: {dur:.1f}s, {len(cuts)} cuts, {60*len(cuts)/dur:.0f} cuts/min, median shot {np.median(L):.2f}s, p10 {np.percentile(L,10):.2f}s, shots<0.5s: {(L<0.5).sum()}")
if "--list" in sys.argv:
	for i,(a,l) in enumerate(zip(b[:-1],L)):
		if l<0.6: print(f"  short shot {a/fps:6.2f}s–{(a/fps+l):6.2f}s  {l:.2f}s")
