#!/usr/bin/env python3
"""Beats and downbeats of a music file -> music-beats.json (seconds).

Uses librosa's beat tracker if librosa is installed (pip install librosa). Without it, it falls back to the
same comb-filter tempo estimate as bpm.py (numpy + scipy + ffmpeg) and lays a steady beat grid from the
best phase. The fallback assumes a steady tempo, which suits most launch-film tracks.

Usage: python3 music_beats.py music.mp3 [--out music-beats.json]
"""
import argparse, json, subprocess
import numpy as np


def with_librosa(path):
	import librosa
	y, sr = librosa.load(path, sr=None, mono=True)
	tempo, frames = librosa.beat.beat_track(y=y, sr=sr)
	tempo = float(tempo if not hasattr(tempo, "__len__") else tempo[0])
	return tempo, [round(float(t), 3) for t in librosa.frames_to_time(frames, sr=sr)]


def with_comb(path, sr=22050):
	from scipy.signal import stft
	raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"],
		capture_output=True, check=True).stdout
	m = np.frombuffer(raw, np.float32)
	hop = 110
	_, _, Z = stft(m, sr, nperseg=1024, noverlap=1024 - hop)
	L = np.log1p(100 * np.abs(Z))
	fps = sr / hop
	e = np.concatenate([[0], np.maximum(np.diff(L, axis=1), 0).sum(0)])
	e = np.maximum(e - np.convolve(e, np.ones(int(fps)) / fps, "same"), 0)
	best = (0.0, 120.0, 0.0)
	for bpm in np.arange(70, 180, 0.05):
		per = 60 / bpm * fps
		n = int(len(e) / per) - 1
		if n < 2:
			continue
		idx = (np.arange(n)[:, None] * per + np.arange(int(per))[None, :]).astype(int)
		prof = e[idx].mean(0)
		score = prof.max() / (prof.mean() + 1e-9)
		if score > best[0]:
			best = (score, float(bpm), prof.argmax() / fps)
	_, bpm, phase = best
	dur = len(m) / sr
	return bpm, [round(float(t), 3) for t in np.arange(phase, dur, 60 / bpm)]


def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("audio")
	ap.add_argument("--out", default="music-beats.json")
	a = ap.parse_args()
	try:
		tempo, beats = with_librosa(a.audio)
		how = "librosa"
	except ImportError:
		tempo, beats = with_comb(a.audio)
		how = "comb filter (librosa not installed)"
	out = {"tempo": round(tempo, 1), "beats": beats, "downbeats": beats[::4], "method": how}
	json.dump(out, open(a.out, "w"), indent=1)
	print(f"{len(beats)} beats at ~{out['tempo']} BPM ({how}) -> {a.out}")


if __name__ == "__main__":
	main()
