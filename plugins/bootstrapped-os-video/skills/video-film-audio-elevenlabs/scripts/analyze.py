#!/usr/bin/env python3
"""Analyse the REF soundtrack (remake/ref/audio.wav): tempo + beat phase, loudness arc,
hard stop, and SFX-like onsets. Prints a report (copied into ANALYSIS.md) and saves
work/analysis.json for the other scripts.  Run from the project root (or set PROJECT_ROOT / REF_DIR / AUDIO_DIR).

Needs REF_DIR/words.json: either Whisper's JSON output (whisper ... --word_timestamps True --output_format json,
renamed to words.json) or a plain list [{"s": start, "e": end}, ...].

Usage: python3 analyze.py [--voice-extra 6.8-7.5 ...] [--end-window 2.5]
  --voice-extra  extra voiced spans in seconds that Whisper missed (short sounds like "Oh" or a sigh)
  --end-window   seconds before the end to print at 50 ms resolution (default 2.5)"""
import argparse, json, os
import numpy as np, soundfile as sf
from scipy.signal import stft

# Paths: run from your project root, or set PROJECT_ROOT / AUDIO_DIR.
ROOT = os.environ.get("PROJECT_ROOT", os.getcwd())
AUDIO = os.environ.get("AUDIO_DIR", os.path.join(ROOT, "remake", "audio"))
WORK = os.path.join(AUDIO, "work")
REF_DIR = os.environ.get("REF_DIR", os.path.join(ROOT, "remake", "ref"))
ap = argparse.ArgumentParser()
ap.add_argument("--voice-extra", action="append", default=[], help="a voiced span Whisper missed, e.g. 6.8-7.5")
ap.add_argument("--end-window", type=float, default=2.5)
args = ap.parse_args()
x, sr = sf.read(os.path.join(REF_DIR, "audio.wav"))
if x.ndim == 1:
	x = x[:, None]
m = x.mean(1)
HOP = 240  # 5 ms
f, t, Z = stft(m, sr, nperseg=2048, noverlap=2048 - HOP)
S = np.abs(Z)
fps = sr / HOP
L = np.log1p(100 * S)


def flux(lo, hi):
	b = (f >= lo) & (f < hi)
	d = np.diff(L[b], axis=1)
	return np.concatenate([[0], np.maximum(d, 0).sum(0)])


def band_db(lo, hi):
	b = (f >= lo) & (f < hi)
	return 10 * np.log10((S[b] ** 2).sum(0) + 1e-12)


def load_words(path):
	"""Word spans (start, end) from Whisper JSON or a plain [{"s", "e"}] list."""
	d = json.load(open(path))
	if isinstance(d, dict):
		return [(w["start"], w["end"]) for seg in d.get("segments", []) for w in seg.get("words", [])]
	return [(w["s"], w["e"]) for w in d]


voiced = np.zeros(len(t), bool)
for s0, e0 in load_words(os.path.join(REF_DIR, "words.json")):
	voiced[(t >= s0 - 0.05) & (t <= e0 + 0.05)] = True
# Whisper misses short sounds ("Oh", a sigh): mark them from --voice-extra
for span in args.voice_extra:
	a, b = (float(v) for v in span.split("-"))
	voiced[(t >= a) & (t <= b)] = True


def tempo(env, mask=None):
	e = env - np.convolve(env, np.ones(int(fps)) / fps, "same")
	e = np.maximum(e, 0)
	if mask is not None:
		e = e * mask
	best = []
	for bpm in np.arange(80, 160, 0.05):
		per = 60 / bpm * fps
		# comb: sum envelope at beat positions over all phases
		n = int(len(e) / per)
		idx = (np.arange(n)[:, None] * per + np.arange(int(per))[None, :]).astype(int)
		idx = idx[idx[:, -1] < len(e)]
		prof = e[idx].mean(0)
		best.append((prof.max() / (prof.mean() + 1e-9), bpm, prof.argmax() / fps))
	best.sort(reverse=True)
	return best[:5]


kick = flux(30, 150)
full = flux(30, 16000)
hat = flux(6000, 16000)
out = {}
print("## Tempo (comb over onset envelope)")
for name, env, mask in [("kick band, voice-free frames", kick, ~voiced), ("kick band, all", kick, None), ("hat band, voice-free", hat, ~voiced), ("full, voice-free", full, ~voiced)]:
	r = tempo(env, mask)
	print(f"- {name}: " + ", ".join(f"{b:.2f} BPM (score {s:.2f}, phase {p:.3f}s)" for s, b, p in r[:3]))
	out.setdefault("tempo", {})[name] = r[:3]

# loudness per second (RMS dB) + low band
print("\n## Loudness arc (per 1 s, RMS dBFS full / <150 Hz / voice-free?)")
rms = []
for s in range(int(len(m) / sr) + 1):
	seg = m[s * sr:(s + 1) * sr]
	if len(seg) == 0:
		break
	rms.append(20 * np.log10(np.sqrt((seg ** 2).mean()) + 1e-9))
lowdb = band_db(30, 150)
print(" ".join(f"{i}:{v:.0f}" for i, v in enumerate(rms)))
# fine loudness around the dips (50 ms)
print("\n## Low-band (<150 Hz, music body) per 0.25 s")
q = []
for k in range(int(t[-1] / 0.25)):
	sel = (t >= k * 0.25) & (t < (k + 1) * 0.25)
	q.append(float(np.mean(lowdb[sel])))
print(" ".join(f"{k*0.25:.2f}:{v:.0f}" for k, v in enumerate(q)))
out["low_q"] = q
out["rms_s"] = rms

# hard stop: last sample above -60 dBFS
a = np.abs(m)
last = np.where(a > 10 ** (-60 / 20))[0][-1] / sr
env50 = [20 * np.log10(np.sqrt((m[int(i * sr / 20):int((i + 1) * sr / 20)] ** 2).mean()) + 1e-9) for i in range(int(len(m) / sr * 20))]
w0 = max(0.0, len(m) / sr - args.end_window)
print(f"\n## End: last sample > -60 dBFS at {last:.3f} s; 50 ms RMS from {w0:.2f} s:")
print(" ".join(f"{i/20:.2f}:{v:.0f}" for i, v in enumerate(env50) if i / 20 >= w0))
out["last"] = last

# onsets: peaks of full flux, with spectral character
print("\n## Onsets (flux peaks, top by strength) — time, strength, centroid Hz, hi/low ratio dB, in-voice")
from scipy.signal import find_peaks
fl = full / full.max()
pk, pr = find_peaks(fl, height=0.18, distance=int(0.12 * fps))
cent = (f[:, None] * S).sum(0) / (S.sum(0) + 1e-9)
ons = []
for p in pk:
	hi_lo = band_db(4000, 16000)[p] - band_db(30, 300)[p]
	ons.append({"t": round(float(t[p]), 3), "h": round(float(fl[p]), 2), "cent": int(cent[p]), "hilo": round(float(hi_lo), 1), "voice": bool(voiced[p])})
for o in ons:
	print(f"- {o['t']:6.3f}  {o['h']:.2f}  {o['cent']:5d}  {o['hilo']:+5.1f}  {'V' if o['voice'] else ''}")
out["onsets"] = ons
os.makedirs(WORK, exist_ok=True)
json.dump(out, open(os.path.join(WORK, "analysis.json"), "w"), indent=1)
