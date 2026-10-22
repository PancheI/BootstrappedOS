#!/usr/bin/env python3
"""
scout.py — measure candidate reference videos and rank them against a style profile.

  python3 scout.py fetch <url|file> [...]                 # download LOW-RES copies (480p) into scout/<id>.mp4 (cheap)
  python3 scout.py score scout/*.mp4 --profile launch     # metrics + score + contact sheet per video → scout/report.md
  python3 scout.py calibrate <name> liked1.mp4 [liked2.mp4]  # LEARN a profile from videos the user liked (preferred)
  python3 scout.py profiles                               # list profiles

Metrics per video (all local, no API cost):
  dur, fps          length and frame rate (source fps via ffprobe on the file)
  cuts_pm           hard cuts per minute (frame-diff spike > 4× local median and > 12)
  energy            mean per-frame change (how "alive" it is; a lively launch film ≈ 2–4)
  still_frac        share of frames that barely move (dead frames; lower = something on every beat)
  cam_cont          camera continuity 0–1: share of moving frames whose global motion is a smooth pan/zoom
                    (phase-correlation velocity close to the previous frame's) — high = one continuous camera
  ui_frac           share of frames that look like UI: light background + many small crisp edges
  text_kin          kinetic-type proxy: bursts of new edge mass appearing in the centre band (word reveals)
  bpm, bright       music tempo (hat/snare band autocorr, 3/4-alias aware) and >4 kHz energy share
Score = weighted closeness to the profile's targets (0–100). Also writes scout/<id>_sheet.jpg (1 fps).

Built-in hand profiles (learned ones in profiles.json are better: use calibrate on videos you liked):
  launch     continuous camera, UI-driven, kinetic type, fast bright music, about 30 s
  linear     slow engineered drifts, few cuts, very clean UI, calmer music
  punchy     many hard cuts, kinetic word slams, very fast music (fast social cut)
"""
import json, os, re, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw

OUT = os.environ.get("SCOUT_DIR", "scout")  # relative to the current directory
PROFILES = {
	# metric: (target, tolerance, weight)
	"launch": {"dur": (30, 15, 1), "cuts_pm": (1, 6, 2), "energy": (3, 2.5, 1), "still_frac": (0.1, 0.25, 1.5), "cam_cont": (0.8, 0.3, 3), "ui_frac": (0.8, 0.35, 3), "text_kin": (0.25, 0.2, 2), "bpm": (140, 25, 1.5), "bright": (0.3, 0.15, 1)},
	"linear": {"dur": (55, 25, 1), "cuts_pm": (3, 8, 1.5), "energy": (1.8, 1.5, 1), "still_frac": (0.25, 0.25, 1), "cam_cont": (0.85, 0.25, 3), "ui_frac": (0.85, 0.3, 3), "text_kin": (0.15, 0.15, 1.5), "bpm": (110, 30, 1), "bright": (0.22, 0.15, 0.5)},
	"punchy": {"dur": (30, 20, 1), "cuts_pm": (30, 20, 3), "energy": (6, 4, 2), "still_frac": (0.05, 0.15, 1), "cam_cont": (0.4, 0.4, 1), "ui_frac": (0.5, 0.4, 1), "text_kin": (0.4, 0.25, 2.5), "bpm": (150, 25, 2), "bright": (0.35, 0.15, 1)},
}


PFILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "profiles.json")
if os.path.exists(PFILE):
	PROFILES.update({k: v for k, v in json.load(open(PFILE)).items() if not k.startswith("_")})  # "_note" etc. are comments
FLOOR = {"dur": 12, "cuts_pm": 4, "energy": 1.0, "still_frac": 0.12, "cam_cont": 0.15, "ui_frac": 0.2, "text_kin": 0.08, "bpm": 15, "bright": 0.08}
WEIGHT = {"dur": 1, "cuts_pm": 1.5, "energy": 1.5, "still_frac": 1.5, "cam_cont": 3, "ui_frac": 2.5, "text_kin": 2, "bpm": 1.5, "bright": 1}


def calibrate(name, paths):
	"""Learn a profile from videos the user LIKED: target = mean metric, tolerance = max(spread, 35 % of value, floor)."""
	ms = [measure(p) for p in paths]
	prof = {}
	for k in FLOOR:
		vals = [m[k] for m in ms if m.get(k) is not None]
		if not vals:
			continue
		t = float(np.mean(vals)); tol = max(float(np.ptp(vals)) if len(vals) > 1 else 0, abs(t) * 0.35, FLOOR[k])
		prof[k] = (round(t, 3), round(tol, 3), WEIGHT[k])
	saved = json.load(open(PFILE)) if os.path.exists(PFILE) else {}
	saved[name] = prof; json.dump(saved, open(PFILE, "w"), indent=1)
	print(f"profile '{name}' from {len(ms)} video(s) → {PFILE}\n" + json.dumps(prof))


