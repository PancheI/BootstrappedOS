import numpy as np, subprocess, json, sys, os
from scipy.signal import stft
def br(p, a=0, b=40):
    sr=44100
    m=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-ss',str(a),'-t',str(b-a),'-i',p,'-ac','1','-ar',str(sr),'-f','f32le','-'],capture_output=True).stdout,np.float32)
    f,t,Z=stft(m,sr,nperseg=4096); A=np.abs(Z); P=A**2
    return P[f>4000].sum()/P.sum(), P[f<100].sum()/P.sum(), A[f>4000].sum()/A.sum(), A[f<100].sum()/A.sum()
if __name__=='__main__':
    for p in sys.argv[1:]:
        r=br(p); print(os.path.basename(p), 'pow>4k %.3f pow<100 %.3f | mag>4k %.3f mag<100 %.3f'%r)
