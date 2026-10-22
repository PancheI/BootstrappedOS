# Creative Director (video module)

**A 30-second launch video from your real product screens, in one afternoon.** Story first, captions for muted viewing, 9:16 and 16:9. You record your voice (or pick an AI voice) and post it.

**What the module adds:** the `launch-video` skill (start here), the creative-director skill, and an advanced pipeline for polished films (Remotion for animation, ElevenLabs for voice). It needs the core plugin (`bootstrapped-os`). The core's Creative Director agent and the launch-video stage of `/start-from-zero` only work with this module installed.

## Set it up (2 minutes, once)
1. Install the core first ([INSTALL.md](../INSTALL.md)), then the module:
   ```
   claude plugin install bootstrapped-os-video@bootstrapped-os
   ```

   **You should see** `✔ Successfully installed plugin: bootstrapped-os-video@bootstrapped-os`.

## For each launch (one afternoon)
1. Type: "Use launch-video for <what I'm launching>."

   **You should see** a 4-line story (the problem, what changed, the proof, one ask), then a beat sheet: what is on screen and what is said, second by second.
2. Record your real product screens with your screen recorder. Cut the picture first, with no voice.
3. Add the voice, captions and music, then export 9:16 and 16:9.

## What a good result looks like
```
0-1 s    the problem moment, already moving       "I launched and nobody paid."
1-8 s    an empty dashboard                       one short line
8-12 s   your product appears                     "So I built..."
12-24 s  the real screen doing the one thing      what it does
24-27 s  one big real number                      the outcome
27-30 s  logo, one ask, URL                       the ask, warm
```

## One memory
It reads `knowledge/brand/brief.md` for your colours and fonts and `knowledge/numbers.md` for the one real number, and logs what it made in `knowledge/log/`.

## Avoid
- **Fake screens.** Record the real product; never a mock-up of it.
- **Text-heavy frames.** One thing per frame, 4-6 words at most.
- **Cropping 16:9 into vertical.** Recompose for 9:16 instead.

**Files behind this role:** `plugins/bootstrapped-os/agents/creative-director.md`, `plugins/bootstrapped-os-video/skills/launch-video/`
