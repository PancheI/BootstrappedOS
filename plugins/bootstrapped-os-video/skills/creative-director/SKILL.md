---
name: creative-director
description: Creative Director (advanced) - promo films of about 30 seconds built in Remotion with an ElevenLabs voice - a story gate, one measured motion system, silent drafts first and a two-sided review before the founder sees a cut. Use for product promos, launch films and short reels when the simple launch-video cut is done and you want studio-grade motion.
---

# Creative Director (advanced)

When the video module is installed, the core `creative-director` agent loads this skill for studio-grade films. For a first film, use `launch-video`.

The founder approves the story, the style plan, the silent draft and the final cut. The agent builds, measures and reviews. Every rule here cost the author a rejected cut; his quotes are the test. Module rules (length, references, brand, paid generation): [RULES.md](../../RULES.md).

**References:** none. **Tools:** ElevenLabs (voice; the `elevenlabs` connector), Remotion (video in code; ask `remotion-docs`). Optional public skill: remotion-best-practices. Full pipeline: `video-promo-video-playbook` (entry point), then `video-motion-system-storyboard`, `video-reference-scout` / `video-reference-video-analysis`, `video-frame-locked-remake` or `video-short-form-reel`, and `video-film-audio-elevenlabs`.

## The process
1. **Story gate.** About 30 seconds, hook in second one. A beat table (seconds / on screen / voice) in the customers' own words. **Gate:** the founder approves it before any build.
2. **One style plan.** One spine film owns camera, easing, rhythm and type; other references lend single moments, redone in that grammar (`video-motion-system-storyboard`). Palette and fonts from `knowledge/brand/brief.md`. **Gate:** the founder approves the plan.
3. **Build:** one thing per frame, show, don't type. All motion is a pure function of the frame number. Land state changes on music beats (`video-film-audio-elevenlabs/scripts/music_beats.py`; it uses librosa if installed and a built-in tempo estimate if not).
4. **Silent drafts first.** "Before you spend voice give me videos without a voice... once they are good we record the voice." Render drafts muted on an estimated timing grid. **Gate:** the founder approves the silent cut.
5. **Voice last.** Lock the script, record one base take, then patch single lines. End warm, not hyped (an excited ending was "annoying"). **Gate:** a yes on the character cost first.
6. **Review on both sides** (see Quality bar), then show the founder.
7. **Ship:** master audio at about -14 LUFS, sound effects on cut points only. Export 16:9 and a separately composed 9:16. Keep all copy (names, prices, numbers) in one data block, so a version for a second audience is a copy change. Watch the final file once, start to end, on a phone.

## Decision rules
- **Emotion over features.** "No one connects to a box." Copy is founders' real excuses ("I don't have time", "I don't know where to start"), never a feature list.
- **Every number has a visible cause.** "300 signups" from nowhere was cut; sign-ups arriving "via your launch post" stayed.
- **The founder owns the claims.** Flag a risky claim once, in one line; never soften or harden it yourself.
- **Copy timing from proven films by measuring them, never their assets.** Originality is combining measured sources, none above 25 % of the film ([RULES.md](../../RULES.md)).
- **One look, including the ending.** "Unify the style and coloring, I got different colors in the last." No dark act. Rebuilding beat by beat, each from a different reference, passed every metric and still got "glued, not a coherent motion design".
- **Own the look.** Delegating beats to separate builders fragmented the film. Helpers measure and research; the lead builds the look.
- **One hero and 6 words or fewer per frame.** "It doesn't have to be slower... just not while showing 5 different dashboards." Remove things; don't slow down.
- **Show, don't type.** "I see only text; that's not the purpose of a motion designer." Every beat needs a visual object or real UI; text is numbers, labels and captions.
- **Easy to watch at a glance.** Headlines 96 px or more, key numbers 160 px or more, zoom onto what the voice names, no corner text, no near-empty frames.
- **Pacing over the whole film:** 12 hard cuts a minute at most, no shot under 0.7 s. Stacking each beat's fastest reference can double the cut rate.
- **Stay in motion design.** Photoreal 3D ("we went too far into graphics building"), stock montages and type-only scenes were all rejected.
- **Energy matters.** A slow music track made the product feel slow; a faster one won.

## Quality bar
- [ ] About 30 seconds (60 only for a walkthrough).
- [ ] **Automatic checks pass:** length, frozen stretches (0.8 s at most outside the end card), empty frames, cuts per minute, voice transcript against the script, pronouns against faces.
- [ ] **An independent reviewer** (an agent with no part in the build) watched a 2 fps contact sheet and the transcript, tried to fail it with a numbered defect list, and the defects are fixed. The author's failed cuts had frozen stretches, near-empty frames and "she" said over a man's face; judging from a few stills missed all of them.
- [ ] Real logo file and real product screens; one palette and one type system from the brand brief.
- [ ] Watched once, start to end, on a phone.

## Never
- Record the voice before the silent cut is approved.
- Fake a product screen or rebuild a logo: "the checkout is fake, style is not uniform".
- Invent motion on the advanced route ([RULES.md](../../RULES.md)).
- Publish the film. Gates: `shared/gates.md` (core).

## Shared knowledge
**Read first:** `knowledge/brand/brief.md`, `knowledge/positioning.md`, `knowledge/numbers.md`. **Write after:** one dated line in `knowledge/log/<date>.md` (what was made, run time, credits spent). Paths from `shared/knowledge-tree.md` (core).

## Bootstrapped core
Ask `recipes` (area `video`) before step 1 and `lessons` (theme `video`) at the decision rules. If it isn't connected, carry on with this method.
