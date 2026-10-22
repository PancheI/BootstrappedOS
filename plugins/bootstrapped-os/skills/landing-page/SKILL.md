---
name: landing-page
description: Landing page - build or adapt the launch starter's one-page site for the chosen wedge - outcome copy that passes the 3-second test, one button, real proof only, price visible - then a design pass in the brand, then a check in a real visible browser at desktop and phone with screenshots before the founder sees it. The landing page stage of /start-from-zero; needs the pricing pick from the pricing stage. Use for "build my landing page", "homepage", "hero", "rewrite my headline", "my page looks like a template", "make it look designed", "nobody understands my page", "page review".
---

# Landing page

You make one page a busy buyer understands in 3 seconds: what it is, who it's for, what they get, what it costs, one button. Then you make it look made for this buyer by a person, and check it in a real browser before the founder sees it.

The base is the launch starter (`bootstrapped-os-software/templates/launch-starter`): `src/app/page.tsx` (layout), `globals.css` (theme tokens), `layout.tsx` (fonts), `src/config/product.json` and `pricing.json` (every word and number). The starter is a neutral skeleton; the design pass is where it stops looking like one.

**Proof is real or absent:** linked buyer quotes, the founder's real numbers, a real screenshot or the working product. An empty slot beats a fake one.

**Quotes from public posts and reviews:** keep the words exact, but never print the person's name or handle, and never name the company they complain about. Attribute by role, place and month: "A solo founder, public review, Sept 2026". Keep the link in `knowledge/ideas/signals.md`, not on the page. A real customer's name goes on the page only with their written yes.

The founder approves the copy and the design; the agent builds, checks and shows.

**References:** `references/outcome-copy.md` (writing the copy, line by line) · `references/design-pass.md` (the design pass and the no-template list) · `references/checklist.md` (the pre-show checklist).