def sh(*a, **k):
	return subprocess.run(a, capture_output=True, text=k.get("text", True))


def fetch(srcs):
	os.makedirs(OUT, exist_ok=True)
	for s in srcs:
		if os.path.exists(s):
			vid = re.sub(r"\W+", "_", os.path.splitext(os.path.basename(s))[0])[:40]
			sh("ffmpeg", "-v", "error", "-y", "-i", s, "-vf", "scale=-2:480", "-c:v", "libx264", "-crf", "26", "-c:a", "aac", f"{OUT}/{vid}.mp4")
		else:
			vid = re.sub(r"\W+", "_", s.split("v=")[-1].split("/")[-1])[:40]
			r = None
			for fmt in ("bv*[height<=480]+ba/b[height<=480]/b", "18", "b"):
				r = sh("yt-dlp", "-q", "--no-update", "-f", fmt, "--merge-output-format", "mp4", "-o", f"{OUT}/{vid}.%(ext)s", s)
				if r.returncode == 0:
					break
			if r.returncode:
				print("FAIL", s, r.stderr.strip().splitlines()[-1:] if r.stderr else "")
				continue
			meta = sh("yt-dlp", "-q", "--no-update", "--skip-download", "--print", "%(title)s|%(fps)s|%(duration)s", s).stdout.strip()
			open(f"{OUT}/{vid}.meta", "w").write(f"{s}|{meta}")
		print("ok", vid)


def frames(path, fps=12, w=192, h=108):
	raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", f"fps={fps},scale={w}:{h}", "-pix_fmt", "gray", "-f", "rawvideo", "-"], capture_output=True).stdout
	return np.frombuffer(raw, np.uint8).reshape(-1, h, w).astype(np.float32)


def phase(a, b):
	A = np.fft.fft2(a - a.mean()); B = np.fft.fft2(b - b.mean()); R = A * np.conj(B); R /= np.abs(R) + 1e-6
	r = np.abs(np.fft.ifft2(R)); y, x = np.unravel_index(np.argmax(r), r.shape)
	H, W = a.shape
	return (x - W if x > W / 2 else x), (y - H if y > H / 2 else y), r.max()


def audio_metrics(path):
	raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vn", "-ac", "1", "-ar", "22050", "-f", "s16le", "-"], capture_output=True).stdout
	x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
	if len(x) < 22050 * 5:
		return None, None
	sr, hop = 22050, 256
	n = len(x) // hop; fr = x[: n * hop].reshape(n, hop)
	S = np.abs(np.fft.rfft(fr * np.hanning(hop), axis=1)); f = np.fft.rfftfreq(hop, 1 / sr)
	bright = float(S[:, f > 4000].sum() / (S.sum() + 1e-9))
	env = np.log1p(S[:, (f >= 1500) & (f < 11000)].sum(1) * 50); o = np.maximum(0, np.diff(env, prepend=env[0])); o -= o.mean()
	ac = np.correlate(o, o, "full")[len(o) - 1:]; ac /= ac[0] + 1e-9; fps = sr / hop
	best = max(((ac[int(round(60 / b * fps))] + 0.5 * ac[int(round(120 / b * fps))], b) for b in np.arange(80, 180.5, 0.5)))
	return float(best[1]), bright


