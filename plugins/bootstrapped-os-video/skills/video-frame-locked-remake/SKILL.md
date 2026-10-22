---
name: video-frame-locked-remake
description: Build an original film that borrows a reference video's measured timing and pacing, in Remotion, with your own brand and story - measure the reference with numpy, build shots in parallel agent groups, add ElevenLabs voice and music, verify with a stacked sync check. Originality mode is the default (grammar, not frames); multi-reference mode combines the best beats of 2-3 references. Check the platform's terms before downloading any reference. Use for "same feel as this video", "frame-locked", "use this film's timing for my product", or a pasted frame-locked remake prompt.
---

# Frame-locked remake

**What you get:** an original film of about 30 seconds whose timing and pacing are measured from films you like, with your story, brand, real screens, voice and music. The founder approves the story table, the silent cut and the final film; the agent measures, builds and checks. Advanced and optional. Module rules (length, references and terms, measured motion, brand, paid generation): [RULES.md](../../RULES.md).

## Originality first (the default)
Frame-locking to one film produces a trace: a remake of one film typically scores well over half its runtime as "traced" (> 60). The default goal is an ORIGINAL film that borrows grammar, not frames:
1. **Measure:** `python3 "${CLAUDE_PLUGIN_ROOT}/skills/video-reference-video-analysis/scripts/originality.py" ours.mp4 ref.mp4 --map remake/audio --beats beats.json` after every render, against EVERY reference used. Targets: every beat < 45, traced runtime (> 60) under 10 %.
2. **Share cap:** no single reference drives more than 25 % of the runtime. The main reference is only the PACING spine (beat lengths, cut rhythm, VO pace), not the look of individual shots.
3. **A different primary influence per beat,** from several studios, designers and templates. Record it in a table: beat → reference → what we take → how we change it.
4. **Transform by COMBINING, don't trace one source.** Each beat's layout and composition are yours (your story and UI), and its MOTION is measured from a different reference than its neighbours (or from 2 references blended per move). Never hand-invent a curve. Keep your design system: your palette, your font, your real UI crops, AI portraits.
5. **Audio stays fixed when rebuilding for originality.** Keep each beat's frame window and its hit points (VO words, drops). Only the visuals inside change, so there's no ElevenLabs cost.
6. **Rebuild the worst-scoring beats first,** in rounds of about 4 agents, and re-measure after each round.

Templates: `${CLAUDE_PLUGIN_ROOT}/skills/video-frame-locked-remake/templates/`. Analysis scripts: `${CLAUDE_PLUGIN_ROOT}/skills/video-reference-video-analysis/scripts/`. Audio scripts: `${CLAUDE_PLUGIN_ROOT}/skills/video-film-audio-elevenlabs/scripts/`.

