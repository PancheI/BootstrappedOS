# SPEC — <reference name> → <your product>

REF: `remake/ref/reference.mp4` — **<W×H>, <fps> fps, <N> frames (<seconds> s)**, audio <codec / rate>.
All frames: `remake/ref/full/fNNNN.jpg` (0-based). Audio: `remake/ref/audio.wav`. 1 fps sheets: `remake/ref/sheets/`.
Per-frame mean-abs-diff (192×108 gray): `remake/ref/diff.npy` (index i = change from frame i to i+1).
**ref/full is the truth; this prose is a guide.** Per-group detail lives in `remake/spec/G1..G4.md`, merged here at integration.

Rules: the video module's `RULES.md` (references, platform terms, never reuse assets). Your palette and fonts come from `knowledge/brand/brief.md`.

## Global
- Camera grammar: continuous camera or hard cuts? List the biggest moves with frames (whips, pushes, floods) from `diff.npy` spikes.
- Type: the font measured from crops, weights, headline ink colour, the ONE accent treatment.
- Background: canvas colour, grid geometry (spacing and phase from row/col mean profiles), how it moves with the camera.
- Cursor: style; measure tip paths per shot.

## Palette swap (one mapping, applied everywhere; preserve LIGHTNESS, not colour density)
| REF | role | OURS (`T.*` in core.tsx) |
|---|---|---|
| `#......` | ink | `#......` |
| `#......` | brand primary | `#......` (`T.brand`) |
| `#......` | brand secondary | `#......` (`T.brand2`) |

## Swaps
- Brand: REF logo → your real icon (`<Logo>`, `<Wordmark>` from `public/assets/brand/`). Never redraw it.
- Third-party UI (social platforms, payment pages): keep the layout, remove every brand name and logo.
- Faces: no real people. Use `<Avatar>` (your own AI portraits, or initials).
- Screens: where a real product screen fits, use your real crops `R(name)`.

## Story / copy map (REF on-screen or VO → OURS). Keep REF positions; absorb width deltas and report them.
| frames | REF | OURS |
|---|---|---|
| 0–120 | … | … |

## Groups (seams sit on REF transition spikes)
| group | frames | content |
|---|---|---|
| G1 | 0–… | … |
| G2 | …–… | … |
| G3 | …–… | … |
| G4 | …–<N-1> | … |

## Narration (REF word timings from Whisper, `remake/ref/words.json`) → OURS
| line | REF slot (s) | REF text | OURS text (similar syllable count) |
|---|---|---|---|
| 1 | 0.00–… | … | … |

VO: ElevenLabs voice `<your voice id>` (set `ELEVENLABS_VOICE_ID`), one continuous take cut per line. Measure REF pace (wpm). Each line must fit its slot with ≤ 8 % speed-up.

## Audio
- Music tempo per band (kick / snare / hats); watch for a 3/4 alias between the kick and hat reads.
- Loudness arc, drops and hit times, hard stop.
- **Never reuse REF music or voice.**

# Per-group shot detail (merged from remake/spec/G1..G4.md)
## G1
| shot | frames | what happens (measured) |
|---|---|---|
