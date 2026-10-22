---
name: video-reference-video-analysis
description: Get a reference video (Vimeo/YouTube/X/local; check the platform's terms first) and measure its timing for an original film — download, frames, labelled contact sheets, cut/whip detection, colour tokens, font sizes, grid, Whisper word timings, music tempo per band; plus Remotion compare/sync/sheet tools for REF-vs-ours checks and film-level gates (pacing, filmfeel, motion sync, originality). Use when the user says "like this video", "check <brand>'s video", "analyze the reference", or before any remake.
---

# Reference video analysis

Measure a reference so its timing can be matched, never its assets. Advanced and optional. Module rules (length, references and terms, measured motion, brand, paid generation): [RULES.md](../../RULES.md).

Scripts: `${CLAUDE_PLUGIN_ROOT}/skills/video-reference-video-analysis/scripts/`. Run them from your project root (or set `PROJECT_ROOT`); outputs go to `<project>/remake/ref/` by default (`REF_DIR` overrides it).

## 0. Where to find great references
1. **Curated launch-video libraries** (e.g. https://impractical.ai/launch-videos), filterable by category (Devtools / AI / SaaS / Fintech), with style notes and official uploads.
2. **Official company YouTube channels** (the "Introducing X" uploads). Highest bitrate, up to 4K/60: `yt-dlp -f "bv*[fps>=50]+ba/bv*+ba" <url>`.
3. **The brand's X account on launch day:** `"introducing" filter:videos from:<brand>`. Often a square cut too.
4. **Vimeo:** studio and freelance reels, where the creator allows download.
5. **Motion-design studios' portfolios** are often a step above in-house launch films.
6. Jitter community: single moves only. Dribbble/Behance: low hit rate. Reddit: almost nothing useful.

To rank candidates, use `video-reference-scout`. Written style notes overrate calm, "premium" films; measure and look.

## 1. Get the file
- Check the platform's terms first. Then try `yt-dlp -f "bv*+ba/b" --merge-output-format mp4 -o remake/ref/reference.mp4 <url>`.
- **A site won't let you download:** pick a reference you can download normally, or ask the creator. Never work around logins, paywalls or captchas.


## 2. Frames and overview
```
ffmpeg -i remake/ref/reference.mp4 -start_number 0 -q:v 3 remake/ref/full/f%04d.jpg
ffmpeg -i remake/ref/reference.mp4 -vn -ac 2 -ar 48000 remake/ref/audio.wav
```
- Contact sheets at 1 fps: label them with PIL (many ffmpeg builds have no `drawtext`).
- **Cuts and whips:** compute per-frame mean-abs-diff on 192×108 gray and save it as `diff.npy`. Spikes against the local median are cuts or whips. Some of the best films have ZERO hard cuts: one continuous camera. Put build-group seams on spikes.

## 3. Measure, don't eyeball (numpy on remake/ref/full)
- **Colours:** sample pixels for bg, flood, text ink (mean of dark pixels) and accents (hue masks).
- **Font:** identify it from crops. Size comes from cap height (e.g. Poppins cap ≈ 0.70 × size).
- **Grid:** use row/col mean profiles for line spacing and phase (e.g. 160 px cells at x = 140 + 160k).
- **Tracks:**
  - per-frame ink bboxes, card rects, cursor tip, camera scale (from grid spacing);
  - particle and flame masks (e.g. a hue mask per frame, then a polar resample → track JSON);
  - perspective: fit corners, and only use matrix3d if a flat fit fails.
- **Palette swaps preserve LIGHTNESS**: pick your colour's alpha by matching luma, not colour density.

## 4. Audio
- **Narration:** `whisper remake/ref/audio.wav --model small --language en --word_timestamps True --output_format json`, then save the JSON as `remake/ref/words.json` (the audio `analyze.py` reads Whisper's format directly). Build the slot table (line, start, end, text) and the wpm (a brisk launch VO is ≈ 144). Whisper misses short sounds like "Oh" or a sigh, so find those in the voice band and pass them to `analyze.py --voice-extra`.
- **Music:** tempo per band (kick / snare / hats), phase, and brightness. See `video-film-audio-elevenlabs`. Loudness per second, drop and hit times, hard stop.
- **SFX:** onset times from spectral flux (top 1 %).

## 5. Motion sync (does it FEEL like the reference?)
`python3 scripts/motion_sync.py <ref_frames> <our_frames> --f0 N --win 20` gives, per window, REF vs OURS motion energy, camera velocity (phase correlation) and vector error.
- **Ours ≈ 0 energy while REF is 1–3:** a frozen stretch. REF never stops (card drift, camera float), so add the measured drift.
- **REF fast, ours ~0:** a missing whip.
- **Ours 2–3× REF:** too violent.
- **A big error one window apart:** a whip on the wrong frames.

Targets: error < 5 px/frame, energy within ±30 %. Render ours on the REF-locked composition, then confirm by eye with REF|OURS strips at 6 fps. Viewers notice unsynced motion before any number does.

## 6. Compare tools (`scripts/`, for Remotion remakes)
These are the only copies of `compare.py`, `render.mjs`, `sheet.py` and `sync.py`; `video-frame-locked-remake` copies them from here into `remake/tools/`.
- `node scripts/render.mjs <OUT> compare <frames>`: one browser, renders frames of the `RemakeLocked` composition (`COMP` overrides it), then a REF | OURS | diff sheet.
  - `full f0 f1` renders a sequence.
  - It resolves `@remotion/bundler` and `@remotion/renderer` through `node_modules/@remotion/cli` (works with pnpm).
- `python3 scripts/sync.py ours.mp4 out.mp4`: REF stacked over ours, frame-locked (internal only; deliver only the user's video).
- `python3 scripts/sheet.py <seqdir> out.jpg`: 1 fps REF | OURS sheet.
- **Jump scan:** ours per-frame diff vs `diff.npy`. Flag `d > 6 and d > 2.5·ref + 3`.

## 7. Film-level gates
- `pacing.py <video> [--list]`: hard cuts, cuts/min, shortest shots.
- `filmfeel.py a.mp4 b.mp4`: cuts/min, still %, longest still, motion energy, jerk — compare yours to the quality reference.
- `originality.py ours.mp4 ref.mp4 --map <dir with timeline.py> [--beats beats.json]`: per-beat copy score (> 60 traced, 35–60 derived, < 35 own work).

With several references, analyse each into `<project>/remake/ref/<A|B|C>/` (`REF=A` selects it in the tools), normalised to one resolution and fps, then make a 1 fps contact sheet for each so the user can point at the beats they like.

Output everything to `<project>/remake/ref/` and write `SPEC.md` (template: `${CLAUDE_PLUGIN_ROOT}/skills/video-frame-locked-remake/templates/SPEC.template.md`): shot table, palette table, copy map, narration table, audio notes. Then follow `video-frame-locked-remake`.

## Download and disk gotchas
- "Connection reset by peer" on the video stream (the page loads fine): force IPv4 with `yt-dlp -4 …`. Keep yt-dlp current; old builds fail on many sites.
- Disk: every Remotion render bundle is several hundred MB. Reuse ONE bundle per agent (`NOBUNDLE=1`) and delete old frame dumps.

## Requirements
- ffmpeg, yt-dlp, python3 with numpy, scipy and pillow, openai-whisper for word timings
- Node 22 and a Remotion project for the compare tools

## Never
- Work around a login, paywall, captcha or download block.
- Deliver the stacked sync check; it's internal.
- Publish anything. Gates: `shared/gates.md` (core).

## Shared knowledge
**Read first:** the project's `STORY.md`. **Write after:** one dated line in `knowledge/log/<date>.md`. Paths from `shared/knowledge-tree.md` (core).

## Bootstrapped core
Ask `lessons` (theme `video`) before step 1. If it isn't connected, carry on with this method.
