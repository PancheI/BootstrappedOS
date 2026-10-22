# Pre-show checklist

Tick every line before the founder sees the page. Paste the ticked list into `knowledge/checks/YYYY-MM-DD-home.md` with the screenshots.

## Copy
- [ ] The 3-second test was run on a zero-context reader; all five answers were right (what, who, what they get, price, button). Answers written down.
- [ ] Headline = the buyer's result, from the brief's one-liner or close to it.
- [ ] One main button; its words are a verb plus what they get; same words at the bottom.
- [ ] Price visible next to the button and in the pricing section, matching `pricing.json`.
- [ ] Each fact appears once per screen. No line explains the line above it.
- [ ] No AI tells, no buzzwords, no em dashes, no "free money", no competitor names.
- [ ] Everything on the old page (if any) is carried over or the founder agreed to cut it.

## Proof and truth
- [ ] 3 buyer quotes, exact, each link opened today and still showing that text.
- [ ] Every number has a source in `knowledge/pages/home.md`; rounded down; true today.
- [ ] No fake testimonials, logos, ratings, counts, countdowns or "as seen in".
- [ ] Legal page details (`legal` in `product.json`) are the founder's real ones, not samples.
- [ ] No `SAMPLE`, `example.com`, placeholder text or `_note` left anywhere on the page.

## Design
- [ ] Tokens and fonts match `knowledge/brand/brief.md`; neither font is a default.
- [ ] Contrast measured: body text 4.5:1 or more, large text 3:1 or more, button label 4.5:1 or more.
- [ ] The one idea is written down and visible in the hero.
- [ ] Hero visual is the working product, a real screenshot, a real photo, or nothing.
- [ ] The four "make it striking" items in `design-pass.md` §4 pass, and nothing from §5 (fake product, fake proof, dark patterns).

## In the browser (visible, not headless)
- [ ] `npm run build` passes.
- [ ] 1440 wide: first-screen and full-page screenshots taken and looked at.
- [ ] 390 wide: first-screen and full-page screenshots taken and looked at.
- [ ] Headline is 2 lines or fewer at both widths.
- [ ] Button visible on the first screen at 390; tap targets 44px or more.
- [ ] Nothing scrolls sideways; no overlaps; no text cut off.
- [ ] The main button works and lands where it says. Checkout opens in test mode only, if set up.
- [ ] The waitlist form shows its state (works, or says the service is missing) without errors.
- [ ] Console: no errors.
- [ ] Title, description and the social image match the new copy.

## Review
- [ ] Critic pass done (cold visitor, skimmer on phone, conversion, trust); findings applied or rejected with a reason.
- [ ] Shown to the founder as one finished page with screenshots, the design idea in one line, and a list of anything unverified.
