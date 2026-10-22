---
name: video-motion-system-storyboard
description: MANDATORY gate before building or rebuilding any multi-beat promo film (especially multi-reference/"original" films). Pick ONE motion spine, write a Motion Design System (canvas, type, element kit, 5–7 transitions, easing family, camera, rhythm) and a per-beat storyboard (VO → one hero → in/during/out move with measured source) and get the user's yes BEFORE any code. Use when the user says the film feels "glued", "not coherent", "different styles", or before round 1 of a new film.
---

# Motion system + storyboard FIRST

Plan the whole flow and the motion design end to end, pick the best sources, then implement. The founder approves the system and the storyboard; the agent writes them. Advanced and optional. Module rules (length, references and terms, measured motion, brand, paid generation): [RULES.md](../../RULES.md).

## Why this exists
Rebuilding a film beat by beat, each time with a new "best donor for this beat", makes every beat speak a different motion language: a different accent font, a different logo reveal, a different transition, a different stage. The metrics can pass and the film still feels glued. **Coherence comes from REPETITION of one small grammar**, not from per-beat quality. A strong launch film typically uses about 6 transitions and one card kit.

## The gate (in order; nothing is coded until step 5 is approved)
1. **Pick the spine (ask once).** One reference owns the SYSTEM: its camera, transitions, easing curves, rhythm, type slot and card kit. Other references lend only HERO MOMENTS (an object, a layout), re-expressed inside the spine's grammar. Cap per source still applies (≤ 25 % of runtime traced from any one clip).
2. **Extract the spine's grammar from measurement** (SPEC.md / frame sheets from `video-reference-video-analysis`, never from memory):
   - transition vocabulary: list each with its REF frames (e.g. a click-flood, an accelerating up-exit, a whip-pan, a zoom-through-letter into a burst, a wave wipe, each with its frame range);
   - entry curves (word stagger, rise + overshoot, pop 0.31 → 1.04 → 1.0, exp-decay τ);
   - camera rules (constant grid drift, slow push during holds, one tilt plane for data UI);
   - rhythm (BPM, change interval, cuts/min);
   - type slot (where the headline lives, size, ONE accent treatment) and the element kit (one card, one pill, one cursor).
3. **Write the Motion Design System** (one page): canvas · type slot + accent (palette and fonts from `knowledge/brand/brief.md`) · element kit · the 5–7 transitions (each used ≥ 2×) · easing family · camera · rhythm/beat grid · banned list (other palettes, second accent font, dark act, invented moves).
4. **Storyboard every beat** (table + a mockup frame per beat): time · VO words · the ONE hero · headline ≤ 6 words · move IN / DURING / OUT, each with its measured source (clip + frame/timestamp) · real UI/brand asset used · spine % running total. Put spine frames and current frames side by side.
5. **Show it to the founder (e.g. a local HTML page) and get a yes** on the system and the storyboard. Flag choices the user owns (keep/drop a hero, accent style) with a recommendation.
6. **Build once, lead-owned:** shared components first (Stage, Headline, Card, Pill, Cursor, Transition<T1..T7>), then beats in film order using only those. A beat that needs a new component/transition goes back to step 3 first.
7. **Verify for coherence, not just metrics:** a whole-film 1 fps sheet must read as one world (same canvas, same headline slot, same accent, same card) and every seam must be one of the named transitions. Then the filmfeel / pacing / originality gates.

## Anti-patterns (don't repeat)
- Replacing beats round by round with the "best donor for this beat".
- Two accent treatments (sans colour + serif italic) and several different logo reveals in one film.
- Headline position wandering (left/top/centre) between beats.
- A donor's whole stage coming along with its move (3D coins + moon + glass + pixel blocks in one film).
- Optimising filmfeel/originality numbers instead of the whole-film sheet.

## Never
- Code a beat before the system and storyboard are approved.
- Bring a donor's whole stage or palette along with its move.
- Publish anything. Gates: `shared/gates.md` (core).

## Shared knowledge
**Read first:** `knowledge/brand/brief.md`, the project's `STORY.md`. **Write after:** one dated line in `knowledge/log/<date>.md`. Paths from `shared/knowledge-tree.md` (core).

## Bootstrapped core
Ask `lessons` (theme `video`) before step 1. If it isn't connected, carry on with this method.
