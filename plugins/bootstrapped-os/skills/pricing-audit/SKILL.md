---
name: pricing-audit
description: CFO. A one-page pricing audit - signs up and walks your product as a buyer, roasts the offer ("why would anyone pay?") with verified facts and the buyer's ROI, designs 2-3 models each with a live precedent and a break-even on your costs, ranks them by money, picks one with a 10-day rollout, then passes a checker that refuses scores, projections in the headline and uplift percentages at $0. SaaS, digital products, services, $0-$1k a month. Use for /pricing-audit, "am I charging right", "what should I charge", "what to charge before anyone has paid", "should I add a yearly plan", "free tier or trial", "founding offer", "am I profitable", "why is nobody paying", "price my service".
---

# Pricing audit

The founder reads one page and knows two things: **what to change, and why it matters to their money.** The agent walks, researches and drafts; the founder decides the price. The author's words after an audit that carried a score: "no one cares in audit about scoring; founders don't have time and they just say: what do I have to change and why this is relevant."

**References:** `references/how-the-author-does-it.md` (real misses and the rule each one left; read before the first audit) · `references/evidence-checklist.md` (the 7 checks) · `references/benchmarks.md` (what the market benchmarks measure) · `references/first-paid-customers.md` (offer and route for the first payers, graded) · `references/models-and-break-even.md` (models, precedents, numbers, services) · `references/template.md` (the page).

**Scripts:** `node scripts/check-audit.mjs knowledge/checks/YYYY-MM-DD-pricing-audit.md --stage zero|paying` must print `OK` before the founder sees the page. `node scripts/place-my-price.mjs --price 19 --model subscription --interval month --mrr 0` places the price; without a benchmarks file it says "live precedents only", which is the normal path.

**In /start-from-zero (the pricing stage):** read `knowledge/positioning.md` first. Its roast ROI line is the price ceiling.

