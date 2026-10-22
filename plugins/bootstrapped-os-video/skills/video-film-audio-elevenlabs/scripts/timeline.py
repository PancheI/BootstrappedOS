"""Film timeline shared by the audio scripts: REF time -> film (output) time, plus the music grid.
Mirrors src/Remake/Remake.tsx (STRETCHES + CUTS, in REF frames). That file is the source of truth;
keep remake/tools/stretches.json equal to it too.

The values below are a neutral EXAMPLE: a 35 s reference cut to a 30 s film at 144 BPM
(one beat = 25 frames at 60 fps). Replace them with your own film's values.

  stretch (S0, S1, EXT): REF frames S0..S1 play EXT frames longer (EXT < 0 = faster); later frames shift by EXT
  cut (C0, C1): REF frames C0..C1 are removed; later frames shift by -(C1-C0+1)
Keep every EXT and every cut length a whole number of beats, so the music stays on its grid.
"""
FPS = 60
REF_FRAMES = 2100  # example: a 35 s reference
STRETCHES = [(300, 360, 100)]  # example: hold 4 beats on a screen the viewer must read
CUTS = [(1200, 1599)]  # example: remove 16 beats the story doesn't need
FRAMES = REF_FRAMES + sum(e for *_, e in STRETCHES) - sum(c1 - c0 + 1 for c0, c1 in CUTS)  # 1800 in the example
FILM = FRAMES / FPS  # 30.0 s in the example

# Music grid (used by make-music.py and make-sfx.py)
FILM_BPM = 144.0  # the tempo the music bed plays at in the film
HITS_REF = (10.0, 1900 / 60)  # REF seconds of the two picture hits the music drops land on (example)

_EVENTS = sorted([("s", a, b, e) for a, b, e in STRETCHES] + [("c", a, b, 0) for a, b in CUTS], key=lambda x: x[1])


def film_f(ref_f):
	"""Output frame (float) of REF frame ref_f, or None if that frame was cut."""
	shift = 0.0
	for kind, a, b, ext in _EVENTS:
		if kind == "s":
			if ref_f <= a:
				return ref_f + shift
			if ref_f <= b:
				return a + shift + (ref_f - a) * (b - a + ext) / (b - a)
			shift += ext
		else:
			if ref_f < a:
				return ref_f + shift
			if ref_f <= b:
				return None
			shift -= b - a + 1
	return ref_f + shift


def film_t(t):
	"""Film seconds of REF second t (None inside a cut)."""
	f = film_f(t * FPS)
	return None if f is None else f / FPS
