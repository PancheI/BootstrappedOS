# The design pass

Copy first, then design. The design pass makes the page look like it was made for this buyer by a person, inside the brand from `knowledge/brand/brief.md`. You decide every visual call yourself and show one finished page.

## 1. Tokens and fonts (5 minutes, do it first)

`src/app/globals.css`, inside `@theme`. Keep the token names; the components use them.

| Token | From the brief | Note |
|---|---|---|
| `--color-ink` | Ink | text and borders |
| `--color-paper` | Paper | the ground |
| `--color-accent` | Accent | the one button, links, one highlighted word |
| `--color-accent-ink` | the label colour on the accent | must pass 4.5:1 on the accent |
| `--color-soft` | ink at a lighter step | secondary text; must still pass 4.5:1 on paper |
| `--color-line` | a light hairline | rules between sections |
| `--color-tint` | paper or near-paper | see "no tinted bands" below |

`src/app/layout.tsx`: swap the two `next/font/google` imports for the brief's fonts and keep the variable names, so nothing else changes:

```tsx
import { Display_Font, Body_Font } from "next/font/google"; // the brief's two fonts
const body = Body_Font({ subsets: ["latin"], variable: "--font-body" });
const head = Display_Font({ subsets: ["latin"], weight: ["700"], variable: "--font-head" });
```

Add the subsets the founder's languages need (`latin-ext`, `cyrillic`...). Run the contrast check from the brand brief on the final values.

## 2. One idea from the subject

Pick one idea that comes from the buyer's world, and let it shape the hero and at most one other section. Examples of the kind of thing (not to copy):
- A pricing tool: the price itself is the hero object, set big, with the break-even number next to it.
- A tool for electricians: the job sheet they fill in today, real, with the painful field circled.
- A payments service for makers abroad: the rejection email they got, then the payout landing.
- The founder's own result: a chart only if it is their real data, plotted from real points, as the proof block, not as decoration under the headline.

One idea, one gesture. If you're adding a second idea, you're decorating. Write the idea in one line in `knowledge/pages/home.md`.

## 3. The hero visual: real or nothing

Best to worst:
1. **The working product, embedded** (the `/product` route, or its first step, live in the hero).
2. **A real screenshot** of the product, taken in the visible browser at 2x, cropped to the part that shows the result. Save under `public/shots/`, with alt text that says what it shows.
3. **A real photo** of the founder or the buyer's real context, with permission.
4. **No visual.** Big type and white space. Always better than a fake.

## 4. Make it striking (required)

A page that is clean, correct and plain has failed: it reads as a document, and buyers scroll past documents. Every page needs all four:

- [ ] **One live thing in the hero, made from the product.** The buyer does the product's first step on the page and sees their own result: enter a due date and see your dated emails appear; paste a price and see your break-even; pick a file and see it converted. Real logic, works on a phone with a thumb, works without sign-up. This is the one thing people remember.
- [ ] **A direction from the subject, not a default.** Run the design kit's direction step (taste-skill) or decide one yourself from the buyer's world: their documents, tools, colours, places. Big colour fields, cards, tints, gradients, photography and type at poster size are all allowed when the direction calls for them. Write the direction in one line in `knowledge/pages/home.md`.
- [ ] **Real pictures of real things:** the live product, screenshots of it, the buyer's real world (open archives, the founder's own photos). At least one strong visual per screen on desktop.
- [ ] **A motion layer:** each section's parts enter in a short stagger as they come into view, every button and the live thing answer the press, and one signature move tied to the idea. Transform and opacity only; respect reduced motion.

## 5. Honest, always (these are the only bans)
- [ ] No fake product: no drawn dashboards, fake browser windows or skeleton lines pretending to be the app. Show the real thing or the live thing.
- [ ] No fake proof: no stock people, AI faces, logo walls of non-customers, invented counters, ratings or "as seen in".
- [ ] No dark patterns: no countdowns that reset, no fake scarcity, no hidden price.

## 6. Layout and type
- Headline at most 2 lines at 1440 and at 390. If it wraps to 3, cut words first.
- Body text 16px or more on phone. The button is visible on the first screen at 390. Nothing scrolls sideways. Tap targets 44px or more.
- Copy the shapes buyers know (nav top, price table, FAQ list). Differ in the direction and the live thing, not in where the button is.

## 7. Two readers

People scroll; AI tools summarise the markup. Keep both: real headings in order (one `h1`), alt text on every image, the FAQ in the HTML, no text hidden for search. The starter already writes title, description and the social image from `product.json`; check they match the new copy.
