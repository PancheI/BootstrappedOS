#!/usr/bin/env python3
"""Film VO: your script lines as ONE continuous ElevenLabs eleven_v3 take, cut per line
at the character timestamps, then each line fitted (≤8 % atempo) and placed at its slot.

Writes <AUDIO_DIR>/work/vo/<id>.wav (cut lines), work/vo_track.wav (48 kHz mono, full
film length) and <AUDIO_DIR>/SLOTS.md.  API responses are cached in work/takes/;
pass --takes=N to ask for more takes of the current text.

Paying for a take needs --go. Without it, the script prints how many characters it would send and stops,
so you can show the cost and get a yes first.

Run from the project root: python3 <skill>/scripts/make-vo.py [--takes=N] [--go]
Env: ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID (environment or <project>/.env; never printed).
Optional: PROJECT_ROOT (default: cwd), AUDIO_DIR (default: <root>/remake/audio).

Edit the CONFIG block below (lines, slots, nudges) for your film. The values are an EXAMPLE.
"""
import base64, json, os, re, subprocess, sys, urllib.request
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.environ.get("PROJECT_ROOT", os.getcwd())
AUDIO = os.environ.get("AUDIO_DIR", os.path.join(ROOT, "remake", "audio"))
WORK = os.path.join(AUDIO, "work")
SR = 48000
sys.path.insert(0, HERE)
from timeline import FILM, film_t  # REF → film time (holds, speed-ups, cuts)

# ---------------- CONFIG (example) ----------------
MAX_STRETCH = 1.08
EARLY = 0.35  # a line may start this much before its slot when it cannot fit otherwise
GAP = 0.25  # minimum breath between lines
# per-line nudges (s) so a key word lands on its picture hit (check with Whisper word times), e.g. {"06": 0.40}
SHIFT = {}
# place a line so its LAST phrase starts at a film time, e.g. {"01": round(film_t(2.20), 3)} for a word on a click
ANCHOR = {}
PAUSE_MAX = {}  # cap pauses inside a line (s), e.g. {"01": 0.20}
# keep an earlier full take for every line except the reworded ones ("" = use the best current take whole)
BASE = ""
NEW = "best"  # = the best-fitting take of the current text
# line: take file (full-context) or el_tts.py patch file it comes from, e.g. {"05": "patch_05.json"}
REWORDED = {}
SAY = {"YourProduct": "Your Product", "SaaS": "sass"}  # pronunciation fixes (on-screen word: spoken form)

# (id, slot start, slot end, [v3 tag], text) in REF seconds, mapped to film time below.
REF_LINES = [  # a neutral 30 s example (see timeline.py); write your own story here
	("01", 0.60, 3.00, "[tired]", "I launched last week... and nobody signed up."),
	("02", 3.40, 5.00, "[honest]", "I didn't know why."),
	("03", 10.00, 14.00, "", "YourProduct reads your page and shows what stops people from paying."),
	("04", 14.50, 19.50, "", "Fix one thing a day, and watch the sign-ups come in."),
	("05", 27.00, 31.50, "", "More customers from the visitors you already have."),
	("06", 32.00, 34.80, "[warm, inviting]", "Try YourProduct today."),
]
FILM_SLOT = {}  # override a line's slot in FILM seconds, e.g. {"02": (3.40, 5.80)}
LINES = [(i, *FILM_SLOT.get(i, (film_t(a), film_t(b))), tag, text) for i, a, b, tag, text in REF_LINES]
# ---------------------------------------------------


def _env(name):
	v = os.environ.get(name)
	p = os.path.join(ROOT, ".env")
	if not v and os.path.exists(p):
		for line in open(p):
			if line.startswith(name + "="):
				v = line.split("=", 1)[1].strip().strip("'\"")
	return v


def key():
	k = _env("ELEVENLABS_API_KEY")
	if not k:
		sys.exit("ELEVENLABS_API_KEY missing (env or .env)")
	return k


def voice():
	v = _env("ELEVENLABS_VOICE_ID")
	if not v:
		sys.exit("ELEVENLABS_VOICE_ID missing (env or .env): set it to <your voice id>")
	return v


