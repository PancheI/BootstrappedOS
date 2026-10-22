#!/usr/bin/env python3
"""bpm.py file1 [file2 ...]: best tempo (BPM), score, beat phase, duration and loudness per 5 s, for each file.
Needs ffmpeg, numpy and scipy."""
import numpy as np, subprocess, sys, glob
from scipy.signal import stft
def load(p,sr=22050):
    raw=subprocess.run(['ffmpeg','-v','error','-i',p,'-ac','1','-ar',str(sr),'-f','f32le','-'],capture_output=True).stdout
    return np.frombuffer(raw,np.float32),sr
def comb(m,sr):
    HOP=110; f,t,Z=stft(m,sr,nperseg=1024,noverlap=1024-HOP); L=np.log1p(100*np.abs(Z)); fps=sr/HOP
    e=np.concatenate([[0],np.maximum(np.diff(L,axis=1),0).sum(0)]); e=e-np.convolve(e,np.ones(int(fps))/fps,'same'); e=np.maximum(e,0)
    best=[]
    for bpm in np.arange(70,180,0.05):
        per=60/bpm*fps; n=int(len(e)/per)-1
        idx=(np.arange(n)[:,None]*per+np.arange(int(per))[None,:]).astype(int)
        prof=e[idx].mean(0); best.append((prof.max()/(prof.mean()+1e-9),bpm,prof.argmax()/fps))
    best.sort(reverse=True); return best[0]
if len(sys.argv) < 2:
    sys.exit(__doc__)
for p in sys.argv[1:]:
    m,sr=load(p); s,b,ph=comb(m,sr)
    rms=[20*np.log10(np.sqrt((m[i*sr*5:(i+1)*sr*5]**2).mean())+1e-9) for i in range(int(len(m)/sr/5))]
    print(p.split('/')[-1], f"{b:.2f}bpm s{s:.2f} ph{ph:.3f} dur{len(m)/sr:.1f}", ' '.join(f"{v:.0f}" for v in rms))