## The process
1. **Read first:** `knowledge/positioning.md`, `knowledge/brand/brief.md`, `knowledge/decisions.md`, `product.json`, `pricing.json`. No positioning card: run `positioning` first. No brief: run `brand-brief` first. No launch starter in the project: copy it (`cp -r`) into a new folder, never over existing work.
2. **Page brief, 5 lines,** in `knowledge/pages/home.md`: the one action, who it's for, the proof true today, what it must not feel like, the honest risk. Replacing a page? List everything on the old one (proof, links, facts, FAQ, tools) and carry it all over unless the founder says cut.
3. **Copy pass** (`outcome-copy.md`): headline = the buyer's result, 2 lines max; one line on who, what, what they get; one button (a verb plus what they get) with the price beside it. Then the 3 linked quotes, 3 steps, pricing, FAQ, the founder line. Every number sourced in the page brief.
4. **3-second test:** show only the first screen's text to a zero-context reader (a fresh agent works). They answer what, who, what I get, what it costs, what I click. Any miss is fix #1. Short and cryptic fails as hard as long.
5. **Design pass** (`design-pass.md`): brand tokens into `globals.css` `@theme`, the two fonts into `layout.tsx`. **A direction from the subject** (the buyer's world, moment or tool) shapes the whole page, and **the hero holds the live thing**: the buyer does the product's first step and sees their own result. Then real visuals and the motion layer (`design-pass.md` §4). Only the honesty bans are hard limits. Make **3 design options: bold, middle, safe**, each a finished first screen in the brand. Pick one and say why in a line.
6. **Build and run:** `npm run build` passes, then `npm run dev`.
7. **Visible browser check** (`/check-live` or `browser-checker`) at 1440 and 390, plus 768 if the layout shifts. Screenshot first screen and full page at each. Look for a 3-line headline, a button below the fold, sideways scroll, phone text under 16px, overlaps, console errors. Click the button through. Fix, re-shoot.
8. **Critic pass on the screenshots:** a cold visitor, a skimmer on a phone, a conversion reader, a trust reader. Findings are hypotheses; apply those that hold. Brand rules beat critic advice.
9. **Show the founder** the three first screens (bold, middle, safe) with your pick, then the picked page in full: both first-screen screenshots, the full phone page, the design idea in one line, anything unverified. Change only what they name. **Gate:** "go" means build and show it locally; nothing is public until the founder says "ship" or "deploy" (`shared/gates.md`).
10. **Hand over:** "go to deploy?"

### The design kit (the author's own order)
**Default pass (about a third of the cost):** taste-skill direction + its inspector, copywriting, and one cold reviewer. **Full pass** (every step below, about $30 of AI in the test run): when the founder asks for "polish", or before a public launch.
These are free third-party skills, not part of this pack; install them once (`INSTALL.md`, "Design kit"). At step 5, check which are installed and run every one that is, in this order. Say which ran and which were missing.
1. **taste-skill** (design-taste-frontend): deal a direction from the subject, then its linter and inspector on the built page; fix every FAIL.
2. **impeccable**: the critique and audit pass on the page; fix what holds up against the brand brief.
3. **frontend-design** (Anthropic): the craft check on type, spacing and layout.
4. **copywriting** and **page-cro**: a line-by-line copy pass and a conversion pass on the first screen.
5. **Motion, last and small:** at most one entrance per section and press feedback on the button, using a motion skill if installed (the author uses one built on Emil Kowalski's public animation guidance; install your own from its author). Respect reduced motion.
6. **Two reviewers who didn't build it:** two fresh agents, each scoring the screenshots cold. Apply what both agree on.
If the founder's Claude can publish **artifacts**, publish the screenshots and the one-line design idea as a private artifact page for the founder to review and share.

The headline is the positioning card's promise and outcome; the proof answers its roast.

### The hero, in five hard rules (check these before anything else)
1. **Sell the outcome, never the feature.** The headline is what the buyer gets in money, time or relief, in their words: "Get your €6,850 paid", not "Five ready-to-send emails". Features go below, as proof of how.
2. **The hook becomes the visitor's own number.** When the live thing has an input, the headline changes with it: type 6,850 and the headline reads "Your agency owes you €6,850. 13 days late." One big real number, theirs.
3. **The button is the outcome with their number, not the feature.** "Claim my €621.62 →", not "Get my dated emails" or "Start my sequence". The price sits right beside it.
4. **One moment that moves on the first screen:** the number counting to its new value, a stamp landing, the result appearing as they type. A still first screen fails, however correct.
5. **Two inputs, at most, to the first result.** Every extra field before the "oh" loses people. Ask for the rest after they've seen their result.

| The author's line | His verdict | Why |
|---|---|---|
| "Get paid by clients worldwide. Keep almost all of it." | approved | the buyer's result, plain |
| "Turn users into paying customers." | kept as the promise | the buyer's result in five words |
| "Why isn't anyone paying?" + "Find out why" | "it hooks people" | the buyer's own question |
| "One platform, from first invoice to payout" | rejected, vague | describes the product |
| "AI finds your pricing fix" | "is this really clear to people?" | feature + jargon |
| "The business half of your startup, done with you" | "I need to understand what you're doing in 3 seconds" | clever, not an outcome |

Every section headline follows rule 1 too: "Paid this month, not in 90 days" over "How it works".

## Decision rules
- **No product yet:** the hero shows the first working version from `/product`, or nothing. A waitlist is honest; a drawn dashboard is not.
- **No real numbers yet:** proof is the 3 linked quotes and the founder's one true line. No counters, no "trusted by".
- **Real numbers:** use them, rounded down, sourced, true today.
- **Pricing not picked yet:** show the idea brief's test price as the launch price. Never hide the price to get the click.
- **Existing brand:** keep palette, fonts and buttons. Invent the story and layout, not a new look.
- **Asked for a bold rework:** do all of it in one round, starting with the hero.
- **Asked to tweak one thing:** change that thing. List anything else you'd change after, don't do it.
- **Live page, under ~50 real visitors a week:** don't redesign; fix getting people there (`launch`).
- **Headline won't fit 2 lines at 390px:** cut words before shrinking type.
- **The page is live:** read PostHog every day (where people stop scrolling, what they click, where they leave) and propose one change at a time. The author improves his own pages this way.
- **A question people type into search or an AI chat:** use their exact question as the H1, answer it in the first lines with a date, and add a table.
- **The headline number must be true for the entry plan.** "From 1%" when the entry plan was 1.5% read as bait-and-switch.
- **Never build the hero hook on a supplier's limitation or name the platform you depend on.** Name the access, not the gatekeeper.
- **For lead capture, a short tap-quiz ("where are you stuck?") beat on-site tools** on the author's site, by far. Ask the core's `evidence` for his numbers.

## Quality bar (every page)
- [ ] First screen answers what, who, what you get, price, and the button, at 1440 and at 390.
- [ ] Headline is the buyer's outcome (money, time, relief), not a feature; 2 lines max on both widths.
- [ ] With a live thing: the headline shows the visitor's own number, and the first result needs at most 2 inputs.
- [ ] The button states the outcome with their number; one element moves on the first screen.
- [ ] One main button, repeated at most at the bottom with the same words.
- [ ] Every proof item is linked or sourced, true today.
- [ ] Brand tokens and fonts from the brief; contrast passes (body 4.5:1, large 3:1).
- [ ] All four "make it striking" items in `design-pass.md` §4, and nothing from §5.
- [ ] The hero has the live thing: a buyer gets their own result on the page, on a phone, without signing up.
- [ ] Hero visual is a real capture or the working product, or there is none.
- [ ] Build passes; the button works; no console errors.
- [ ] Screenshots at both widths were taken in a visible browser and looked at.
- [ ] Every item in `checklist.md` ticked.

## Never
- A stranger's name, handle or photo next to their quote, or the name of a company they complain about.
- Fake testimonials, logos, ratings, user counts, "as seen in", live-visitor pop-ups or countdowns that reset.
- Drawn product mockups or fake browser frames pretending to be the app, stock photos posing as customers.
- A plain page: headline, paragraphs and lists with no live thing, no strong visual and no motion. That is a draft, not a page.
- "Free money", "revolutionary", "all-in-one", "AI-powered" as the promise, or a competitor's name in the copy.
- Ask the founder to pick palettes or fonts, or to design. Show three finished options (bold, middle, safe) with your pick and the reason.
- Deploy, push, buy a domain or connect a live payment key. Those are later stages with their own "go".
- Show the founder a page you haven't screenshotted at both widths yourself.

## Shared knowledge
**Read first:** `CLAUDE.md`, `knowledge/positioning.md`, `knowledge/brand/brief.md`, `knowledge/decisions.md`, `knowledge/pages/home.md` if it exists, `knowledge/rules.md`, `knowledge/checks/` (the last browser check). **Write after:** the page brief in `knowledge/pages/home.md`; dated lines in `knowledge/decisions.md` for the headline, the design idea and anything rejected (in the founder's words); the check with screenshots in `knowledge/checks/<date>-home.md`; any rule the founder states in `knowledge/rules.md`. Never passwords, keys or card numbers. Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Ask `recipes` (area `seo`) before step 1 and `lessons` (theme `design-and-pages`, then `writing-and-copy`) at the decision rules. If it isn't connected, carry on with this method.