def spoken(t):
	for a, b in SAY.items():
		t = t.replace(a, b)
	return t


def build_text():
	full, spans = "", []
	for _, _, _, tag, text in LINES:
		if full:
			full += " "
		if tag:
			full += tag + " "
		body = spoken(text)
		spans.append((len(full), len(full) + len(body)))
		full += body
	return full, spans


def takes(full):
	"""All cached takes of this exact text; --takes=N pays for more until N exist."""
	d = os.path.join(WORK, "takes")
	os.makedirs(d, exist_ok=True)
	have = []
	for fn in sorted(os.listdir(d)):
		r = json.load(open(os.path.join(d, fn)))
		if r.get("text") == full:
			have.append((fn, r))
	want = max([int(a.split("=")[1]) for a in sys.argv if a.startswith("--takes=")] + [1])
	if len(have) < want and "--go" not in sys.argv:
		n = want - len(have)
		sys.exit(f"{n} new take(s) needed: {n * len(full)} characters on eleven_v3. Re-run with --go after a yes.")
	while len(have) < want:
		body = {"text": full, "model_id": "eleven_v3", "voice_settings": {"stability": 0.5, "similarity_boost": 0.8}}
		req = urllib.request.Request(
			f"https://api.elevenlabs.io/v1/text-to-speech/{voice()}/with-timestamps?output_format=mp3_44100_128",
			data=json.dumps(body).encode(), headers={"xi-api-key": key(), "Content-Type": "application/json"})
		r = json.load(urllib.request.urlopen(req, timeout=300))
		r["text"] = full
		fn = f"take_{len(os.listdir(d)):02d}.json"
		json.dump(r, open(os.path.join(d, fn), "w"))
		have.append((fn, r))
	return have


def cut_lines(r, spans):
	"""Decode a take and cut it into trimmed per-line clips."""
	al = r["alignment"]
	assert len(al["characters"]) == len(r["text"])
	mp3 = os.path.join(WORK, "tmp_take.mp3")
	open(mp3, "wb").write(base64.b64decode(r["audio_base64"]))
	x = decode(mp3)
	st, en = al["character_start_times_seconds"], al["character_end_times_seconds"]
	# v3 timestamps drift a little, so cut in a silent stretch around each line boundary
	cuts = [0.0] + [quiet_cut(x, en[spans[i - 1][1] - 1], st[spans[i][0]]) for i in range(1, len(spans))] + [len(x) / SR]
	return [trim(x[int(cuts[i] * SR):int(cuts[i + 1] * SR)]) for i in range(len(spans))]


def cut_present(r):
	"""{line id: clip} for the lines whose current text appears in a take (a patch or an older full take).
	Text in the take that is not a current line (old wordings) still counts as a boundary, sentence by sentence,
	so a kept line never swallows the old line next to it."""
	text = r["text"]
	ids, spans, pos = [], [], 0
	for lid, _, _, _, body in LINES:
		i = text.find(spoken(body), pos)
		if i >= 0:
			ids.append(lid)
			spans.append((i, i + len(spoken(body))))
			pos = spans[-1][1]
	extra = []
	for m in re.finditer(r"[^\[\]\s][^\[\]]*?[.?!](?=\s|$)", text):  # sentences outside tags
		a, b = m.start(), m.end()
		if not any(a < e and b > s0 for s0, e in spans):
			extra.append((a, b))
	allsp = sorted([(sp, lid) for sp, lid in zip(spans, ids)] + [(sp, None) for sp in extra])
	clips = cut_lines(r, [sp for sp, _ in allsp])
	return {lid: c for (sp, lid), c in zip(allsp, clips) if lid}


