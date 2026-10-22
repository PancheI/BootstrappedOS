#!/usr/bin/env python3
"""Remake SFX: synthesised with numpy (no samples) and placed on the REF hit times
(frame-diff spikes + non-voice onsets, see ANALYSIS.md).  Writes work/sfx.wav (48 kHz stereo).

Run from the project root: python3 <skill>/scripts/make-sfx.py
The EVENTS table below is a neutral EXAMPLE for a 30 s film: replace it with your own hits.
"""
import os, subprocess, sys
import numpy as np
from scipy.signal import butter, sosfilt

HERE = os.path.dirname(os.path.abspath(__file__))
# Paths: run from your project root, or set PROJECT_ROOT / AUDIO_DIR.
ROOT = os.environ.get("PROJECT_ROOT", os.getcwd())
AUDIO = os.environ.get("AUDIO_DIR", os.path.join(ROOT, "remake", "audio"))
WORK = os.path.join(AUDIO, "work")
SR = 48000
sys.path.insert(0, HERE)
from timeline import CUTS, FPS, FRAMES, HITS_REF, film_f, film_t  # noqa: E402  REF -> film time (holds, speed-ups, cuts)
N = round(FRAMES / FPS * SR)
rng = np.random.default_rng(7)


def env(n, a, d):
	"""Attack a samples, exponential decay with time-constant d samples."""
	e = np.exp(-np.arange(n) / max(d, 1))
	if a:
		e[:a] *= np.linspace(0, 1, a)
	return e


def bandnoise(n, lo, hi):
	return sosfilt(butter(2, [lo, hi], "band", fs=SR, output="sos"), rng.standard_normal(n))


def sweep_noise(n, f0, f1, q=1.5, blocks=64):
	"""Noise through a band-pass whose centre glides f0→f1 (block-wise)."""
	x = rng.standard_normal(n)
	out = np.zeros(n)
	edges = np.linspace(0, n, blocks + 1).astype(int)
	for i in range(blocks):
		fc = f0 * (f1 / f0) ** (i / (blocks - 1))
		lo, hi = fc / (1 + 1 / q), min(fc * (1 + 1 / q), SR / 2 - 100)
		seg = sosfilt(butter(2, [lo, hi], "band", fs=SR, output="sos"), x[max(0, edges[i] - 2000):edges[i + 1]])
		out[edges[i]:edges[i + 1]] = seg[-(edges[i + 1] - edges[i]):]
	return out


class Peak(np.ndarray):
	"""A sound placed by its loudest point (whooshes) or its end (risers) instead of its start."""


def norm(x, peak=1.0):
	return x / (np.abs(x).max() + 1e-9) * peak


# ── sounds (mono unless noted; pan applied at placement)
def click():
	n = int(0.035 * SR)
	tick = bandnoise(n, 2500, 9000) * env(n, 0, 0.002 * SR)
	body = np.sin(2 * np.pi * 1800 * np.arange(n) / SR) * env(n, 0, 0.004 * SR) * 0.5
	return norm(tick + body, 0.9)


def pop(f0=900, f1=320, dur=0.09):
	n = int(dur * SR)
	t = np.arange(n) / SR
	f = f1 + (f0 - f1) * np.exp(-t / (dur / 4))
	s = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, int(0.002 * SR), dur / 3.5 * SR)
	tr = bandnoise(n, 1500, 7000) * env(n, 0, 0.003 * SR) * 0.3
	return norm(s + tr, 0.8)


def whoosh(dur=0.45, f0=500, f1=3500, peak_at=0.6):
	n = int(dur * SR)
	x = sweep_noise(n, f0, f1)
	t = np.linspace(0, 1, n)
	shape = np.where(t < peak_at, (t / peak_at) ** 2, ((1 - t) / (1 - peak_at)) ** 1.5)
	return norm(x * shape, 0.8).view(Peak)


def riser(dur=1.5):
	n = int(dur * SR)
	t = np.linspace(0, 1, n)
	x = sweep_noise(n, 300, 7000, q=2.5) * t ** 2.5
	ph = np.cumsum(220 * 2 ** (2.5 * t)) / SR
	tone = np.sin(2 * np.pi * ph) * t ** 3 * 0.25
	out = x + tone
	out[-int(0.01 * SR):] *= np.linspace(1, 0, int(0.01 * SR))
	return norm(out, 0.7).view(Peak)


def impact(dur=1.2):
	n = int(dur * SR)
	t = np.arange(n) / SR
	f = 45 + 70 * np.exp(-t / 0.04)
	boom = np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, int(0.002 * SR), 0.28 * SR)
	crack = bandnoise(n, 800, 9000) * env(n, 0, 0.05 * SR) * 0.6
	air = bandnoise(n, 4000, 14000) * env(n, int(0.01 * SR), 0.35 * SR) * 0.15
	return norm(boom + crack + air, 0.95)


