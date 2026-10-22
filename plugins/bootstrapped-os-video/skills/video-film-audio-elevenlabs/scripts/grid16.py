#!/usr/bin/env python3
"""grid16.py file bpm phase [all|low|hi]: loudness of each beat, 16 beats per row, on a fixed tempo grid.
Use it to check which band (low = kick, hi = hats) carries the tempo you measured with bpm.py."""
import numpy as np, subprocess, sys
from scipy.signal import stft
if len(sys.argv) < 4:
    sys.exit(__doc__)
p=sys.argv[1]; bpm=float(sys.argv[2]); ph=float(sys.argv[3]); band=sys.argv[4] if len(sys.argv)>4 else 'all'
sr=22050; m=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',p,'-ac','1','-ar',str(sr),'-f','f32le','-'],capture_output=True).stdout,np.float32)
f,t,Z=stft(m,sr,nperseg=1024,noverlap=1024-256); S=np.abs(Z)**2
rng={'all':(0,11025),'low':(0,150),'hi':(5000,11025)}[band]
beat=60/bpm; k=0; row=[]
while ph+(k+1)*beat<len(m)/sr:
    s=ph+k*beat; sel=(t>=s)&(t<s+beat)
    row.append(10*np.log10(S[(f>=rng[0])&(f<rng[1])][:,sel].sum(0).mean()+1e-12)); k+=1
row=np.array(row); row-=row.max()
for i in range(0,len(row),16):
    print(f"b{i:4d} {ph+i*beat:6.2f}s", ' '.join(f"{v:3.0f}" for v in row[i:i+16]))
