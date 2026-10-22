# BRIEF — shot-group agents

You rebuild ONE contiguous frame range of the REF video as a frame-locked Remotion remake. Read `remake/SPEC.md` first (swap rules, palette, copy map, your group's frames).

## Acceptance bar
REF and remake stacked + frame-locked must show the same pose on every frame of your range:
- positions/sizes within **1 % of frame** (≈19 px horizontally, ≈11 px vertically); cuts/transitions on the **same frames** (0 frames off);
- camera moves, cursor tip, typing char-count, reveals on the same frames;
- differences only where the swap forces them (word widths, swapped copy, avatars instead of faces) — report every one.

## File rules
- Write ONLY `src/Remake/shots/<G>.tsx` (export `<G>_SHOTS: Shot[]`) and, if you need measured tracks, `src/Remake/tracks/<G>_*.json` (import them). Your spec notes go in `remake/spec/<G>.md`. Scratch work in `remake/work/<G>/`.
- Import helpers only from `../core` (`FPS W H T FONT E kf samples clamp01 lerp mix hash Camera GridBg Cursor Ripple Logo Wordmark Reveal Avatar R ICON`). **Never edit core.tsx, Remake.tsx, Root.tsx or another group's file.** If you need a core change, finish without it using a local `<G>_` helper and list the request in your report.
- Prefix every local helper/const with `<G>_`. Shots: `{ id: "<G>-<name>", f0, f1, render: (lf, F) => JSX }`; F is the global frame, lf = F − f0. Your shots together must cover your whole range with no gap; overlapping shots are allowed (later f0 renders on top).
- Pure functions of F only: no useState/useEffect timers, no Date, no Math.random (use `hash`), no CSS transitions/animations. `<Img>` from remotion for images.
- Keep the file compiling — the other three groups bundle the same tree. Run `npx tsc --noEmit -p . 2>&1 | grep Remake/shots/<G>` before every render.

## Measure, don't eyeball
Use numpy on `remake/ref/full/fNNNN.jpg`: ink bounding boxes (text rows/cols darker than bg), flood fills, colour masks, template matching (cv2 is not installed; use numpy/PIL — normalised cross-correlation on downscaled crops is fine). For every major move (camera scale/translate, card positions, cursor tip, text block bbox) extract a per-frame track and either fit keyframes (`kf`) or store the array and play it back with `samples(F, f0, arr)`. Font size from cap height (e.g. Poppins cap height ≈ 0.70 × font-size; measure your font's ratio).

## Verify loop (per shot)
`node remake/tools/render.mjs remake/work/<G> compare <frames>` — ≤15 frames per call, one render at a time. Then view `remake/work/<G>/compare.jpg` (REF | OURS | diff) and `compare_<F>.jpg` at full res. Check the first/last frame of each shot, every keyframe, and 2 frames into each transition. Iterate until within tolerance. Use `NOBUNDLE=1` only when you didn't change code. Never claim a shot matches without viewing REF|OURS for it.

## Seams
Your first frame must match the REF at that frame even though the previous group draws the frame before it — design your first shot to be correct standalone at f0 of your range. Same for your last frame.

## Report (final message)
Table: shot | frames | MATCHES / CLOSE / ROUGH | residual mean-abs-diff at checked frames | frames that would drift when stacked | spec errors found vs REF. Then: list of forced differences (with frames), core change requests, anything unfinished.

## More rules
- **Copy block:** keep every on-screen line in one `<G>_COPY` block of plain strings (`*…*` = accent), mapped onto REF's reveal frames through a `<G>_SLOTS` table. A copy change must be a one-line edit.
- **Motion self-check before you report:** render your range with `node remake/tools/render.mjs remake/work/<G> full f0 f1` (RemakeLocked) and run `python3 "${CLAUDE_PLUGIN_ROOT}/skills/video-reference-video-analysis/scripts/motion_sync.py" "remake/ref/full/f*.jpg" "remake/work/<G>/seq/*" --f0 <f0>`. Fix every `<<` window (frozen stretch, missing, too violent or mistimed whip), or explain it in your report.
- **Holds:** any hold (a still, readable beat) eases in and out over 8–10 frames. Never start a full-speed move out of a still frame.
- **Faces:** use `<Avatar seed faceIdx />` with gender matched to the name (`FACE_GENDER`) when portraits are installed; no real people.
- **Assets:** read every screenshot crop before using it. No other brands' names or logos, and follow the project's copy rules in SPEC.md.
