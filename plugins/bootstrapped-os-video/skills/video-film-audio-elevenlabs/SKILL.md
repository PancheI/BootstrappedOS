---
name: video-film-audio-elevenlabs
description: Build a promo film's audio — ElevenLabs voiceover as ONE continuous take cut per line and fitted to timing slots, ElevenLabs Music (or licensed library music) beat-matched so drops land on picture hits, numpy-synth SFX, sidechain duck and −14 LUFS master. Use for any video voiceover/music/mix task, "change a VO line", "music too slow", "new voice take", or audio for a remake.
---

# Film audio with ElevenLabs

**In short:** record the voice once and patch single lines, generate or license the music once and re-cut it locally, make the sound effects in code, then mix to a standard loudness. The founder approves the script and every paid generation. Advanced and optional; module rules: [RULES.md](../../RULES.md).

Scripts: `${CLAUDE_PLUGIN_ROOT}/skills/video-film-audio-elevenlabs/scripts/`. Copy them into your project (e.g. `remake/audio/`) or run them in place from the project root. They read `PROJECT_ROOT` (default: the current directory) and `AUDIO_DIR` (default: `<root>/remake/audio`, work files in `work/`). Edit the constants for your film: the frames, stretches, cuts, tempo and the two music hits in `timeline.py` (all scripts read it); the lines and slots in `make-vo.py`; the candidate tracks and voice pauses in `make-music.py`; the sound events in `make-sfx.py`. The shipped values are a neutral example for a 30 s film, so read each header before running it.

Keys: `ELEVENLABS_API_KEY` and `ELEVENLABS_VOICE_ID` (your voice id) in the environment or the project's `.env`. Never print the key.

## Cost discipline (ElevenLabs is the expensive part — read first)
Re-recording the whole script for every copy change costs several times the characters you need. The waste comes from three habits:
- re-recording the WHOLE script for a one-line change;
- several takes per change;
- copy changes arriving one at a time, with messages crossing (the same line recorded 3 times).

Rules:
1. **Lock the script before any TTS.** Show the user the plain-words beat table (seconds / on screen / voice) and get a yes. Batch every copy change into ONE run.
2. **`scripts/el_tts.py`** (cache + usage log + patching):
   - `full` renders one base take of the whole script, once.
   - `patch --line ID` sends only [previous line + NEW line + next line], so the neighbours keep the voice consistent. It cuts the new line out using the timestamps, costing ~50–300 chars instead of ~1,500.
   - Identical requests come from `.el_cache` for free.
   - `usage` prints the chars paid versus served from cache. Report it to the user when asked.
   - `--dry` shows the cost before sending.