## Always
- **Write the project's `STORY.md` first** (story arc, copy, brand, faces, assets, voice, music, banned words and claims) and check every cut against it.
- **Story before geometry.** Map every REF beat to YOUR story and show the user that table in plain words (seconds, what's on screen, what the voice says) BEFORE building. Literal ports of REF beats that don't fit your story get rejected: e.g. a reference's outreach DMs → your launch post; a disconnected "300 signups" → reactions → signups via the post, so the number has a cause.
- **Stay in sync with REF's craft when modifying.** Every change keeps the reference's learnings, even where your story differs:
  - its camera grammar (push-ins, whips, pans and their easing curves);
  - its reveal cadence (word and letter timing, card fly-in tracks);
  - its rhythm (a change on every beat, no dead frames, a brisk VO with few pauses);
  - its transitions (floods, snaps, the continuous camera, no slide fades);
  - its type scale, spacing and background grid.

  New elements borrow an existing REF motion: e.g. reaction cards reuse the flying-card tracks, a post modal reuses REF's card zoom curve. Stretches come in whole beats and reuse REF's easing.

  After every modification, still render the internal REF-vs-ours sync check (RemakeLocked) and the jump scan. Explain any deviation in DIFFERENCES.md; otherwise put it back in sync.
- **Frame-lock is a tool, not the goal.** When your story needs a different layout (a centred post modal instead of REF's docked chat window) or more time (let the post be read), break the lock for that beat. Use the `STRETCHES` remap, see below.
- **Remotion, never HTML/Playwright screen capture.** The `seek(t)` "pure function of frame" engine = a Remotion composition at REF native res/fps/frame count; shots `{id, f0, f1, render(lf, F)}` routed by `useCurrentFrame()`.
- **Content hygiene:** no other brands' names or logos (platform-STYLE UI is fine, without logos or names); no real people (AI-generated portraits of people who do not exist, gender-matched to names, look better than initials); flag risky claims to the user once and let them decide.

## Phase 0 — get + measure REF (lead, no agents)
Detailed commands: `video-reference-video-analysis`. Audio pipeline: `video-film-audio-elevenlabs`.
1. Check the platform's terms, then download with `yt-dlp`. If a site won't let you download, choose another reference; never work around a login or block.
2. `ffmpeg -i reference.mp4 -start_number 0 -q:v 3 remake/ref/full/f%04d.jpg`; audio.wav; labelled 1 fps sheets via PIL.
3. Cuts: per-frame mean-abs-diff on 192×108 gray → `diff.npy`; spikes vs local median. Pick group seams ON transition spikes (e.g. hard snaps), never mid-move.
4. Tokens by pixel sampling (text ink mean, flood colours, bg), font by eye from crops, grid geometry from row/col mean profiles.
5. Narration: `whisper audio.wav --model small --word_timestamps True`. Build a slot table REF line → OURS line with similar syllables.
6. Music tempo per band (kick 40–120, snare 1.5–4k, hats 7–16k). **Kick-led reads can be a 3/4 alias**; listeners hear the snare/hat tempo. Also compare brightness (> 4 kHz share).
7. Write `remake/SPEC.md` (from `templates/SPEC.template.md`: global, palette swap table, copy map by frames, groups, narration table, audio notes) + `remake/BRIEF.md` (from `templates/BRIEF.md`: acceptance bar, file rules, verify loop, report format).

## Phase 1 — engine (lead)
- Copy `templates/core.tsx`, `Remake.tsx` (router with `STRETCHES`, `CUTS`, `toRef` and the `locked` prop), `audio.ts` → `src/Remake/`. Put your real brand icon and product screenshots in `public/assets/brand/`, set `BRAND_NAME` / `ICON_ASPECT`, the palette `T` and the font in core.tsx from `knowledge/brand/brief.md`, and `FRAMES` from SPEC.md. Stub `shots/G1..G4.tsx`. Register BOTH compositions in Root.tsx exactly as in `templates/Root.snippet.txt`: `Remake` (stretched, with audio) and `RemakeLocked` (REF timeline, muted, used by the compare tools). Multi-reference: use `templates/Remake.multi.tsx` instead.
- **Faces:** no portraits ship with the templates. To use photo avatars, add AI-generated portraits of people who do not exist (generated by you, or licensed for commercial use) as `public/remake/faces/f00.jpg …`, then set `FACES` and `FACE_GENDER` in core.tsx. With `FACES = 0`, `<Avatar>` draws initials.
- Copy `templates/tools/finalize.sh` and the compare tools from `${CLAUDE_PLUGIN_ROOT}/skills/video-reference-video-analysis/scripts/` (`compare.py`, `render.mjs`, `sheet.py`, `sync.py`; the only copy) → `remake/tools/`. Run them from the project root. `render.mjs` uses @remotion/bundler + @remotion/renderer resolved from `node_modules/@remotion/cli`, one browser for many stills: `node remake/tools/render.mjs <OUT> compare <frames>` → REF|OURS|diff sheet; `full f0 f1`; `sync.py` stacks REF over ours; `sheet.py` 1-per-second REF|OURS.
- core exports: tokens T (palette already swapped), FONT, E easings, kf, samples (measured tracks), Camera, GridBg, Cursor, Ripple, Logo (mask), Wordmark, Reveal, Avatar, hash, R(name) for real UI crops.

## Phase 2 — parallel build (background agents G1..G4 + AUDIO)
- 4 contiguous frame groups, each writes ONLY `src/Remake/shots/<G>.tsx` (+ `tracks/<G>_*.json`, `remake/spec/<G>.md`). Prompt = range, REF content guide by frames, SPEC swaps for that range, "measure with numpy, compare loop ≤ 15 frames, cover the whole range CLOSE before polishing, keep tsc clean, report table".
- AUDIO agent (give it `video-film-audio-elevenlabs` and its **Cost discipline** rules verbatim): REF analysis; music generated ONCE (ElevenLabs Music `music_v1` at the REF's snare/hat tempo) or licensed library music; 20 s previews for the user; numpy SFX on REF onsets; VO = `<your voice id>` on eleven_v3, ONE base take via `/with-timestamps`, cut per line, ≤ 8 % stretch; later line changes via `el_tts.py patch`, 1 take; timeline in `timeline.py`; sidechain duck; −14 LUFS, TP ≤ −1; outputs `public/remake/mix.wav`, `LICENSES.md`, `SLOTS.md`. It must report the mix's final timestamp and then not touch it.
- The lead reviews every group with its own compare renders and sends precise fix lists (frame numbers, what REF does). Seam ownership: if REF holds a scene 2 frames past your seam, move those frames to the owning group.

## Phase 3 — integrate + verify
- Full render: `npx remotion bundle` then `npx remotion render <bundle> Remake out.mp4 --crf=16 --concurrency=4`; check nb_frames == REF (plus stretches).
- Jump scan: ours per-frame diff vs REF `diff.npy`; flag `d > 6 and d > 2.5·ref + 3` → send to the owning group (usually overlapping-shot hand-offs).
- Seam sheets (last 2 / first 2 frames per seam), 1 fps sheet, old-brand colour scan (hue mask on REF's brand colours; semantic reds like error dots are fine).
- Palette rule: preserve LIGHTNESS, not colour density (a dark colour at a light colour's alpha looks much darker).
- Deliver `out/remake/`: 1080p60 master, 1080p30 web and the X file. SPEC.md and DIFFERENCES.md stay in `remake/`, and sync-check.mp4 is INTERNAL; deliver only the user's video.

Typical timing: analysis about 30 min, 4 groups built in about 35 min in parallel, fix rounds about 15 min each.

## Modifying an existing remake (runbook)
Ownership (one agent per range; the lead owns core/router/Root):
| what | where |
|---|---|
| beats in the first quarter | G1 `src/Remake/shots/G1.tsx` |
| second quarter | G2 |
| third quarter | G3 |
| last quarter, end card | G4 |
| palette, fonts, Avatar/faces, helpers | `src/Remake/core.tsx` |
| timing stretches and cuts / locked comp | `src/Remake/Remake.tsx` (`STRETCHES`, `CUTS`, `toRef`), `src/Root.tsx` (`Remake`, `RemakeLocked`); audio mirror in `remake/audio/timeline.py` (keep both in sync) |
| VO text + takes | `make-vo.py` (LINES, `BASE`, `REWORDED`), `SLOTS.md` |
| music / SFX / mix | `make-music.py`, `make-sfx.py`, `mix.py` → `public/remake/mix.wav` |

Recipes:
- **Keep copy editable:** each group keeps its on-screen lines in one `<G>_COPY` block of plain strings (`*…*` marks the accent), mapped onto REF's reveal frames by a `<G>_SLOTS` table. Extra words spread evenly across the slot window. A copy change is then a one-line edit. Ask groups to set this up early.
- **Change on-screen copy:** tell the owning group the exact new text, the REF frames, and "keep REF reveal timing". Width changes are fine.
- **Change a voice line:** only after the user has approved ALL copy changes, as one batch. Patch the line with `el_tts.py patch --line ID` (1 take). Fall back to one full-context take only if the patch sounds different from its neighbours. Level-match, run `mix.py`, and re-check the hit words with Whisper.
- **Shorten or tighten:** `Remake.tsx` has `CUTS: [{C0, C1}]` (REF spans removed entirely) and negative-EXT `STRETCHES` (speed-ups). `toRef` applies both in REF order. Keep the removed total in WHOLE music beats. Put cut edges just before any next-scene text fades in; check 3–4 frames on each side, since stray cards or headlines peek through. The music re-cut and the SFX shift go through `timeline.py`. A 35 s cut can drop to 30 s this way with no new visuals.
  - Signals: "too long", "we repeat the same thing" (say each idea ONCE), and "one sentence across 3 screens feels slow" (speed that span up about 1.2–1.3×).
- **Give a beat more time:** add an entry to `STRETCHES` in `Remake.tsx`. `toRef` handles several segments. Use it to stay on a post the viewer must read, or to focus on a key comment (a still, big hold). Pick EXT as a whole number of music beats (60·fps/BPM·n), so the music re-cut stays on the grid. Every later audio slot shifts by EXT/fps: tell AUDIO the new total frames and the shifted hit times. The compare tools use `RemakeLocked` (REF timeline, muted).
- **Finalize in one command:** `bash remake/tools/finalize.sh <name>` (template in `templates/tools/`, macOS). It stats the mix, bundles, renders, remuxes if the mix changed, runs the jump scan using `remake/tools/stretches.json` (`{"stretches": [[S0,S1,EXT],…], "cuts": [[C0,C1],…]}`, keep it equal to `STRETCHES` and `CUTS`), exports the master, web and X files, and opens the master.
- **Render (manual):** make sure `public/remake/mix.wav` is final BEFORE `npx remotion bundle` (the bundle copies public/). Or remux: `ffmpeg -i video.mp4 -i public/remake/mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k out.mp4`.
- **After every render:** run the jump scan (ours vs REF `diff.npy`; with a stretch, compare with RemakeLocked or ignore the shifted range) and a 1 fps sheet.

## Multi-reference mode (combine the best beats of 2–3 videos)
**The fastest way is the donor-override pattern:**
- Keep the spine film as it is.
- Each donor beat is a shot with `replace: [r0, r1]` in REF frames. Inside the window only donor shots render; outside it the spine renders untouched. Same timeline, so the same voice mix, and **no new ElevenLabs**.
- Compositions: `RemakeV2` and `RemakeV2Locked`.
- One agent per donor beat (write a short `remake/DONOR_BRIEF.md`). Each extracts the donor moment at 60 fps, MEASURES the motion (push curve, stagger, roll, press, check pop), rebuilds it in your style, and pixel-checks both seams against the spine.
- New sound cues (clicks, dings, slams) are numpy-synthesised onto the existing mix.
- Good donor beats: a button that fills the frame and gets pressed, a dashboard push-in with a number roll, a live re-rank of rows, a real pay flow.

Use the full EDL router below only when the spine itself changes between references.

1. **Analyse each reference separately:** `video-reference-video-analysis` → `remake/ref/<A|B|C>/` with its own full/, diff.npy, words.json, tempo and SPEC notes. Normalise every reference to the SAME resolution and fps before measuring (ffmpeg `-vf scale=1920:1080,fps=60`).
2. **Pick a SPINE reference.** It owns the global look: type, palette mapping, background grid, camera grammar, music tempo and VO pace. The other references only lend BEATS: a transition, a reveal, a data viz, a hook.
3. **Beat-picking table for the user,** in seconds and plain words, then approval:

   | our beat | taken from | ref time range | why this one | length in our cut |
   |---|---|---|---|---|

   Keep each borrowed beat whole, from one transition to the next. Never splice half a camera move.
4. **Build the timeline as an edit decision list:** use `templates/Remake.multi.tsx`, where `EDL: [{ ref, f0, f1, out0, ext? }]`, `toRefEDL(out) → {ref, F}` is unit-tested, and each shot declares `ref`. Register `Remake` (the EDL cut) plus one `RemakeLocked<X>` per reference. Compare with `COMP=RemakeLockedB REF=B node remake/tools/render.mjs <OUT> compare <frames>`; `REF=B` also works for `sync.py` / `sheet.py`. The template is typechecked; verify it on the first beats.
5. **Seams between references:**
   - Put every cut on a transition that exists in the spine's grammar (flood, whip, push). Build it with the spine's measured curve, so a borrowed beat enters and leaves "in the spine's language".
   - Restyle borrowed beats to the spine's palette and type, keeping their motion. Motion comes from the donor; the look comes from the spine.
6. **Audio:** one music bed at the spine's tempo. Re-time borrowed beats to land on its bars (whole-beat stretches). Write VO slots for your script, not the donors' narration.
7. **Share, don't copy.** Base groups EXPORT the components and camera that donor shots continue from (composer, cursor path, backgrounds, helpers). Donor shots import them. Copies drift every time the base changes.
8. **Verify** each segment against its OWN reference: motion_sync windows and jump scan per segment. Check the seams by eye; no reference has them, so judge by feel.
Cost: about 30 min of analysis per extra reference; the build is the same size.

## Review checklist (check BEFORE showing a cut)
- The story beats read as YOUR story (e.g. a public post, not DMs, if that's your launch).
- Anything the viewer must read stays on screen long enough.
- Every number has a visible cause.
- Faces are portraits (or clean initials), never real people.
- No screenshots showing other brands or the wrong currency.
- Motion in sync with the reference (motion_sync + strips).
- Key visuals strong enough; focus moments actually in focus.

## Working rules
- **Motion re-sync method:** run `motion_sync.py` per 20-frame window. Send the owning group a numbered list: window, REF vs ours speed and energy, and what to do (add whip / add drift / tame / retime). Ask for a before/after table plus strips.
- **Never move what the viewer is reading.** While text is being typed or read (a post, a comment, a price), keep it centred and still, with at most a straight push-in. Motion grammar yields to readability.
- **Focus beats need time.** A readable half-second isn't enough. Add a whole-beat STRETCH and a still, big hold (text ≈ 64–72 px, ≤ 2 px/frame drift, other items sliding in). Ease INTO and OUT of holds over about 8–10 frames: a hold that ends into a full-speed pull-back pops, which the jump scan catches.
- **Story and claims research:** spawn a research agent only when the user asks ("is this real?"). Present the findings as options with a recommendation. The user owns bold claims, so flag a risk once and never dilute on your own.
- **Deliverables:** `out/remake/` master 1080p60, web 1080p30, and `<name>-x.mp4` for X: H.264 High 4.1, 30 fps, CRF 20, maxrate 8M, AAC 128k, faststart.
- **Before every final render,** `stat` the mix, then bundle and render. `stat` again afterwards and remux if the mix changed. Run the jump scan with the STRETCHES mapping.
- **Review with your own eyes before relaying.** REF is LEFT in compare sheets; don't flag a label that is on REF's half.
- **Measure before you instruct.** Send coordinates you measured, not guessed. Agents that measure first will correct you, so let them.
- **Batch changes, especially anything that costs ElevenLabs credits.** Hold AUDIO until every copy decision is final, then send ONE message.
- **Stale source, not just a stale mix:** a shot file edited after `remotion bundle` isn't in the render. Before bundling, make sure every agent is idle. After rendering, compare `stat` of `src/**` against the bundle time, and re-render if anything is newer.
- **Agent messages cross.** Send ONE consolidated change per agent, keep a pending list, and check the files (grep for the new text) rather than trusting a report that may predate your message.
- **Checking copy with grep:** shots store words one per reveal unit, so grep each WORD, not the phrase, or look at a rendered frame.
- **User-facing updates:** seconds and plain words, not frame numbers or agent names.

## Requirements
- ffmpeg, yt-dlp, python3 with numpy, scipy, pillow and soundfile, openai-whisper; `finalize.sh` is for macOS (notes inside for Linux)
- Node 22 and a Remotion project (`@remotion/cli`, `@remotion/bundler`, `@remotion/renderer`, `@remotion/google-fonts`, `@remotion/media`)
- ElevenLabs API key (`ELEVENLABS_API_KEY`) and voice id (`ELEVENLABS_VOICE_ID`)

## Never
- Download a reference against the platform's terms, or work around a login, paywall or block.
- Reuse a reference's music, voice, logo, footage, screenshots or brand names.
- Trace one film: no single reference above 25 % of the runtime.
- Deliver the internal sync check, or publish the film. Gates: `shared/gates.md` (core).

## Shared knowledge
**Read first:** `knowledge/brand/brief.md` (palette, fonts, logo), `knowledge/positioning.md`. The project's `STORY.md` and `remake/` folder hold the film's own files. **Write after:** one dated line in `knowledge/log/<date>.md` (what was made, credits spent). Paths from `shared/knowledge-tree.md` (core).

## Bootstrapped core
Ask `lessons` (theme `video`) before Phase 0. If it isn't connected, carry on with this method.