def spans_in(text):
	"""Where each current line sits in a take's text. A line that was reworded after the take
	(so its text is absent) gets the stretch between its neighbours."""
	spans, pos = [], 0
	for _, _, _, tag, body in LINES:
		i = text.find(spoken(body), pos)
		spans.append(None if i < 0 else (i, i + len(spoken(body))))
		if i >= 0:
			pos = i + len(spoken(body))
	k = 0
	while k < len(spans):  # a run of reworded lines gets the stretch between its found neighbours
		if spans[k] is not None:
			k += 1
			continue
		j = k
		while j < len(spans) and spans[j] is None:
			j += 1
		a = spans[k - 1][1] + 1 if k else 0
		tag = LINES[j][3] if j < len(spans) else ""
		b = (spans[j][0] - (len(tag) + 1 if tag else 0) - 1) if j < len(spans) else len(text)
		if text[a:a + 1] == "[":
			a = text.index("]", a) + 2
		spans[k] = (a, b)
		for m in range(k + 1, j):
			spans[m] = (b, b)
		k = j
	return spans


def speech_db(clip):
	w = int(0.02 * SR)
	n = len(clip) // w
	fr = np.sqrt((clip[:n * w].reshape(n, w) ** 2).mean(1))
	return 20 * np.log10(np.sqrt((fr[fr > 10 ** (-40 / 20)] ** 2).mean()) + 1e-9)


def overrun(clips, only=None):
	"""How far past the 8 % cap the take is, summed over lines (0 = every line fits)."""
	return sum(max(0.0, len(c) / SR / (s1 - s0) - MAX_STRETCH) for c, (lid, s0, s1, _, _) in zip(clips, LINES) if only is None or lid in only)


def decode(path, af=None):
	cmd = ["ffmpeg", "-v", "error", "-i", path] + (["-af", af] if af else []) + ["-ac", "1", "-ar", str(SR), "-f", "f32le", "-"]
	return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).copy()


def write_wav(path, x, ch=1):
	subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", str(ch), "-i", "-", "-c:a", "pcm_f32le", path],
		input=np.ascontiguousarray(x, np.float32).tobytes(), check=True)


def trim(x, thr_db=-42, pad=0.02):
	"""Drop leading/trailing silence (20 ms RMS below thr), keep a small pad."""
	w = int(0.01 * SR)
	n = len(x) // w
	rms = 20 * np.log10(np.sqrt((x[:n * w].reshape(n, w) ** 2).mean(1)) + 1e-9)
	on = np.where(rms > thr_db)[0]
	if len(on) == 0:
		return np.zeros(int(0.05 * SR), np.float32)
	a = max(0, on[0] * w - int(pad * SR))
	b = min(len(x), (on[-1] + 1) * w + int(pad * SR * 3))
	y = x[a:b].copy()
	f = int(0.006 * SR)
	y[:f] *= np.linspace(0, 1, f)
	y[-f:] *= np.linspace(1, 0, f)
	return y


def quiet_cut(x, e_prev, s_next):
	"""Cut point between two lines: the silent run (<-50 dBFS, >=30 ms) nearest the midpoint of
	the previous line's last char end and the next line's first char start."""
	w = int(0.01 * SR)
	a, b = e_prev - 0.25, s_next + 0.45
	seg = x[int(a * SR):int(b * SR)]
	n = len(seg) // w
	q = list(20 * np.log10(np.sqrt((seg[:n * w].reshape(n, w) ** 2).mean(1)) + 1e-9) < -50) + [False]
	runs, k0 = [], None
	for k, v in enumerate(q):
		if v and k0 is None:
			k0 = k
		if not v and k0 is not None:
			if k - k0 >= 3:
				runs.append(a + (k0 + k) / 2 * w / SR)
			k0 = None
	mid = (e_prev + s_next) / 2
	if not runs:  # no silence: quietest frame
		k = int(np.argmin([np.abs(seg[j * w:(j + 1) * w]).mean() for j in range(n)]))
		return a + (k + 0.5) * w / SR
	return min(runs, key=lambda c: abs(c - mid))