3. **Takes = 1 by default.** Only make a 2nd take when the Whisper check or slot fit fails (a misread name, a line that won't fit at ≤ 8 %).
4. **Draft cheap, finish once.** Test timing with `--model eleven_flash_v2_5`; render the final lines with `eleven_v3` once.
5. **Timeline changes never need TTS.** Stretches and shifts just re-place cached lines. The mapping lives in ONE file, `scripts/timeline.py` (REF → film time, several stretches and cuts); every audio script imports it.
6. **Music: generate once per project**, a plain prompt at the film length (`el_music.py prompt --bpm <tempo> --length <s>`). Run it with `--dry` first, show the founder the length and the credit cost, and get a yes before the paid call. Every later timeline change is a LOCAL re-cut in whole beats. Composition plans tend to ignore section timings, so they waste credits. Make previews from that one file.
7. Whisper checks, level matching, SFX and mixing are local and free, so do all verification locally.

## Voice
- **Voice / model:** `<your voice id>` (set `ELEVENLABS_VOICE_ID`), `eleven_v3`. `make-vo.py` prints the character count and stops; add `--go` only after the founder's yes.
- **Health check:** make a tiny TTS POST. Some restricted keys return 401 `missing_permissions` on `/v1/models` and `/v1/user`, which is normal. A real `invalid_api_key` means the user has to fix the key: tell them, and don't work around it.
- **One continuous take:** send the whole script with `/v1/text-to-speech/{voice}/with-timestamps` and cut it per line at the character timestamps. Line-by-line generation changes the voice between lines, and listeners hear "a different voice in the second half".
- **Fitting to slots:** fit each line into its slot with atempo, **capped at 8 %**. If it still doesn't fit, start it early (≤ 0.35 s), keeping a 0.25 s breath.
  - Anchor key words on picture hits with Whisper word times: `ANCHOR`, `SHIFT` in `make-vo.py` (e.g. a word on a button click, a number on its big-number hit).
- **Rewording a line:** default is `el_tts.py patch` (the previous, new and next line only, 1 take). If it sounds unlike its neighbours, make ONE full-context take and use only that line. Either way, level-match it (about ±0.7 dB) and keep the base take for untouched lines (`make-vo.py`: `BASE`, `REWORDED = {"05": "take_10.json"}`). eleven_v3 has no previous_text stitching.
  - `make-vo.py` loads every `work/patches/*.json` written by `el_tts.py patch` as a take of the text it sent (`"sent"` + `"take"`). In `REWORDED`, name the patch file: `REWORDED = {"07": "patch_07-10.json"}`. `cut_present()` cuts only the lines found in that short take, and each patched line is level-matched to the base on the context lines the patch shares with it.
    - **Pass the base take's voice_settings** to the patch: `--settings '{"stability":0.5,"similarity_boost":0.8}'`. Otherwise the patch uses the voice defaults and sounds different.
    - **Adjacent changed lines:** merge them into ONE patch entry in a temp lines.json (e.g. `"07-10"` = lines 7–10 joined). That sends prev + block + next once instead of several overlapping windows, roughly halving the characters sent. Check the `x-character-count` response header for what was billed.
    - When no line needs a new full take, `make-vo.py` does not call the full-take generator.
- **Delivery:**
  - Pace: natural and fast (about 144 words a minute for a brisk launch film), short ellipsis beats, no long gaps.
  - Tone via v3 tags, e.g. `[tired]`, `[honest]`; the ending warm and inviting, not hyped.
- **Checks:** run Whisper (`whisper … --word_timestamps True`) on the placed VO track to confirm every line and the hit words.

## Music
- **Measure the reference tempo per band** (`bpm.py`, `grid16.py`): kick 40–120 Hz, snare 1.5–4 kHz, hats 7–16 kHz.
  - A kick-led read can be a **3/4 alias**: e.g. 108 BPM on the kick while the snare and hats run at 144, and listeners hear 144. "Too slow, not energetic" means you matched the wrong band.
  - Also compare brightness (`bright.py`: energy share above 4 kHz, below 100 Hz).
- **Candidates:** give the user 20 s previews to choose from (`music-cand-N.wav`).
  - **ElevenLabs Music** (`el_music.py`, POST `/v1/music`, `music_v1`, plain prompt with BPM/style/sections, instrumental) can be generated natively at the reference tempo.
  - Royalty-free library music (e.g. Mixkit, under its own licence) as backup. Record the URL and licence in LICENSES.md.
- **Cutting (`make-music.py`):**
  - Cut on bars so drops land exactly on picture hits (logo burst, big-number hit).
  - Dip under dramatic pauses in the voice (`DIPS`); filtered build before a drop; stutter into the second drop; hard stop on the last frame.
  - When the film timeline changes, insert or remove WHOLE beats: 60·fps/BPM·n frames, e.g. 4 beats at 144 BPM = 100 frames at 60 fps. `make-music.py` works out the section lengths from `timeline.py`, so a re-run is enough.
  - With no arguments it builds every candidate whose track is available; a generated track is skipped until you have made it.

## SFX and mix
- **SFX (`make-sfx.py`):** synthesise everything with numpy (clicks, pops, whooshes, risers, impacts, dings, typing ticks, reaction pops), placed on the reference's onset times (`analyze.py`) plus your own UI clicks. No samples means no licence issues.
- **Mix (`mix.py`):**
  - Duck the music under the voice with a sidechain gain envelope.
  - Limiter, then two-pass loudnorm to **−14 LUFS, TP ≤ −1 dBTP**.
  - The output is exactly the film's frame count (samples = frames/fps·48000), written to `public/remake/mix.wav`.
- **Render order:** the mix must be final BEFORE `npx remotion bundle`, because the bundle copies `public/`. Otherwise remux: `ffmpeg -i video.mp4 -i mix.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 256k out.mp4`.
- **After rendering, re-check `stat mix.wav` against the bundle time.** An audio agent can rebuild the mix after its report. If the mix is newer, remux.
- **Deliverables:** `public/<name>/mix.wav`, `SLOTS.md` (line | slot | start–end | stretch | take), `LICENSES.md`.

## Requirements
- ffmpeg, python3 with numpy, scipy and soundfile, openai-whisper for checks
- librosa is optional: `music_beats.py` uses it if installed and falls back to a built-in tempo estimate if not
- ElevenLabs API key with TTS + Music access: `ELEVENLABS_API_KEY`; voice: `ELEVENLABS_VOICE_ID`

## Never
- Pay for a voice take or a music track without the founder's yes on the cost.
- Print the API key.
- Use a sample or track without its licence recorded in `LICENSES.md`.

## Shared knowledge
**Read first:** `knowledge/brand/brief.md` (voice and tone). **Write after:** credits spent, one dated line in `knowledge/log/<date>.md`. Paths from `shared/knowledge-tree.md` (core).

## Bootstrapped core
Ask `lessons` (theme `video`) before the first paid call. If it isn't connected, carry on with this method.