## The process
1. **Triage.** Nothing a buyer can use or pay for, and no sign of users: don't audit. Write the three steps that would make one worth doing. In doubt: not ready.
2. **Walk today's offer as a buyer, dated.** Homepage, pricing, sign-up, the product up to the paywall, checkout up to the card field. Sign up with the founder's test address (`you+buyer@...`), open the confirmation email, fill onboarding as the buyer. Stop only at a card, SMS, CAPTCHA (never bypass) or a third-party-only login. Type the email slowly and read it back. Never use "Forgot password" on an old account. Then one sentence: **where does a buyer get stuck?**
3. **Name the buyer from the homepage and service pages, quoted.** Never from blog posts or one case study.
4. **Today's model in one line:** the unit, the term, what's free, what isn't priced. Then ask whether the traffic suits another model (a free tool with buying-intent visitors may have an affiliate path nobody switched on).
5. **The roast** (format below).
6. **What buyers already pay:** 2+ named alternatives read live, dated, quoted. Doing nothing or DIY is always one. A funded competitor's price is shape, not a target.
7. **The 7 checks** (`evidence-checklist.md`) in order, then `place-my-price.mjs`. Quote its lines as printed. Back each check with live precedents from public pricing pages, dated, plus the core's figures when connected.
8. **Design 2-3 models** (`models-and-break-even.md`), each on three legs: the verified fact it answers, a named live precedent, a break-even. A missing leg cuts it. One model may be "keep what you have, add X". Turn a problem into the model (a fake "price goes up soon" countdown became "charge the higher price your countdown already shows").
9. **Rank by money** (first-12-month value, founder's currency, largest first). Different order? One clause why.
10. **Pick one, with a 10-day rollout** that keeps current customers whole: their price stays, no surprise charges.
11. **One starting offer and one route** (`first-paid-customers.md`), each graded, with the first action.
12. **Fill `template.md`, run the checker, then the independent review.** A fresh agent with only the page and the URL tries to falsify every price, quote and sum, and writes `<audit>-review.md`. Fix the page, then add "What changed after". A rewrite beyond the review's own fix list gets a new review. **Gate:** the founder decides the model; nothing on their site changes.

## The roast (format)
- **The question, on one verified fact:** "$39? Why would a team lead pay it when the free plan already includes every feature and refills every month?"
- **2-3 lines a buyer would throw back at the price,** each `verified` or `arithmetic`, no adjectives doing the work: "The free plan locks nothing." · "The best-known alternative costs $20 a month."
- **What they get back,** arithmetic on the founder's own claims, in the buyer's unit: "One client session, $300 by your own page, pays for 6 months of the plan."
- **A line claims only what it shows.** Compare the plan cards themselves before saying "that's the whole difference".
- **The loss must be the payer's.** "One avoided fine pays for 50 months" was wrong: the fine fell on the technician, not the team that pays.
- No verified basis for an ROI: say so. Roast the offer, never the founder.

## Decision rules
- **Defensible or cut.** Every figure is `verified` (seen live on the walk date), `arithmetic` (only on verified figures or the founder's own published claims) or `projection` (any assumed input). Headline, roast and any message: the first two only. The author, on a draft that led with a big projected number: "we are throwing numbers and assumptions before validating them rock solid."
- **Read only in the code, never seen in use = not `verified`.** Leave it out.
- **"How do you know?"** For every "X is real" claim, name the mechanism you checked, not the vendor (the proof a counter was real was the site's own network call returning the count, not the widget). Cut hedges (real, genuine, appears to) or add the check that removes them.
- **No checkout yet is not a failure.** Many have no price live because payments aren't set up. The moves before payments: the price on the page now ("launching soon" is fine), the same plan built in test mode with one test payment, real demand meanwhile (a waitlist showing the price, pre-orders, first customers invoiced by hand).
- **At $0:** one starting model plus one alternative, break-evens on real costs, **no percentage uplift** (the checker refuses "+30%"). Ladders, anchoring and expansion go under "Later, once you have paying customers".
- **With paying customers:** their numbers from the payment tool first. A live sale paid by the founder's card, or by the person on the legal notice, is a test, not a customer.
- **Before "raise the price",** check what's missing: a yearly plan, card up front on the trial, recurring billing on a product used repeatedly.
- **Models, not QA.** Bugs, stale promo pages and legal gaps: at most three lines under "Before you change the price", only if they block the model.
- **Yin-yang every model:** the risk as concrete as the upside, with its mechanism and one mitigation (see the risk table in `models-and-break-even.md`).
- **Today's offer only.** Old blog posts are history; today's pages decide.
- **Best for their business, and decide.** One recommendation against what's live, never "survey your users first".
- **Services sold as "let's talk":** fixed packages, one outcome, counted contents, one price; never "from" or "starting at" (`models-and-break-even.md` §7).
- **"Am I profitable?":** every income stream and every cost first, then compute. Booked is not paid.

## Quality bar
- [ ] `check-audit.mjs` prints OK; the review file ends with "What changed after".
- [ ] Opens with what they could sell. Builder, not inspector.
- [ ] Walk done by signing up, dated; where a buyer gets stuck; buyer quoted from the homepage.
- [ ] The roast in the format above; 2+ dated alternatives, doing nothing included.
- [ ] Every model: precedent, base/other/risk rows, "works if", a concrete risk.
- [ ] Ranked by money; one pick; 10 days (When | Do this, no effort estimates); one offer and one route, graded.

## Never
- A score, grade, "out of 100", bars or a formula.
- Buy, enter a card, guess a discount code, or log into someone else's account.
- An assumed conversion, renewal or churn rate as fact.
- Paid ads, paid directory slots or affiliates before the first paying customer.
- A number from memory, this file or an old audit (a remembered share went stale within hours of being written down).
- Figures from a private sample (products you reviewed, people who applied to you) quoted as market data. The checker refuses the tell-tale phrases.
- Change a price, a plan or a page. Propose; the founder decides.

## Shared knowledge
**Read first:** `CLAUDE.md`, `knowledge/decisions.md` (prices and policies set, who we sell to), `knowledge/numbers.md` (real revenue, customers, costs), `knowledge/customers.md` (what buyers said about price), `knowledge/positioning.md`. **Write after:** the page as `knowledge/checks/YYYY-MM-DD-pricing-audit.md` with its `-review.md` beside it; the picked model and its 10-day plan in `knowledge/decisions.md` only after the founder's go; buyer quotes about price in `knowledge/customers.md`. One dated line each. Never passwords or card numbers. Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Ask `recipes` (area `pricing`) before step 1 (the author's plays: open checkout on the price the card will see, preload the checkout, ask for payment after the first value) and `lessons` (theme `money-and-pricing`, then `truth-and-numbers`) at the decision rules. At step 7 ask `evidence` (topic: pricing) for the market benchmarks, each with its n and date. If it isn't connected, carry on with this method.
