---
name: video-reference-scout
description: Find, review, measure and rank the best reference video(s) for a video task when the user hasn't given one — search good sources, download low-res candidates, score them with scout.py against a style profile LEARNED from videos the user liked, eye-check contact sheets, and propose a spine + donors for approval. Use when the user asks for a promo/launch/explainer video without references, says "find me references/templates", "what's the best style for this", or before video-promo-video-playbook's build when references are missing.
---

# Reference scout

**Goal:** never guess a style. Pick references by **measurement plus a visual check**, matched to what the user has already liked. Written style notes are not evidence: a film a research agent calls the perfect "spine" from a written breakdown can measure as the worst match for the user's taste. Measure and look. The founder approves the picks; the agent finds, scores and proposes. Advanced and optional. Module rules (length, references and terms, measured motion, brand, paid generation): [RULES.md](../../RULES.md).

Script: `${CLAUDE_PLUGIN_ROOT}/skills/video-reference-scout/scripts/scout.py` (below: `scout.py`). It writes into `./scout/` in the current directory (`SCOUT_DIR` overrides it).

## 1. Define the target style
- **Learn a profile from videos the user liked (preferred):**
  ```
  python3 scout.py calibrate <name> liked1.mp4 liked2.mp4
  ```
  Profiles are saved to `scripts/profiles.json` and reused. The shipped `profiles.json` holds only an `example` profile showing the structure (`metric: [target, tolerance, weight]`); your real profiles are learned from your own liked videos.
- **Built-in hand profiles** (less reliable than learned ones): `launch` (continuous camera, UI-driven, kinetic type, fast bright music, about 30 s), `linear` (calm, engineered drifts), `punchy` (hard-cut social slams).
- **Match the task:** a fast social cut suits `punchy`; a 30 s launch film suits `launch` or a learned profile. A longer reference can still be a good pacing spine; ignore the length term then.
- **Sanity check:** a liked video must score ~100 against its own learned profile. Hand-written targets score far lower, which is why profiles are learned.

## 2. Gather 8–15 candidates (only if the user gave none)
Sources, best first (the same list is in `video-reference-video-analysis` §0):
1. Curated launch-video libraries (e.g. https://impractical.ai/launch-videos), filtered by the task's category.
2. Official "Introducing X" uploads on company YouTube channels.
3. The brand's X account on launch day (`"introducing" filter:videos from:<brand>`).
4. Studio reels you can download normally.
5. Motion-design studio portfolios: studio work is often a step above in-house launch films. Credits are often missing because the client uploads the film, so search studio portfolios directly.

Prefer the same domain as the task, a similar length, and recent work. Use WebSearch/WebFetch to find fresh ones. Check each platform's terms before downloading; never work around a login or block.

## 3. Fetch low-res and score (all local; no API cost)
```
python3 scout.py fetch <url|file> ...
python3 scout.py score scout/*.mp4 --profile <name>
```
- `fetch` grabs 480p copies, with automatic format fallbacks when YouTube returns a 403.
- `score` writes `scout/report.md`, ranked, plus a 1 fps `<id>_sheet.jpg` per video.

| Metric | Meaning |
|---|---|
| `cuts_pm` | hard cuts per minute (whips count too) |
| `energy` | how alive each frame is |
| `still_frac` | share of dead frames |
| `cam_cont` | how much of the motion is smooth continuous camera |
| `ui_frac` | how much looks like product UI; works on light AND dark UIs |
| `text_kin` | kinetic word-reveal bursts |
| `bpm`, `bright` | music tempo on the snare/hat band, and brightness |

These are proxies. They rank well, but they don't judge taste. The score caps at 30 when `ui_frac` < 0.3 (stock footage, talking heads, slides).

## 4. Eye-check the top 5 (mandatory)
Read each `<id>_sheet.jpg`. For each, note:
- the camera grammar (continuous or cut);
- canvas (light or dark);
- type style (centred kinetic, word slams, captions);
- UI treatment (flat, tilted plane, 3D);
- the 2–3 best beats with timestamps.

Drop anything the numbers liked but the eye doesn't: slideshow explainers, stock footage, talking heads.

## 4b. Content-aware beat matching (the step that matters most)
Style score picks a SPINE; content decides the DONORS.
1. Write YOUR beat list first (B1…Bn), in the same words as the story table: e.g. launch post, notification swarm plus counter, zero-state dashboard, comment focus hold, problem type over data, logo sting, URL input plus AI working, ranked list, checkout/pay, big-number slam, feature chips, CTA plus cursor click.
2. From every contact sheet, tag which of those beats the video contains, with timestamps and a craft rating from 1 to 5.
3. Build a matrix: rows = your beats, cells = the best 1–2 candidate moments (video, timestamps, craft, why). Spine = the best style score AND the most beats covered. Donors = the best moment for each beat the spine lacks or does weakly.
4. **Sanity-check every search hit.** Searches sometimes return the wrong video entirely.
5. Some categories (e.g. payments infrastructure) have few short launch films, mostly keynotes. Look at adjacent categories with similar UI beats.

## 5. Propose to the user (one message, then wait)

| role | video (link) | score | what we take from it (with timestamps) |
|---|---|---|---|
| spine | … | … | overall look, camera, tempo |
| donor A | … | … | a specific beat, e.g. the "punch-in on the changing value" at 0:23–0:27 |
| donor B | … | … | … |

Add one line on why each lost the others, and a one-line style summary. Then continue with `video-promo-video-playbook` (multi-reference mode in `video-frame-locked-remake`).

## 5b. Originality mode (default)
Pick one spine for the SYSTEM (camera, rhythm, type, card kit; see `video-motion-system-storyboard`), never to copy. For each beat's hero moment, pick the best reference from a different source and re-express it in the spine's grammar, with no reference above 25 % of runtime. Prefer references whose looks differ from each other, so the mix reads as your own style. Keep the user's favourite film only as the pacing spine.

## 6. Learn
- **User likes or dislikes a pick:** re-calibrate the profile including (or excluding) that video.
- **The metric ranking disagreed with your eye:** trust the eye for the pick, and note the case for the next calibration.
- `ui_frac` must count dark UIs as well as light ones.

## Download and disk gotchas
- "Connection reset by peer" on the video stream: force IPv4 with `yt-dlp -4 …`, and keep yt-dlp current.
- Delete old frame dumps and render bundles; they fill disks fast.

## Requirements
- ffmpeg/ffprobe, yt-dlp, python3 with numpy and pillow

## Never
- Pick a reference from a written description alone; measure and look.
- Download against a platform's terms.
- Publish anything. Gates: `shared/gates.md` (core).

## Shared knowledge
**Read first:** `knowledge/brand/brief.md`, the project's `STORY.md`. **Write after:** one dated line in `knowledge/log/<date>.md`. Paths from `shared/knowledge-tree.md` (core).

## Bootstrapped core
Ask `lessons` (theme `video`) before step 1. If it isn't connected, carry on with this method.