def cap_pauses(x, longest):
	"""Shorten silences inside a line (<-45 dBFS, 10 ms frames) to at most `longest` s."""
	w = int(0.01 * SR)
	n = len(x) // w
	quiet = 20 * np.log10(np.sqrt((x[:n * w].reshape(n, w) ** 2).mean(1)) + 1e-9) < -45
	keep, k = np.ones(len(x), bool), 0
	while k < n:
		if quiet[k]:
			j = k
			while j < n and quiet[j]:
				j += 1
			if 0 < k and j < n and (j - k) * w > longest * SR:
				mid = (k + j) // 2 * w
				cut = (j - k) * w - int(longest * SR)
				keep[mid - cut // 2:mid - cut // 2 + cut] = False
			k = j
		else:
			k += 1
	return x[keep]


def last_phrase_onset(x):
	"""Seconds from the clip start to the onset of its last phrase (after its last pause ≥ 150 ms)."""
	w = int(0.01 * SR)
	n = len(x) // w
	loud = 20 * np.log10(np.sqrt((x[:n * w].reshape(n, w) ** 2).mean(1)) + 1e-9) > -40
	run, last = 0, 0
	for k in range(n):
		if not loud[k]:
			run += 1
		else:
			if run >= 15:
				last = k
			run = 0
	return last * w / SR


def atempo(x, r):
	if abs(r - 1) < 1e-3:
		return x
	tmp = os.path.join(WORK, "tmp_at.wav")
	write_wav(tmp, x)
	return decode(tmp, f"atempo={r:.4f}")


def main():
	os.makedirs(os.path.join(WORK, "vo"), exist_ok=True)
	os.makedirs(os.path.join(WORK, "takes"), exist_ok=True)
	full, spans = build_text()
	need_new = NEW in REWORDED.values() or not BASE
	if need_new:
		takes(full)  # full-script takes of the current text (paid); skipped when every reworded line comes from a patch
	d = os.path.join(WORK, "takes")
	all_takes = {fn: json.load(open(os.path.join(d, fn))) for fn in sorted(os.listdir(d))}
	# el_tts.py patch outputs (short [prev + new + next] context takes) behave like takes of the text they sent
	pd = os.path.join(WORK, "patches")
	for fn in sorted(os.listdir(pd)) if os.path.isdir(pd) else []:
		j = json.load(open(os.path.join(pd, fn)))
		all_takes[fn] = dict(j["take"], text=j["sent"])
	best, clips = BASE, None
	if need_new:
		current = {fn: r for fn, r in all_takes.items() if r["text"] == full}
		cands = [(fn, cut_lines(r, spans)) for fn, r in current.items()]
		for fn, clips in cands:
			print(f"{fn}: overrun score {overrun(clips):.3f}, new lines {overrun(clips, [l for l, f in REWORDED.items() if f == NEW]):.3f}")
		only = [lid for lid, fn in REWORDED.items() if fn == NEW] if BASE else None  # judge takes on the lines we take from them
		best, clips = min(cands, key=lambda c: overrun(c[1], only))
	if BASE:  # an earlier take whose other lines we keep; each reworded line comes from its donor take
		base = cut_lines(all_takes[BASE], spans_in(all_takes[BASE]["text"]))
		keep = [lid for lid, *_ in LINES if lid not in REWORDED]
		ref = np.mean([speech_db(c) for c, (lid, *_ ) in zip(base, LINES) if lid in keep])
		clips, notes = list(base), []
		idx = {l: k for k, (l, *_ ) in enumerate(LINES)}
		for lid, fn in REWORDED.items():
			fn = best if fn == NEW else fn
			don = cut_present(all_takes[fn])
			# level: match the donor to the base on the lines both share (a patch's context lines), else overall
			shared = [l for l in don if l in keep]
			lvl = (np.mean([speech_db(base[idx[l]]) for l in shared]) - np.mean([speech_db(don[l]) for l in shared])) if shared \
				else ref - np.mean([speech_db(c) for c in don.values()])
			clips[idx[lid]] = don[lid] * 10 ** (lvl / 20)
			notes.append(f"line {lid} from {fn} ({lvl:+.1f} dB)")
		best = f"{BASE}, with {'; '.join(notes)}, level-matched to {BASE}"
	print("using", best)

	track = np.zeros(int(round(FILM * SR)), np.float32)
	rows, prev_end = [], -1.0
	for i, ((lid, s0, s1, _, text), clip) in enumerate(zip(LINES, clips)):
		if lid in PAUSE_MAX:
			clip = cap_pauses(clip, PAUSE_MAX[lid])
		nat = len(clip) / SR
		if lid in ANCHOR:  # the last word lands on a picture beat; speed up (≤8 %) only to clear the previous line
			on = last_phrase_onset(clip)
			r_ = 1.0
			while ANCHOR[lid] - on / r_ < prev_end + 0.12 and r_ < MAX_STRETCH:
				r_ = min(MAX_STRETCH, r_ + 0.005)
			clip = atempo(clip, r_)
			d = len(clip) / SR
			at = ANCHOR[lid] - on / r_
			write_wav(os.path.join(WORK, "vo", f"{lid}.wav"), clip)
			k = int(round(at * SR))
			track[k:k + len(clip)] += clip[:len(track) - k]
			rows.append((lid, s0, s1, text, at, at + d, nat, (r_ - 1) * 100, False, at - (prev_end + 0.12) if at < prev_end + 0.12 else 0))
			prev_end = at + d
			continue
		nxt = LINES[i + 1][1] if i + 1 < len(LINES) else FILM - 0.3
		# fit to the REF slot end with up to 8 % speed-up; if that is not enough, start up to
		# EARLY s sooner (never within GAP of the previous line), then let the rest run past the slot end
		need = nat / (s1 - s0)
		r_ = min(max(need, 1.0), MAX_STRETCH)
		clip = atempo(clip, r_)
		d = len(clip) / SR
		at = s0 + SHIFT.get(lid, 0.0)
		if at + d > s1 and lid not in SHIFT:  # a nudged line keeps its nudge
			at = max(0.0, s0 - EARLY, prev_end + GAP, s1 - d)
		prev_end = at + d
		over = at + d - (nxt - 0.08)
		write_wav(os.path.join(WORK, "vo", f"{lid}.wav"), clip)
		k = int(round(at * SR))
		assert k >= 0, (lid, at, d, s0, s1, prev_end)
		seg = clip[:len(track) - k]
		track[k:k + len(seg)] += seg
		rows.append((lid, s0, s1, text, at, at + d, nat, (r_ - 1) * 100, need > MAX_STRETCH, over))
	write_wav(os.path.join(WORK, "vo_track.wav"), track)

	with open(os.path.join(AUDIO, "SLOTS.md"), "w") as f:
		f.write(f"# VO slots — OURS vs REF\n\nOne continuous eleven_v3 take ({best}), cut per line at silent gaps next to the character-timestamp boundaries, trimmed, placed at its slot start. Slots are in FILM time (timeline.py mirrors the router's STRETCHES/CUTS). Stretch = atempo speed-up applied to fit the slot end (cap 8 %); a line that still does not fit starts up to 0.35 s early (keeping a 0.25 s breath after the previous line) and may end past its slot end. Check the placed track with Whisper word timestamps.\n\n")
		f.write("| line | text | slot (film s) | ours start–end (s) | natural dur (s) | stretch % | note |\n|---|---|---|---|---|---|---|\n")
		for lid, s0, s1, text, a, b, nat, pct, capped, over in rows:
			note = []
			if capped:
				note.append(f"needs {((nat / (s1 - s0)) - 1) * 100:.1f} % — capped at 8 %; starts {a - s0:+.2f} s vs REF, ends {b - s1:+.2f} s vs slot end")
			if lid in ANCHOR:
				note.append(f"placed so its last word starts at {ANCHOR[lid]:.2f} s; internal pauses capped at {PAUSE_MAX.get(lid, 0):.2f} s")
			if SHIFT.get(lid):
				note.append(f"nudged {SHIFT[lid]:+.2f} s so its key word lands on the picture hit")
			if over > 0:
				note.append(f"runs {over:.2f} s into next line")
			f.write(f"| {lid} | {text} | {s0:.2f}–{s1:.2f} | {a:.2f}–{b:.2f} | {nat:.2f} | {pct:+.1f} | {'; '.join(note)} |\n")
	for row in rows:
		lid, s0, s1, text, a, b, nat, pct, capped, over = row
		print(f"{lid:>3} slot {s0:5.2f}-{s1:5.2f}  ours {a:5.2f}-{b:5.2f}  nat {nat:4.2f}  stretch {pct:+4.1f}%  {'CAPPED' if capped else ''} {'OVERLAP %.2f' % over if over > 0 else ''}")


main()
