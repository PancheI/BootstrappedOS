#!/usr/bin/env python3
"""
Cost-aware ElevenLabs TTS with timestamps: cache + usage log + context-window patching.

WHY: re-recording the whole script for every change can easily cost 4x the characters you need.
This tool makes a change cost only the
changed line (+ a little context), never pays twice for the same text, and logs every character.

Usage
  # full take (only when the script is new or the voice/model changes)
  el_tts.py full  --script lines.json --out takes/take_base.json
  # patch ONE changed line: sends [prev line] + NEW line + [next line] (same voice/model),
  # returns only the new line's audio+timestamps cut out of that short take
  el_tts.py patch --script lines.json --line 07 --out takes/line07_v2.json
  # dry-run: print what it would cost, send nothing
  el_tts.py patch ... --dry
  # usage report
  el_tts.py usage

lines.json = [{"id":"01a","text":"Mmm…"}, {"id":"01b","text":"I launched today… and nobody signed up."}, ...]

Env: ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID in the environment or <project>/.env (never printed).
Run from the project root (or set PROJECT_ROOT). Default model: eleven_v3.
Cache: .el_cache/<sha1>.json keyed by (voice, model, settings, exact text sent). A re-run of the same
request is free. Usage log: .el_cache/usage.csv (time, mode, chars, cached, note).

Tips baked in:
- Draft timing with --model eleven_flash_v2_5 (much cheaper), then render the FINAL once with eleven_v3.
- Default takes=1; only ask for a 2nd take if the Whisper / slot-fit check fails.
- Batch all copy changes and patch them in one run; lock the script with the user (beat table) first.
- A timeline stretch never needs TTS: re-place the cached lines.
"""
import argparse, base64, csv, hashlib, json, os, sys, time, urllib.request

ROOT = os.environ.get("PROJECT_ROOT", os.getcwd())
CACHE = os.path.join(ROOT, ".el_cache")


def _env(name):
	"""Value from the environment, else from <ROOT>/.env."""
	v = os.environ.get(name)
	p = os.path.join(ROOT, ".env")
	if not v and os.path.exists(p):
		for ln in open(p):
			if ln.startswith(name + "="):
				v = ln.split("=", 1)[1].strip().strip("'\"")
	return v


VOICE = _env("ELEVENLABS_VOICE_ID")
MODEL = "eleven_v3"


def key():
	k = os.environ.get("ELEVENLABS_API_KEY")
	if k:
		return k
	p = os.path.join(ROOT, ".env")
	if os.path.exists(p):
		for ln in open(p):
			if ln.startswith("ELEVENLABS_API_KEY="):
				return ln.split("=", 1)[1].strip().strip("'\"")
	sys.exit("no ELEVENLABS_API_KEY in env or .env")


def log(mode, chars, cached, note=""):
	os.makedirs(CACHE, exist_ok=True)
	new = not os.path.exists(os.path.join(CACHE, "usage.csv"))
	with open(os.path.join(CACHE, "usage.csv"), "a", newline="") as f:
		w = csv.writer(f)
		if new:
			w.writerow(["time", "mode", "chars", "cached", "note"])
		w.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), mode, chars, int(cached), note])


def tts(text, voice, model, settings, mode, note, dry=False):
	body = {"text": text, "model_id": model}
	if settings:
		body["voice_settings"] = settings
	h = hashlib.sha1(json.dumps([voice, body], sort_keys=True).encode()).hexdigest()
	path = os.path.join(CACHE, h + ".json")
	if os.path.exists(path):
		log(mode, len(text), True, note)
		print(f"cache hit ({len(text)} chars, free)")
		return json.load(open(path))
	print(f"{'DRY ' if dry else ''}request: {len(text)} chars · {model}")
	if dry:
		return None
	req = urllib.request.Request(f"https://api.elevenlabs.io/v1/text-to-speech/{voice}/with-timestamps",
		data=json.dumps(body).encode(), headers={"xi-api-key": key(), "Content-Type": "application/json"})
	with urllib.request.urlopen(req, timeout=300) as r:
		j = json.load(r)
		cost = r.headers.get("x-character-count") or r.headers.get("character-cost") or len(text)
	os.makedirs(CACHE, exist_ok=True)
	json.dump(j, open(path, "w"))
	log(mode, cost, False, note)
	return j


def cut(j, start_char, end_char):
	"""Start and end seconds of characters [start_char, end_char) in a with-timestamps response."""
	a = j.get("alignment") or j["normalized_alignment"]
	s = a["character_start_times_seconds"][start_char]
	e = a["character_end_times_seconds"][end_char - 1]
	return s, e


def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("mode", choices=["full", "patch", "usage"])
	ap.add_argument("--script")
	ap.add_argument("--line")
	ap.add_argument("--out")
	ap.add_argument("--voice", default=VOICE, help="ElevenLabs voice id (default: ELEVENLABS_VOICE_ID)")
	ap.add_argument("--model", default=MODEL)
	ap.add_argument("--context", type=int, default=1, help="neighbour lines on each side for patch")
	ap.add_argument("--settings", help='voice_settings JSON, e.g. \'{"stability":0.5,"similarity_boost":0.8}\' (match the base take)')
	ap.add_argument("--dry", action="store_true")
	a = ap.parse_args()
	settings = json.loads(a.settings) if a.settings else None
	if a.mode != "usage" and not a.voice:
		sys.exit("set ELEVENLABS_VOICE_ID (env or .env) or pass --voice <your voice id>")
	if a.mode == "usage":
		p = os.path.join(CACHE, "usage.csv")
		if not os.path.exists(p):
			return print("no usage yet")
		rows = list(csv.DictReader(open(p)))
		paid = sum(int(float(r["chars"])) for r in rows if r["cached"] == "0")
		saved = sum(int(float(r["chars"])) for r in rows if r["cached"] == "1")
		return print(f"paid chars: {paid} · served from cache: {saved} · requests: {len(rows)}")
	lines = json.load(open(a.script))
	if a.mode == "full":
		text = " ".join(l["text"] for l in lines)
		j = tts(text, a.voice, a.model, settings, "full", a.script, a.dry)
		if j:
			j["_lines"] = lines
			json.dump(j, open(a.out, "w"))
		return
	i = next(k for k, l in enumerate(lines) if l["id"] == a.line)
	lo, hi = max(0, i - a.context), min(len(lines), i + a.context + 1)
	parts = [l["text"] for l in lines[lo:hi]]
	text = " ".join(parts)
	start = len(" ".join(parts[: i - lo])) + (1 if i > lo else 0)
	end = start + len(lines[i]["text"])
	j = tts(text, a.voice, a.model, settings, "patch", f"line {a.line}", a.dry)
	if j:
		s, e = cut(j, start, end)
		json.dump({"line": a.line, "text": lines[i]["text"], "start_s": s, "end_s": e, "sent": text, "take": j}, open(a.out, "w"))
		print(f"line {a.line}: {s:.2f}–{e:.2f}s inside a {len(text)}-char context take → {a.out}")


if __name__ == "__main__":
	main()
