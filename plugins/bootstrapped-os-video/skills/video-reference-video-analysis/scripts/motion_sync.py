#!/usr/bin/env python3
"""
motion_sync.py — does OUR motion feel like the reference? Per-window camera velocity + motion energy.

  python3 motion_sync.py <ref_frames_dir_or_glob> <our_frames_dir_or_glob> [--f0 0] [--win 20] [--npz out.npz]

Frames: any sorted jpg/jpeg/png sequences of the SAME timeline (render ours with the REF-locked
composition, e.g. `render.mjs <OUT> full f0 f1` on RemakeLocked). Index i in both = same frame.

Per frame pair it measures, on 320x180 gray:
  energy  = mean |frame[i+1]-frame[i]|            (how much changes: drift, reveals, blur)
  vel     = global translation by phase correlation, x6 → px/frame in 1920x1080
Per window it prints REF vs OURS energy, |vel| and vector error, flagging '<<' when
  vector error > 15 px/frame  or  energy differs by > 3.

What the flags usually mean:
  - ours energy ≈ 0 while REF 1–3  → a FROZEN stretch: REF never stops (card drift, camera float) → add measured drift
  - REF |vel| high, ours ~0       → a MISSING whip → add translate + directional blur on REF's frames
  - ours |vel| 2–3× REF           → a whip that is too violent → tame to REF's speed
  - a big error one window apart  → a whip on the WRONG frames → retime
Phase correlation is unreliable on flat/blank frames; judge those windows by eye (REF|OURS strips at 6 fps).
Targets: vector error < 5 px/frame, energy within ±30 %. Always confirm by watching strips — feel over numbers.
"""
import argparse, glob, os
import numpy as np
from PIL import Image


def seq(p):
	fs = sorted(glob.glob(os.path.join(p, "*"))) if os.path.isdir(p) else sorted(glob.glob(p))
	return [f for f in fs if f.lower().endswith((".jpg", ".jpeg", ".png"))]


def load(p):
	return np.asarray(Image.open(p).convert("L").resize((320, 180)), np.float32)


def shift(a, b):
	A = np.fft.fft2(a - a.mean()); B = np.fft.fft2(b - b.mean())
	R = A * np.conj(B); R /= np.abs(R) + 1e-6
	r = np.abs(np.fft.ifft2(R)); y, x = np.unravel_index(np.argmax(r), r.shape)
	if y > 90: y -= 180
	if x > 160: x -= 320
	return x * 6, y * 6


def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("ref"); ap.add_argument("ours")
	ap.add_argument("--f0", type=int, default=0); ap.add_argument("--win", type=int, default=20)
	ap.add_argument("--npz")
	a = ap.parse_args()
	R, O = seq(a.ref), seq(a.ours)
	n = min(len(R), len(O))
	r = [load(p) for p in R[:n]]; o = [load(p) for p in O[:n]]
	dR = np.array([np.abs(r[i + 1] - r[i]).mean() for i in range(n - 1)])
	dO = np.array([np.abs(o[i + 1] - o[i]).mean() for i in range(n - 1)])
	vR = np.array([shift(r[i + 1], r[i]) for i in range(n - 1)], float)
	vO = np.array([shift(o[i + 1], o[i]) for i in range(n - 1)], float)
	if a.npz:
		np.savez(a.npz, dR=dR, dO=dO, vR=vR, vO=vO)
	print(" frame  eREF eOURS  |vREF| |vOURS|  vErr")
	for w in range(0, n - 1, a.win):
		s = slice(w, min(w + a.win, n - 1))
		e = np.linalg.norm(vR[s] - vO[s], axis=1).mean()
		flag = "  <<" if e > 15 or abs(dR[s].mean() - dO[s].mean()) > 3 else ""
		print(f"{a.f0 + w:6d} {dR[s].mean():5.1f} {dO[s].mean():5.1f} {np.linalg.norm(vR[s], axis=1).mean():7.1f} {np.linalg.norm(vO[s], axis=1).mean():7.1f} {e:6.1f}{flag}")


if __name__ == "__main__":
	main()
