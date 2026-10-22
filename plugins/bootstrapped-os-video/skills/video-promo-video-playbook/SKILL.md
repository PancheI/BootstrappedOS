---
name: video-promo-video-playbook
description: Advanced, studio-grade entry point (first-timers start with launch-video) for an original product promo, launch or explainer film of about 30 seconds that borrows the measured timing of films you like (check each platform's terms first). Use for "promo for my product", "new launch film", "a video with the feel of <brand>'s". The end-to-end playbook - intake, story lock, motion system, reference analysis, build, audio, verification, delivery - and which sub-skill to load at each step.
---

# Promo video playbook (entry point)

A great promo borrows a proven reference's **craft by measurement** and puts **your own story** on top. Films fail when the story is improvised or the motion is eyeballed. The founder approves the story, the motion system and every cut; the agent measures, builds and checks. Advanced and optional. Module rules (length, references and terms, measured motion, brand, paid generation): [RULES.md](../../RULES.md).

## Core rules
- **Plan the motion system first.** No build or rebuild before the `video-motion-system-storyboard` gate is approved. Coherence = one small grammar repeated. Replacing beats one by one with different donors produces a film that feels glued together.
- **The lead owns the film.** Build the shared style kit (canvas, type, card, accent, real logo) and art-direct and edit every beat yourself. Use helper agents only for measurement, research or seams, never for a beat's look. Per-beat delegation produces mixed styles, fake logos and fake UI. Parallel build agents (below, and in the remake and reel skills) are allowed only AFTER the lead has locked the style kit and the motion system: they assemble frames from that kit and the measured tracks, and the lead reviews and re-edits every group before it counts.
- **Real brand only.** Use the real icon file plus the brand font from `knowledge/brand/brief.md` in a horizontal lockup. Never rebuild, redraw, pixelate or restack the logo; a borrowed reveal move may MASK the real lockup. Product moments use REAL product screenshots, with third-party logos and off-brand lines masked.
- **One thing per frame.** Keep the pace; cut density instead. One hero element plus ≤ 6 words per moment; no side HUDs, tickers, extra cards or labels. Audit the densest frame of every beat.
- **One look.** A multi-reference film needs ONE style bible (background world, one type scale with a single accent treatment, one card/glow style), written before the build. Borrow motion and element SHAPES per beat, never a reference's whole palette or stage. Check the whole-film contact sheet for consistency.
- **Measure motion, don't invent it** (the author's rule, [RULES.md](../../RULES.md)). Every card, chip, toggle and transition is recreated from a real reference frame, or is your real product UI; only copy, numbers, colours, font and faces are yours.
- **Motion audit before every render** (the author's rule, not a universal one; `spring(` and `interpolate(` are standard Remotion): `grep -nE "E\.(expo|out|in|outBack|inOut|cubic)|spring\(|interpolate\(" src/**/*.tsx`. Every hit is replaced by measured kf/samples or listed as a declared exception. Re-audit old shots too. Also hunt hand-made motion in other forms: clock-driven fades (`opacity: clamp01((F-a)/n)`), lerps driven straight by the frame, hand power curves, hand parallax ratios, crossfades no reference has. When a move is questioned, show proof: a strip of reference frames over yours at matching times.
- **Easy to watch:** one focal point near the centre; headlines ≥ 96 px (hero words 140–220 px), key numbers ≥ 160 px, UI zoomed so the element the VO names fills ≥ 50 % of the width and its text ≥ 28 px; never crop words while typing; a visible change every ≤ 0.7 s; no near-empty frames longer than ~6 frames; guide the eye with MEASURED punch-ins or select-box snaps; headline and UI never compete. Check with a 3 fps contact sheet of the first 13 s and a 1.5 fps sheet of the rest before showing.
- **Show, don't type.** The VO says the words; the screen SHOWS the idea with UI and objects in measured motion. No text-only scenes; captions ≤ ~4 words and secondary; only key words (numbers, the product name) go big.
- **Pacing budget** (measure with `pacing.py`): ≤ 12 hard cuts/min, ≤ 2 per 5 s, no shot < 0.7 s, whips ≥ 0.4 s; prefer smooth measured push-ins over hard punch cuts. Stacking each beat's fastest donor rhythm can double the cut rate, so check the WHOLE film's rhythm.
- **Quality gate "feels like the reference"** (`filmfeel.py`): match the quality reference's cuts/min, still %, longest still (≤ 1 s), motion energy and jerk, with a camera that never stops and glides between elements. A multi-source film fails this by default, so gate every beat on it.

Scripts live in `${CLAUDE_PLUGIN_ROOT}/skills/video-reference-video-analysis/scripts/` (pacing.py, filmfeel.py, motion_sync.py, originality.py).

## 0. Intake (ask once, in one message)
1. **Reference video(s):** one to three links or files whose timing you measure (check each platform's terms first). With several, ask which beats the user liked in each ("the hook from A, the data reveal from B"). With none, pick together via `video-reference-scout`; never invent a style.
2. **Story / product:** the founder's pain, the arc, the product. Write the story rules in a short `STORY.md` in the project (arc, banned words and brands, claims to avoid, currency, tone) and check every cut against it.
3. **Deliverables:** length (about 30 s; 60 s only for a walkthrough), 16:9 / 1:1 / 9:16, platforms (X, LinkedIn, site).
4. **Voice:** an ElevenLabs voice id (`ELEVENLABS_VOICE_ID`, "<your voice id>") on `eleven_v3`. **Music:** the reference's tempo feel.

**Reel / Short / TikTok / "15 seconds"?** Load **`video-short-form-reel`** as well: hook in 1 s, works muted, vertical recomposition, loop.

**No references given?** Load **`video-reference-scout`**. It finds 8–15 candidates, scores them against a style profile learned from videos the user liked, checks the contact sheets by eye, and proposes a spine plus donors for approval.

**Several references?** Use the multi-reference mode in `video-frame-locked-remake`. One SPINE owns the look and tempo; the others lend whole beats; the user approves a beat-picking table.

**Originality is the goal, not a remake.** Use references for grammar, cap each at 25 % of runtime, pick a different influence per beat, and check with `originality.py` (every beat < 45). See "Originality first" in `video-frame-locked-remake`.

## 1. Lock the story BEFORE building
- Map every reference beat to YOUR story in a plain-words table (seconds / on screen / voice) and get a yes.
- Ask whether each beat fits. Literal ports fail: a reference's DMs might need to become your launch post; a number on screen needs a visible cause.
- Write the copy in customers' real words (their actual excuses and complaints, e.g. "I don't have time", "I don't know where to start"), never a feature list. A list of capabilities read over UI cards does not move anyone.
- A top-of-funnel film shows benefits only: no code, API names, internal or preview details on screen, and never a line the product doesn't actually do.
- If the user questions the problem ("is it real?"), spawn a research agent and present the findings as options. The user decides on bold claims.

## 1b. Motion system + storyboard gate (MANDATORY)
Load **`video-motion-system-storyboard`**. One spine owns the grammar (camera, transitions, easing, rhythm, type slot, card kit); other references lend hero moments re-expressed in it. Show the founder the Motion Design System and per-beat storyboard and get a yes BEFORE any code.

## 2. Measure the reference
Load **`video-reference-video-analysis`**.
- Download it, extract all frames, detect cuts and whips.
- Get colours, font, grid, Whisper word timings and music tempo per band.
- Write SPEC.md.

## 3. Build
Load **`video-frame-locked-remake`**. Build in Remotion only (every frame a pure function of the frame number).
- The lead builds the engine (core.tsx, router with STRETCHES, RemakeLocked, compare tools).
- Up to 4 background agents build contiguous frame groups from the locked style kit, plus 1 AUDIO agent; the lead reviews every group.
- Every group measures and runs the compare loop, keeping its copy in a `<G>_COPY` block.
- Real screenshots beat skeletons; check every crop against your banned list. Use AI-generated portraits of people who do not exist, not initials, when you have them.
- Give focus beats time: a whole-beat stretch plus a still hold for anything the viewer must read.
- Keep all copy (names, prices, numbers, audience) in one data object the scenes read. A version for a new audience is then a new copy preset, not new scenes.

## 4. Audio
Load **`video-film-audio-elevenlabs`**, and **read "Cost discipline" first**.
- Lock the script, then make one base take.
- Change individual lines with `el_tts.py patch`; 1 take by default.
- Generate music once at the reference tempo (snare/hat band), then re-cut it locally.
- Mix to −14 LUFS.

## 5. Verify (every render, before the user sees it)
- **Frame count:** it matches the target.
- **Jump scan:** no pops, including the edges of holds.
- **Motion:** `motion_sync.py` windows plus REF|OURS strips. Motion must FEEL like the reference.
- **Checklist:** run your `STORY.md` checklist (story beats, cause of every number, currency, other brands, faces, claims, stale mix).
- **Independent reviewer:** before the user sees any cut, someone (or an agent) with no part in the build watches the whole film plus the transcript and tries to FAIL it with a numbered defect list: voice/picture contradictions (a name or "he/she" against the face shown), frozen stretches over ~0.8 s, near-empty frames, text walls. Judging from a few stills misses all of these. Fix and re-run until it passes.
- **Recurring render bugs:** a wordmark or lockup clipped at the frame edge (measure text width against the frame; centre the lockup as one group); mask reveals clipping descenders (pad the mask bottom ≥ 0.26 em); hand-offs that flicker or double (swap on one frame at the identical position).
- **Mix timestamp:** `stat` the mix before and after the render; remux if it changed.

## 6. Deliver
- Only the user's video, never the internal sync check.
- Export the 1080p60 master, the 1080p30 web version, and `*-x.mp4` for X (H.264 High, 30 fps, ≤ ~25 MB).
- Describe changes to the user in seconds and plain words.

## 7. Learn
After every project, update the project's `STORY.md` with new story rules, and note new techniques next to the matching sub-skill's scripts.

## Kickoff prompt the user can paste
> Make a ~30 s promo for <product> (60 s only if it's a website walkthrough). References: <link A> (spine: overall style), <link B> (I like its hook at 0:05–0:12), <link C> (its pricing reveal). Story: <founder pain → product → outcome>. Use video-promo-video-playbook. Show me the beat table first, then build. Deliverables: 16:9 master + X version.

## Requirements
- ffmpeg and ffprobe
- yt-dlp
- python3 with numpy, scipy, pillow and soundfile (plus openai-whisper for word timings; librosa is optional, used by `music_beats.py` if installed)
- Node 22 and a Remotion project (`npx create-video@latest`)
- An ElevenLabs API key with TTS + Music access in `ELEVENLABS_API_KEY` (env or the project's `.env`), and `ELEVENLABS_VOICE_ID`

## Never
- Build before the story and the motion system are approved.
- Deliver the internal sync check.
- Publish anything. Gates: `shared/gates.md` (core).

## Shared knowledge
**Read first:** `knowledge/brand/brief.md`, `knowledge/positioning.md`, the project's `STORY.md`. **Write after:** one dated line in `knowledge/log/<date>.md`. Paths from `shared/knowledge-tree.md` (core).

## Bootstrapped core
Ask `recipes` (area `video`) at intake and `lessons` (theme `video`) before the build. If it isn't connected, carry on with this method.