def measure(path):
	fs = frames(path)
	n = len(fs)
	dur = float(sh("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", path).stdout.strip() or 0)
	meta = open(path[:-4] + ".meta").read().split("|") if os.path.exists(path[:-4] + ".meta") else [path, os.path.basename(path), "", ""]
	d = np.abs(np.diff(fs, axis=0)).mean((1, 2))
	med = np.array([np.median(d[max(0, i - 6): i + 7]) for i in range(len(d))])
	cuts = int(((d > 4 * med + 2) & (d > 12)).sum())
	moving = d > 0.6
	vel = [phase(fs[i + 1], fs[i]) for i in range(n - 1)]
	smooth = 0; mv = 0
	for i in range(1, n - 1):
		if moving[i] and not (d[i] > 12):
			mv += 1
			if abs(vel[i][0] - vel[i - 1][0]) + abs(vel[i][1] - vel[i - 1][1]) <= 2 and vel[i][2] > 0.05:
				smooth += 1
	gx = np.abs(np.diff(fs, axis=2)); edge = (gx > 18).mean((1, 2)); flat = (gx < 2).mean((1, 2))
	ui = float(((edge > 0.02) & (flat > 0.55)).mean())  # UI = crisp small edges on large flat areas (light OR dark)
	c = fs[:, 30:78, 20:172]; ce = np.abs(np.diff(c, axis=2)).mean((1, 2))
	text_kin = float((np.diff(ce) > 0.35).mean())
	bpm, bright = audio_metrics(path)
	return {"file": path, "title": meta[1] if len(meta) > 1 else path, "src": meta[0], "src_fps": meta[2] if len(meta) > 2 else "",
		"dur": round(dur, 1), "cuts_pm": round(cuts / max(dur / 60, 1e-6), 1), "energy": round(float(d.mean()), 2),
		"still_frac": round(float((d < 0.3).mean()), 2), "cam_cont": round(smooth / max(mv, 1), 2), "ui_frac": round(ui, 2),
		"text_kin": round(text_kin, 2), "bpm": bpm, "bright": round(bright, 2) if bright is not None else None}


def score(m, prof):
	tot = wsum = 0
	for k, (t, tol, w) in PROFILES[prof].items():
		v = m.get(k)
		if v is None:
			continue
		tot += w * max(0.0, 1 - abs(v - t) / tol); wsum += w
	sc = round(100 * tot / max(wsum, 1e-9), 1)
	# not a UI film (stock footage, talking heads, slides) → cap it, whatever the style numbers say
	if (m.get("ui_frac") or 0) < 0.3 and PROFILES[prof].get("ui_frac", (0,))[0] >= 0.5:
		sc = min(sc, 30.0)
	return sc


def sheet(path, out):
	raw = subprocess.run(["ffmpeg", "-v", "error", "-i", path, "-vf", "fps=1,scale=240:-2", "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True).stdout
	imgs = []; i = 0
	while True:
		j = raw.find(b"\x89PNG", i + 1)
		chunk = raw[i: j if j > 0 else len(raw)]
		if chunk:
			try:
				import io; imgs.append(Image.open(io.BytesIO(chunk)).convert("RGB"))
			except Exception:
				pass
		if j < 0:
			break
		i = j
	if not imgs:
		return
	w, h = imgs[0].size; cols = 8; rows = (len(imgs) + cols - 1) // cols
	S = Image.new("RGB", (cols * w, rows * (h + 14)), "white"); dr = ImageDraw.Draw(S)
	for k, im in enumerate(imgs):
		x, y = (k % cols) * w, (k // cols) * (h + 14); S.paste(im, (x, y + 14)); dr.text((x + 3, y + 1), f"{k}s", fill="black")
	S.save(out, quality=80)


def main():
	if len(sys.argv) < 2:
		return print(__doc__)
	cmd = sys.argv[1]
	if cmd == "profiles":
		return print(json.dumps(PROFILES, indent=1))
	if cmd == "calibrate":
		return calibrate(sys.argv[2], sys.argv[3:])
	if cmd == "fetch":
		return fetch(sys.argv[2:])
	if cmd == "score":
		args = sys.argv[2:]; prof = "launch"
		if "--profile" in args:
			k = args.index("--profile"); prof = args[k + 1]; args = args[:k] + args[k + 2:]
		rows = []
		for p in args:
			m = measure(p); m["score"] = score(m, prof)
			sheet(p, p[:-4] + "_sheet.jpg"); rows.append(m); print(json.dumps(m))
		rows.sort(key=lambda r: -r["score"])
		with open(f"{OUT}/report.md", "w") as f:
			f.write(f"# Reference scout — profile `{prof}`\n\n| rank | score | title | dur | cuts/min | energy | still | cam_cont | ui | text_kin | bpm | bright | sheet |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
			for i, r in enumerate(rows, 1):
				f.write(f"| {i} | {r['score']} | {r['title']} | {r['dur']} | {r['cuts_pm']} | {r['energy']} | {r['still_frac']} | {r['cam_cont']} | {r['ui_frac']} | {r['text_kin']} | {r['bpm']} | {r['bright']} | {r['file'][:-4]}_sheet.jpg |\n")
		print(f"→ {OUT}/report.md")


if __name__ == "__main__":
	main()
