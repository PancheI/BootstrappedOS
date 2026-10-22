#!/usr/bin/env python3
"""Generate ONE music bed with ElevenLabs Music (music_v1). Generate once per project, then re-cut locally.

Usage (run from your project root, or pass --root):
  python3 el_music.py prompt --bpm 144 --length 30 --out remake/audio/work/el_music_prompt.mp3 \
      --prompt "Instrumental only, no vocals. Energetic, bright electronic pop at 144 BPM ..."
  python3 el_music.py plan   --out remake/audio/work/el_music_plan.mp3     # composition-plan example below

Key: ELEVENLABS_API_KEY from the environment or <root>/.env (never printed).
Add --dry to see the length before paying. Generating costs credits, so get a yes first.
Note: composition plans tended to ignore section timings; a plain prompt plus a local re-cut worked better.
"""
import argparse, json, os, sys, urllib.request, urllib.error


def api_key(root):
	k = os.environ.get("ELEVENLABS_API_KEY")
	p = os.path.join(root, ".env")
	if not k and os.path.exists(p):
		for ln in open(p):
			if ln.startswith("ELEVENLABS_API_KEY="):
				k = ln.split("=", 1)[1].strip().strip("'\"")
	if not k:
		sys.exit("ELEVENLABS_API_KEY not set (env or .env in the project root)")
	return k


G = ["instrumental", "energetic bright electronic pop", "future house", "144 BPM", "crisp 16th-note hi-hats", "snappy claps on 2 and 4",
	"driving four-on-the-floor drums", "optimistic modern tech product launch ad", "punchy but light low end", "sparkling synth plucks"]
NG = ["vocals", "singing", "voice", "lo-fi", "chill", "ambient", "slow", "heavy sub bass", "dark"]
PLAN = {"positive_global_styles": G, "negative_global_styles": NG, "sections": [
	{"section_name": "Groove", "positive_local_styles": ["drums and hi-hats from the very first beat", "bouncy plucks", "energetic groove"], "negative_local_styles": ["intro fade-in", "silence"], "duration_ms": 8670, "lines": []},
	{"section_name": "Build", "positive_local_styles": ["filtered build-up", "snare roll", "rising riser", "tension"], "negative_local_styles": [], "duration_ms": 3000, "lines": []},
	{"section_name": "Drop", "positive_local_styles": ["full drop", "big energetic chorus", "bright supersaw chords", "driving hats and claps"], "negative_local_styles": ["breakdown"], "duration_ms": 12500, "lines": []},
	{"section_name": "Build 2", "positive_local_styles": ["short build-up", "snare roll", "riser"], "negative_local_styles": [], "duration_ms": 2500, "lines": []},
	{"section_name": "Final drop", "positive_local_styles": ["biggest drop", "maximum energy", "ends on a clean final hit with a short tail"], "negative_local_styles": ["fade out"], "duration_ms": 3330, "lines": []}]}
DEFAULT_PROMPT = ("Instrumental only, no vocals. Energetic, bright, fast electronic pop / future-house product-launch track at {bpm} BPM, "
	"crisp 16th-note hi-hats and snappy claps driving from the very first second, punchy but not bass-heavy, optimistic, modern tech ad. "
	"Groove from 0 s, a filtered build into a full drop, sustained high energy, a short build and a bigger lift near the end, "
	"ending with a clean hit and short tail.")


def main():
	ap = argparse.ArgumentParser()
	ap.add_argument("mode", choices=["prompt", "plan"])
	ap.add_argument("--root", default=os.environ.get("PROJECT_ROOT", os.getcwd()))
	ap.add_argument("--prompt", help="music prompt (default: an energetic launch-ad prompt at --bpm)")
	ap.add_argument("--bpm", type=float, default=144)
	ap.add_argument("--length", type=float, default=30, help="seconds")
	ap.add_argument("--out", help="output mp3 (default <root>/remake/audio/work/el_music_<mode>.mp3)")
	ap.add_argument("--dry", action="store_true", help="print what would be sent and stop (no credits used)")
	a = ap.parse_args()
	out = a.out or os.path.join(a.root, "remake", "audio", "work", f"el_music_{a.mode}.mp3")
	if a.mode == "plan":
		body = {"composition_plan": PLAN, "model_id": "music_v1"}
	else:
		body = {"prompt": a.prompt or DEFAULT_PROMPT.format(bpm=int(a.bpm)), "music_length_ms": int(a.length * 1000), "model_id": "music_v1"}
	if a.dry:
		secs = sum(x["duration_ms"] for x in PLAN["sections"]) / 1000 if a.mode == "plan" else a.length
		print(f"DRY: {a.mode}, {secs:.1f} s of music -> {out}. This costs credits; run without --dry after a yes.")
		return
	os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
	r = urllib.request.Request("https://api.elevenlabs.io/v1/music?output_format=mp3_44100_192", data=json.dumps(body).encode(),
		headers={"xi-api-key": api_key(a.root), "Content-Type": "application/json"})
	try:
		d = urllib.request.urlopen(r, timeout=600).read()
		open(out, "wb").write(d)
		print("ok", out, len(d))
	except urllib.error.HTTPError as e:
		print("HTTP", e.code, e.read()[:600].decode(errors="replace"))


if __name__ == "__main__":
	main()
