---
name: video-short-form-reel
description: Make a ≤15–30 s vertical (9:16) reel / Short / TikTok for any product — hook in the first second, works muted (burned-in captions + kinetic type), one idea, loopable, built in Remotion by reusing the long film's story and assets. Use when the user asks for a reel, short, TikTok, "15 second video", "vertical version", or a social cut of an existing film.
---

# Short-form reel

Load `video-promo-video-playbook` and the project's `STORY.md` (story, tone, claims), then this skill. Everything from the long-form skills applies (Remotion only, measure the references, parallel agents, cost discipline). This skill adds the rules that are specific to short-form.

Advanced and optional. Module rules (length, references and terms, measured motion, brand, paid generation): [RULES.md](../../RULES.md).

## 1. Rules that differ from long-form
1. **The hook is the first 1–1.2 s, and frame 0 is the thumbnail.** Open on the most emotional frame at full size (e.g. a customer's complaint, a surprising number). No fade from black, and hit within 3–4 frames.
2. **Works MUTED.** Most reels autoplay silently. Burn in one caption line at a time (a white pill in the lower third) and carry the story with huge kinetic words. Voice is optional; add it last (about 150 ElevenLabs characters).
3. **One idea, six beats** (example for a 15 s reel):

   | beat | time | example |
   |---|---|---|
   | hook | 0–1.2 s | the most emotional moment |
   | pain | 1.2–2.8 s | the problem in one number |
   | reveal | 2.8–4 s | "So we built <product>", logo slam on the music drop |
   | proof | 4–10.8 s | the product doing the thing, in 3–4 measured moves |
   | outcome | 10.8–13.4 s | the result, with honest wording (mark projections as projections) |
   | CTA + loop | 13.4–15 s | "Try <product> now", then smash back to frame 0 |

4. **Vertical recomposition, never a crop of the 16:9 film:**
   - one element per frame, BIG (UI text ≥ 40 px, slam words ~80 % of the width);
   - safe area y 250–1500 and 90 px side margins;
   - keep the bottom ~420 px calm for the caption pill and the platform UI.
5. **Loop:** the last 4–6 frames return to frame 0's look so the replay is seamless. A replay counts as a watch.
6. **Pace:** about 14 cuts per minute or faster, with cuts and slams on music beats (at 144 BPM that's 12.5 frames per beat at 30 fps).
7. **Export:** 1080×1920, 30 fps, H.264, AAC, faststart, ≤ ~15 MB. Also offer a 1:1 version for LinkedIn feeds.

## 2. References
- Use `video-reference-scout` with a `reel` profile calibrated from 2–3 short product reels you like (`scout.py calibrate reel a.mp4 b.mp4 c.mp4`). If the liked reels are longer than your target, ignore the duration term.
- The best references are pure product-motion reels: tilted light UI cards on a solid canvas, word slams, a caption pill, ranked rows, a button that fills the frame, counter rolls, flying stat cards.
- Most big-brand Shorts are talking heads or skits (the scout's UI rule caps them). Don't spend long looking there.

## 3. Build (Remotion)
- Composition `Reel15` (and `Reel15Silent`), 1080×1920 @ 30 fps, in `src/Reel15/` (a router plus scenes R1–R3, `theme.ts` with the palette and BEAT, and `Captions.tsx` owned by the lead with a `[f0, f1, text]` table). Write a short `REEL_BRIEF.md` for the scene agents.
- 3 parallel scene agents (hook/pain/reveal, proof, outcome/CTA/loop), built from the lead's locked style kit. The lead owns the look, captions and music, and reviews every scene.
- **Music:** cut 15 s from the long film's music bed so the drop lands on the reveal (about 2.8 s), then fade out at the end. It's local, with no new generation.
- **Captions:** in the brand's voice, from `STORY.md` and `knowledge/brand/brief.md`. Never claim fiction is real ("Real comment. Real launch." on a staged scene is not OK; "Launch day." is).
- **Measure first.** If builder agents are unavailable, the lead still measures the reference reels before animating; a reel built without measured tracks must be redone before shipping.

## 4. Checklist before showing it
- [ ] Frame 0 works as a thumbnail and stops the scroll.
- [ ] Watched muted: the whole story is understood from captions and type alone.
- [ ] Every text ≥ 40 px, inside the safe area, and nothing behind the caption pill.
- [ ] Cuts on beats, the drop on the reveal, the loop seamless.
- [ ] Tone and claims per `STORY.md`.
- [ ] Exported 9:16 (plus 1:1 if needed) and watched end to end.

## Never
- Crop the 16:9 film instead of recomposing for 9:16.
- Claim a staged scene is real.
- Publish anything. Gates: `shared/gates.md` (core).

## Shared knowledge
**Read first:** `knowledge/brand/brief.md`, the project's `STORY.md`. **Write after:** one dated line in `knowledge/log/<date>.md`. Paths from `shared/knowledge-tree.md` (core).

## Bootstrapped core
Ask `lessons` (theme `video`) before the build. If it isn't connected, carry on with this method.
