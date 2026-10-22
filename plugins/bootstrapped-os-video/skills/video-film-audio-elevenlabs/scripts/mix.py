#!/usr/bin/env python3
"""Remake mix: VO + music (ducked under the voice by a gain envelope from the VO) + SFX,
then two-pass ffmpeg loudnorm to -14 LUFS integrated / -1 dBTP.
Inputs: work/vo_track.wav, work/music.wav, work/sfx.wav (make-vo.py, make-music.py, make-sfx.py).
Output: public/remake/mix.wav (48 kHz stereo 24-bit, exactly timeline.FRAMES frames @ 60 fps).

Run from the project root: python3 <skill>/scripts/mix.py   (or set PROJECT_ROOT / AUDIO_DIR)
"""
import json, os, re, subprocess, sys
import numpy as np
from scipy.signal import butter, sosfilt

HERE = os.path.dirname(os.path.abspath(__file__))
# Paths: run from your project root, or set PROJECT_ROOT / AUDIO_DIR.
ROOT = os.environ.get("PROJECT_ROOT", os.getcwd())
AUDIO = os.environ.get("AUDIO_DIR", os.path.join(ROOT, "remake", "audio"))
WORK = os.path.join(AUDIO, "work")
OUT = os.path.join(ROOT, "public/remake/mix.wav")
OUT_NOV = os.path.join(ROOT, "public/remake/music_sfx_nov.wav")  # music + SFX, no VO
SR = 48000
sys.path.insert(0, HERE)
from timeline import FPS, FRAMES  # film length in frames @ 60 fps
N = round(FRAMES / FPS * SR)

VO_DB = -17.0  # active-speech RMS of the voice before the master
MUSIC_DB = -20.0  # music RMS where no one speaks
DUCK_DB = -7.0  # music under the voice
SFX_DB = -1.0  # SFX bus trim


def load(name, ch):
	raw = subprocess.run(["ffmpeg", "-v", "error", "-i", os.path.join(WORK, name), "-ac", str(ch), "-ar", str(SR), "-f", "f32le", "-"],
		capture_output=True, check=True).stdout
	x = np.frombuffer(raw, np.float32).reshape(-1, ch).astype(np.float64)
	x = x[:N]
	return np.pad(x, ((0, N - len(x)), (0, 0)))


def rms_db(x):
	return 20 * np.log10(np.sqrt(np.mean(x ** 2)) + 1e-12)


def frame_rms(x, w):
	n = len(x) // w
	return np.sqrt((x[:n * w].reshape(n, w) ** 2).mean(1))


def smooth(g, attack, release, rate):
	"""One-pole follower on a per-sample target: fast toward lower gain (attack), slow back (release)."""
	a, r = np.exp(-1 / (attack * rate)), np.exp(-1 / (release * rate))
	out = np.empty_like(g)
	y = g[0]
	for i, v in enumerate(g):
		c = a if v < y else r
		y = c * y + (1 - c) * v
		out[i] = y
	return out


def main():
	vo = load("vo_track.wav", 1)[:, 0]
	music = load("music.wav", 2)
	sfx = load("sfx.wav", 2)

	# voice: high-pass, level by active-speech RMS
	vo = sosfilt(butter(2, 90, "high", fs=SR, output="sos"), vo)
	w = int(0.02 * SR)
	fr = frame_rms(vo, w)
	speech = fr > 10 ** (-45 / 20)
	vo *= 10 ** ((VO_DB - 20 * np.log10(np.sqrt((fr[speech] ** 2).mean()))) / 20)

	# music: level on the voice-free stretches, then duck under the voice
	fr = frame_rms(vo, w)
	speech = np.repeat(fr > 10 ** ((VO_DB - 26) / 20), w)
	speech = np.pad(speech, (0, N - len(speech)))
	mfr = np.repeat(frame_rms(music.mean(1), w), w)
	mfr = np.pad(mfr, (0, N - len(mfr)))
	free = (~speech) & (mfr > 10 ** (-40 / 20))
	music *= 10 ** ((MUSIC_DB - 20 * np.log10(np.sqrt((mfr[free] ** 2).mean()))) / 20)
	bed = music + sfx * 10 ** (SFX_DB / 20)  # no-VO version (music un-ducked + SFX) for checks
	# hold the duck through short gaps between words (≤ 250 ms)
	hold = np.convolve(speech.astype(float), np.ones(int(0.25 * SR)), "same") > 0
	target = np.where(hold, 10 ** (DUCK_DB / 20), 1.0)
	duck = smooth(target[::48], 0.06, 0.35, SR / 48)  # 1 kHz follower, upsampled
	duck = np.repeat(duck, 48)[:N]
	music *= duck[:, None]

	mix = music + vo[:, None] + sfx * 10 ** (SFX_DB / 20)
	pre = os.path.join(WORK, "premix.wav")
	write(pre, mix)

	# peak control first (so loudnorm can stay linear): gain to ≈-14 LUFS, 4x-oversampled limiter at -2 dBFS
	lim = os.path.join(WORK, "limited.wav")
	gain = -14.0 - float(measure(pre)["input_i"])
	subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", pre, "-af",
		f"volume={gain:.2f}dB,aresample={SR * 4},alimiter=limit=0.79:attack=1:release=60:level=false,aresample={SR}",
		"-c:a", "pcm_f32le", lim], check=True)
	# two-pass loudnorm → -14 LUFS integrated, true peak ≤ -1 dBTP, linear (a pure gain)
	j = measure(lim)
	af = (f"{LOUDNORM}:measured_I={j['input_i']}:measured_TP={j['input_tp']}:measured_LRA={j['input_lra']}"
		f":measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true:print_format=json")
	os.makedirs(os.path.dirname(OUT), exist_ok=True)
	r = subprocess.run(["ffmpeg", "-hide_banner", "-y", "-i", lim, "-af", f"{af},aresample={SR},apad=whole_len={N},atrim=end_sample={N}",
		"-ar", str(SR), "-ac", "2", "-c:a", "pcm_s24le", OUT], capture_output=True, text=True, check=True).stderr
	j2 = json.loads(r[r.rindex("{"):r.rindex("}") + 1])
	print(f"premix {gain:+.2f} dB → limiter; loudnorm pass 1:", {k: j[k] for k in ("input_i", "input_tp", "input_lra")}, "→", j2["normalization_type"])
	print("→", OUT)

	# music + SFX without VO, at the SAME gain chain as the mix (so it lines up with mix.wav level-wise)
	pre2 = os.path.join(WORK, "premix_nov.wav")
	write(pre2, bed)
	post = -14.0 - float(j["input_i"])  # the linear loudnorm gain applied to the mix
	os.makedirs(os.path.dirname(OUT_NOV), exist_ok=True)
	subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", pre2, "-af",
		f"volume={gain:.2f}dB,aresample={SR * 4},alimiter=limit=0.79:attack=1:release=60:level=false,aresample={SR},"
		f"volume={post:.2f}dB,apad=whole_len={N},atrim=end_sample={N}", "-ar", str(SR), "-ac", "2", "-c:a", "pcm_s24le", OUT_NOV], check=True)
	print("→", OUT_NOV)


LOUDNORM = "loudnorm=I=-14:TP=-1.2:LRA=11"


def measure(p):
	m = subprocess.run(["ffmpeg", "-hide_banner", "-i", p, "-af", LOUDNORM + ":print_format=json", "-f", "null", "-"], capture_output=True, text=True).stderr
	return json.loads(m[m.rindex("{"):m.rindex("}") + 1])


def write(p, x):
	subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_f32le", p],
		input=np.ascontiguousarray(x, np.float32).tobytes(), check=True)


main()
