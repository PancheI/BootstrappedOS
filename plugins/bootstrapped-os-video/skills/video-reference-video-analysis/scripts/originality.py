#!/usr/bin/env python3
"""
originality.py — how much does OUR film look/move like a reference? Per-beat "copy score".

  python3 originality.py <ours.mp4> <ref.mp4> --map <timeline.py dir> [--beats beats.json] [--fps 60]

For each output frame we look up the REF frame it came from (timeline.film_f inverse; frames added by holds or
absent from REF are skipped) and compare, on 192x108 gray:
  layout  = correlation of Sobel edge maps (where things are: cards, text blocks, composition)
  motion  = correlation of per-frame change curves over 1-s windows (does it move on the same beats/shape)
copy score = 100 · (0.6·layout + 0.4·motion), clipped to 0..100.  Rough guide:
  > 60 traced (same composition + same motion)   35–60 clearly derived   < 35 own work
Colour/palette is ignored on purpose (a recolour is still a copy).
Prints per-second scores, per-beat averages (beats.json: [[name, t0, t1], ...] in OUR seconds) and the share of
runtime above 60 / 35.
"""
import argparse, importlib.util, json, os, subprocess, sys
import numpy as np


def frames(p, fps):
	raw = subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-vf", f"fps={fps},scale=192:108", "-pix_fmt", "gray", "-f", "rawvideo", "-"], capture_output=True).stdout
	return np.frombuffer(raw, np.uint8).reshape(-1, 108, 192).astype(np.float32)


def edges(a):
	gx = np.abs(np.diff(a, axis=1, prepend=a[:, :1])); gy = np.abs(np.diff(a, axis=0, prepend=a[:1]))
	return gx + gy


def corr(a, b):
	a = a.ravel() - a.mean(); b = b.ravel() - b.mean()
	d = np.sqrt((a * a).sum() * (b * b).sum())
	return float((a * b).sum() / d) if d > 1e-6 else 0.0


def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("ours"); ap.add_argument("ref")
	ap.add_argument("--map", required=True, help="dir containing timeline.py with film_f(ref_frame)")
	ap.add_argument("--beats"); ap.add_argument("--fps", type=int, default=60)
	a = ap.parse_args()
	spec = importlib.util.spec_from_file_location("timeline", os.path.join(a.map, "timeline.py"))
	tl = importlib.util.module_from_spec(spec); spec.loader.exec_module(tl)
	O = frames(a.ours, a.fps); R = frames(a.ref, a.fps)
	inv = {}
	for rf in range(len(R)):
		try:
			of = tl.film_f(rf)
		except Exception:
			continue
		if of is not None and 0 <= round(of) < len(O):
			inv.setdefault(int(round(of)), rf)
	lay = np.full(len(O), np.nan)
	for of, rf in inv.items():
		lay[of] = max(0.0, corr(edges(O[of]), edges(R[rf])))
	dO = np.r_[0, np.abs(np.diff(O, axis=0)).mean((1, 2))]
	dR = np.r_[0, np.abs(np.diff(R, axis=0)).mean((1, 2))]
	mot = np.full(len(O), np.nan)
	W = a.fps
	for s in range(0, len(O) - W, W // 2):
		idx = [of for of in range(s, s + W) if of in inv]
		if len(idx) > W // 2:
			c = max(0.0, corr(dO[idx], dR[[inv[i] for i in idx]]))
			for i in range(s, s + W):
				mot[i] = c if np.isnan(mot[i]) else max(mot[i], c)
	score = 100 * (0.6 * np.nan_to_num(lay) + 0.4 * np.nan_to_num(mot))
	score[np.isnan(lay)] = np.nan
	sec = [np.nanmean(score[i:i + a.fps]) if np.any(~np.isnan(score[i:i + a.fps])) else float("nan") for i in range(0, len(O), a.fps)]
	print("per-second copy score:", " ".join("--" if np.isnan(x) else f"{x:.0f}" for x in sec))
	valid = score[~np.isnan(score)]
	print(f"runtime traced (>60): {100 * (valid > 60).mean():.0f}%   derived (35–60): {100 * ((valid > 35) & (valid <= 60)).mean():.0f}%   own (<35 or not from REF): {100 * (1 - (valid > 35).sum() / len(O)):.0f}%")
	if a.beats:
		for name, t0, t1 in json.load(open(a.beats)):
			seg = score[int(t0 * a.fps):int(t1 * a.fps)]
			v = seg[~np.isnan(seg)]
			print(f"  {name:28s} {t0:5.1f}–{t1:5.1f}s  copy {np.mean(v) if len(v) else 0:5.1f}  ({len(v)}/{len(seg)} frames map to REF)")


if __name__ == "__main__":
	main()
