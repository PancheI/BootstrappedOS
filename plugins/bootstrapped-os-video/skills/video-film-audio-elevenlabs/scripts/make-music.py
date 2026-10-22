#!/usr/bin/env python3
"""Music bed for the film, cut beat by beat from one of several candidate tracks.

Each candidate is played at the film tempo (timeline.FILM_BPM) and laid out as sections on the film grid:
  PRE    groove from the start, building into
  D1     the first drop, landing exactly on the first picture hit (timeline.HITS_REF[0])
  BUILD  4 beats plus a 2-beat stutter, into
  D2     the second drop on the second hit (timeline.HITS_REF[1]), running to the end
Section lengths are worked out from the timeline, so a timeline change only needs a re-run.
Automation: a low-pass that opens across each build, an optional dip under a pause in the voice (DIPS),
and a fade to the hard stop on the last frame.

Usage, from the project root:
  python3 <skill>/scripts/make-music.py            all candidates whose track is available
  python3 <skill>/scripts/make-music.py 1 3        only those candidates
  python3 <skill>/scripts/make-music.py --use=1    also copy candidate 1's bed to work/music.wav for mix.py
Writes public/remake/music-cand-N.wav (a 20 s preview around the first drop) and work/music_candN.wav (the full bed).

The source beats in CANDS are measured on each track (find beat0 with bpm.py). Candidate 3 is a track you
generate yourself with el_music.py at FILM_BPM (save it as work/el_music_prompt.mp3, then measure beat0 and
the section beats); it is skipped until that file exists. Keep candidates within about 10 % of FILM_BPM.
"""
import math, os, shutil, subprocess, sys, urllib.request
import numpy as np
from scipy.signal import butter, sosfilt

HERE = os.path.dirname(os.path.abspath(__file__))
# Paths: run from your project root, or set PROJECT_ROOT / AUDIO_DIR.
ROOT = os.environ.get("PROJECT_ROOT", os.getcwd())
AUDIO = os.environ.get("AUDIO_DIR", os.path.join(ROOT, "remake", "audio"))
WORK = os.path.join(AUDIO, "work")
SR = 48000
sys.path.insert(0, HERE)
from timeline import FPS, FRAMES, FILM, FILM_BPM, HITS_REF, film_t  # noqa: E402

N = round(FRAMES / FPS * SR)
HIT_A, HIT_B, END = film_t(HITS_REF[0]), film_t(HITS_REF[1]), FILM
FB = 60 / FILM_BPM  # one beat in film seconds
DIPS = [(5.5, 6.2)]  # example: film seconds of a dramatic pause in the voice; [] for none
FADE = 0.008
BUILD, STUTTER = 4, 2

# Source sections, in source beats: groove start, drop start and length, build start.
CANDS = {
	1: dict(name="Positive Energy", by="Michael Ramir C.", url="https://assets.mixkit.co/music/973/973.mp3",
		file="positive-energy.mp3", bpm=134.99, beat0=0.005, groove=31, drop=96, drop_len=56, build=92),
	2: dict(name="Party Like It's Your Birthday", by="Michael Ramir C.", url="https://assets.mixkit.co/music/1115/1115.mp3",
		file="party-birthday.mp3", bpm=138.0, beat0=0.005, groove=39, drop=112, drop_len=16, build=108),
	3: dict(name="ElevenLabs Music (music_v1), generated with el_music.py", by="ElevenLabs", url=None,
		file="el_music_prompt.mp3", bpm=FILM_BPM, beat0=0.0, groove=0, drop=32, drop_len=32, build=28,
		eq="highpass=f=35,lowshelf=f=110:g=-6,highshelf=f=6000:g=2"),  # leaner low end, crisper top
	4: dict(name="Happy Home", by="Michael Ramir C.", url="https://assets.mixkit.co/music/801/801.mp3",
		file="happy-home.mp3", bpm=140.0, beat0=0.422, groove=71, drop=128, drop_len=32, build=124),
}


def source_path(c):
	"""Local path of the candidate's track, downloading it if it has a download URL. None if unavailable."""
	path = os.path.join(WORK, c["file"])
	if os.path.exists(path):
		return path
	if not c["url"]:
		return None
	os.makedirs(WORK, exist_ok=True)
	try:
		urllib.request.urlretrieve(c["url"], path)
	except OSError as e:
		print(f"  could not download {c['url']}: {e}")
		return None
	return path


def load(path, c):
	k = c["bpm"] / FILM_BPM  # film seconds per source second
	af = f"atempo={1 / k:.6f}" + ("," + c["eq"] if "eq" in c else "")
	raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-af", af, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"],
		capture_output=True, check=True).stdout
	return np.frombuffer(raw, np.float32).reshape(-1, 2).astype(np.float64), k


def place(out, x, k, film_at, s0, s1):
	"""Overlay source seconds s0..s1 at film_at, with short overlapping fades at both ends."""
	f = int(FADE * SR)
	a = int(round(s0 * k * SR)) - f // 2
	b = int(round(s1 * k * SR)) + f // 2
	at = int(round(film_at * SR)) - f // 2
	if a < 0:
		at, a = at - a, 0
	seg = x[a:b].copy()
	if len(seg) < 2 * f:
		return
	seg[:f] *= np.linspace(0, 1, f)[:, None]
	seg[-f:] *= np.linspace(1, 0, f)[:, None]
	if at < 0:
		seg, at = seg[-at:], 0
	seg = seg[:max(0, len(out) - at)]
	out[at:at + len(seg)] += seg