def ding(f=1320, dur=1.1):
	n = int(dur * SR)
	t = np.arange(n) / SR
	s = sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t / (dur / (1 + 2 * k)))
		for k, (r, a) in enumerate([(1, 1), (2.0, 0.35), (2.76, 0.18), (5.4, 0.06)]))
	s[:int(0.002 * SR)] *= np.linspace(0, 1, int(0.002 * SR))
	return norm(s, 0.6)


def sparkle(dur=0.9):
	n = int(dur * SR)
	out = np.zeros(n)
	for k in range(9):
		at = int(k / 9 * 0.55 * SR)
		f = rng.uniform(2600, 5200)
		m = n - at
		tt = np.arange(m) / SR
		out[at:] += np.sin(2 * np.pi * f * tt) * np.exp(-tt / 0.12) * rng.uniform(0.4, 1)
	return norm(out, 0.5)


def typing(count, dur):
	n = int((dur + 0.1) * SR)
	out = np.zeros(n)
	for k in range(count):
		at = int((k / count * dur + rng.uniform(-0.012, 0.012)) * SR)
		c = click() * rng.uniform(0.35, 0.7)
		c = sosfilt(butter(2, rng.uniform(3000, 6000), "high", fs=SR, output="sos"), c)
		at = max(0, at)
		out[at:at + len(c)] += c[:n - at]
	return norm(out, 0.6)


def burst():
	"""Particle burst (radial splash): impact without the sub, plus a sparkle tail."""
	a = impact(0.8) * 0.6
	s = sparkle(0.9)
	n = max(len(a), len(s))
	return norm(np.pad(a, (0, n - len(a))) + np.pad(s, (0, n - len(s))), 0.8)


# Sounds on the film timeline itself (film seconds): a whoosh carries each cut,
# because the picture jumps straight to the next REF shot there.
JUMPS = [(film_f(c1 + 1) / FPS, whoosh(0.4, 500, 3500), -14, 0.0) for _, c1 in CUTS]

# (time s, sound, gain dB, pan -1..1) in REF time (shifted to film time in main).
# Times anchor the sound's hit (whooshes: their peak, risers: their end).
# A neutral EXAMPLE for a 30 s launch film (see timeline.py): replace it with your own hits.
EVENTS = [
	(0.50, click(), -8, 0.2),  # the cursor clicks the main button
	(0.70, whoosh(0.5, 300, 2500), -10, 0.0),  # the screen changes
	(3.00, pop(700, 380), -14, -0.3),  # a card appears
	(5.20, pop(820, 340), -15, 0.3),  # a second card, during the hold
	(HITS_REF[0], riser(1.5), -12, 0.0),  # build into the first drop
	(HITS_REF[0], impact(1.2), -7, 0.0),  # the first drop: the product appears
	(HITS_REF[0] + 0.02, burst(), -12, 0.0),
	(14.00, typing(10, 0.5), -16, 0.0),  # typing into the product
	(15.20, click(), -8, 0.25),  # clicks the button
	(17.00, whoosh(0.4, 600, 4500), -14, 0.0),  # push to the result
	(18.00, ding(1480, 0.9), -12, 0.25),  # the result lands
	(24.00, pop(900, 360), -16, 0.0),  # inside the example cut: dropped
	(HITS_REF[1], impact(1.0), -8, 0.0),  # the second drop: the big number
	(HITS_REF[1] + 1.30, sparkle(0.9), -15, 0.0),  # the logo settles
	(34.30, click(), -7, -0.15),  # the cursor clicks the call to action
	(34.32, ding(1320, 1.1), -15, 0.0),
]


def main():
	out = np.zeros((N, 2))
	# REF events → film time; those inside a cut span are dropped
	events = [(film_t(at), snd, db, pan) for at, snd, db, pan in EVENTS if film_t(at) is not None] + JUMPS
	print("dropped (inside cuts):", [at for at, *_ in EVENTS if film_t(at) is None])
	for at, snd, db, pan in events:
		snd = snd * 10 ** (db / 20)
		# whooshes/risers are anchored on their peak/end, one-shots on their start
		peak = int(np.argmax(np.convolve(np.abs(snd), np.ones(480) / 480, "same"))) if isinstance(snd, Peak) else 0
		snd = np.asarray(snd)
		k = int(round(at * SR)) - peak
		a0 = max(0, -k)
		k = max(0, k)
		seg = snd[a0:a0 + N - k]
		l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
		out[k:k + len(seg), 0] += seg * l * 1.414
		out[k:k + len(seg), 1] += seg * r * 1.414
	os.makedirs(WORK, exist_ok=True)
	p = os.path.join(WORK, "sfx.wav")
	subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_f32le", p],
		input=np.ascontiguousarray(out, np.float32).tobytes(), check=True)
	print("→", p, len(events), "events, peak", f"{20 * np.log10(np.abs(out).max()):.1f} dBFS")


if __name__ == "__main__":
	main()