def looped(start, length, beats):
	"""(source beat, n) pieces that fill `beats` film beats by looping a section of `length` beats."""
	pieces, left = [], beats
	while left > 0:
		n = min(length, left)
		pieces.append((start, n))
		left -= n
	return pieces


def sections(c):
	gap = round((HIT_B - HIT_A) / FB)
	if abs(gap * FB - (HIT_B - HIT_A)) > 0.02:
		print(f"  warning: the hits are {(HIT_B - HIT_A) / FB:.2f} beats apart; make it a whole number in timeline.py")
	if gap <= BUILD + STUTTER:
		sys.exit("The two hits are too close for a build; move them apart in timeline.py.")
	pre = math.ceil(HIT_A / FB)
	tail = math.ceil((END - HIT_B) / FB) + 1
	return {
		"pre": looped(c["groove"], max(1, c["drop"] - c["groove"] - BUILD), pre),
		"d1": looped(c["drop"], c["drop_len"], gap - BUILD - STUTTER),
		"build": [(c["build"], BUILD), (c["build"] + BUILD - STUTTER, STUTTER)],
		"d2": looped(c["drop"], c["drop_len"], tail),
	}


def build_bed(path, c):
	x, k = load(path, c)
	sb = 60 / c["bpm"]
	y = np.zeros((N, 2))
	parts = sections(c)
	t = HIT_A - sum(n for _, n in parts["pre"]) * FB
	marks = {}
	for part in ("pre", "d1", "build", "d2"):
		marks[part] = t
		for b0, n in parts[part]:
			s0 = c["beat0"] + b0 * sb
			place(y, x, k, t, s0, s0 + n * sb)
			t += n * FB
	tt = np.arange(N) / SR

	# low-pass that opens across each build and slams open on the drop
	lp = sosfilt(butter(2, 500, "low", fs=SR, output="sos"), y, axis=0)
	a1, a2 = HIT_A - BUILD * FB, marks["build"]
	wet = np.interp(tt, [a1 - 0.05, a1 + 0.3, HIT_A - 0.03, HIT_A, a2 - 0.05, a2 + 0.3, HIT_B - 0.03, HIT_B],
		[0, 0.8, 0.3, 0, 0, 0.75, 0.3, 0])[:, None]
	y = y * (1 - wet) + lp * wet * 1.3

	pts = [(0, 0)]
	for d0, d1 in DIPS:  # -18 dB under each pause in the voice
		pts += [(d0 - 0.12, 0), (d0, -18), (d1, -18), (d1 + 0.3, 0)]
	pts += [(END - 1.57, 0), (END - 0.47, -18), (END - 0.05, -30), (END, -60)]
	g = 10 ** (np.interp(tt, *zip(*sorted(pts))) / 20)
	return (y * g[:, None]).astype(np.float32), marks


def write(p, y, pcm="pcm_f32le"):
	subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", pcm, p],
		input=np.ascontiguousarray(y, np.float32).tobytes(), check=True)


def preview(y, n):
	a = max(0.0, min(HIT_A - 12.0, END - 20.0))
	pv = y[int(a * SR):int(min(END, a + 20.0) * SR)].astype(np.float64)
	f = int(0.3 * SR)
	pv[-f:] *= np.linspace(1, 0, f)[:, None]
	pv[:int(0.05 * SR)] *= np.linspace(0, 1, int(0.05 * SR))[:, None]
	pv *= 10 ** (-3 / 20) / (np.abs(pv).max() + 1e-9)
	write(os.path.join(ROOT, "public", "remake", f"music-cand-{n}.wav"), pv, "pcm_s16le")


def main():
	pick = [int(a) for a in sys.argv[1:] if a.isdigit()] or list(CANDS)
	os.makedirs(os.path.join(ROOT, "public", "remake"), exist_ok=True)
	os.makedirs(WORK, exist_ok=True)
	built = []
	for n in pick:
		c = CANDS[n]
		path = source_path(c)
		if path is None:
			print(f"cand {n} {c['name']}: skipped (no {c['file']} in {WORK})")
			continue
		y, marks = build_bed(path, c)
		write(os.path.join(WORK, f"music_cand{n}.wav"), y)
		preview(y, n)
		built.append(n)
		print(f"cand {n} {c['name']}: {c['bpm']} -> {FILM_BPM} BPM ({(FILM_BPM / c['bpm'] - 1) * 100:+.1f} %), "
			+ ", ".join(f"{k} @{v:.2f}" for k, v in marks.items()))
	use = [int(a.split("=")[1]) for a in sys.argv if a.startswith("--use=")]
	if use:
		if use[0] not in built and not os.path.exists(os.path.join(WORK, f"music_cand{use[0]}.wav")):
			sys.exit(f"cand {use[0]} was not built")
		shutil.copy(os.path.join(WORK, f"music_cand{use[0]}.wav"), os.path.join(WORK, "music.wav"))
		print("work/music.wav <- cand", use[0])


if __name__ == "__main__":
	main()
