# How the author does it

The author ran this audit on products that asked him for one (Sep-Oct 2026) and on his own membership. Each row below is a real miss, what he said about it, and the rule it left in this skill or the checker. Products are not named; quotes are his, lightly cleaned up.

## 1. Misses and the rule each one left

| What the draft did | The author's verdict | The rule now |
|---|---|---|
| Published a score out of 100 with category bars | "no one cares in audit about scoring; founders don't have time … what do I have to change and why this is relevant" | No score, grade or bars. The checker refuses "score", "grade", "out of 100" |
| A section that only listed what was broken on the page | "we need to provide a value on how to improve the product, not to critic it … help him design alternative models … supporting it with numbers" | 2-3 models with numbers are the audit. Critique is a 3-line footnote |
| Led with three checkout bugs (a trial that charged before converting, a stale promo page, docs naming another processor) | "we need to give them a realistic pricing and billing model assessment, not product testing" | Bugs only if they block the model, under "Before you change the price" |
| Advice anyone could give ("you're underpriced", "add a premium tier") | wanted "something they wouldn't think of … based on our analysis of their products, the simulation we've done" | Read their own surface for a pattern they haven't named: one product already metered several things a buyer uses without calling them credits. That's a repackaging model, not a new build |
| Risks written as "this could have downsides" | "yin-yang the recommendation with real simulation models … not hand-waving" | Every model's risk has a mechanism and a mitigation (credit anxiety; a top tier priced off the competitor's own tier ratio) |
| Hedged prose with no number to anchor on | "it's sooo abstract! and we are promising a blunt one" | Declarative sentences plus one concrete picture ("1 of 6 slots sold" style), never softer words |
| "The visitor count is real and public", because a third-party widget showed it | "HOW DO YOU KNOW" | Name the mechanism checked (the site's own API call returning the count), not the vendor |
| Only polished the founder's chosen mechanic (one hand-sold ad slot) | "not sure how this could be monetized and no relevant pricing model" | Ask first whether the traffic fits another model (affiliate, programmatic, packs) |
| Teaser led with a big projected revenue gain, built on an assumed price, an assumed sale a month and an assumed churn rate | "we are throwing numbers and assumptions before validating them rock solid"; "our suggestions need to be defensible" | Headline and roast carry only verified or arithmetic figures. Every suggestion has a fact, a precedent and a break-even, or it's cut |
| A roast line quoted a credit cost read in the app's code | (same review) | A figure seen only in code is not verified |
| A roast line said "that's the whole difference" between Free and Pro | (caught by the independent review) | Compare the plan cards themselves before claiming what differs |
| A short page that said "Two models. Names locked." with abstract tiles | "make the teasers self-containing like a hook, not half-baked info" | The page stands alone: who wrote it and why, two findings with proof, why pay, the first change, what's next |
| Version 1 of the audit page: many sections, many numbers | "v1 confusing … random numbers … doesn't flow"; of the model he copied: "I understand immediately, aha" | One noun and one number per idea, each section answering the one before: the question, your buyer, what they meet, what they compare you with, why they'd pay, the first change |
| Buyer drawn from 13 blog posts and one case study | "it is an SEO agency, what is this pest owner" | The buyer comes from the homepage and service pages, quoted |
| An agency selling quoted work got a "we can't help" note | "we do support digital services … give them an audit on what their pricing could be" | Services get fixed packages (models §7) |
| A package priced "starting at", with add-ons "picked at checkout" | "that's why you can have predefined packages … and add more add-ons" | One fixed base price, each add-on its own fixed item with its own buy button. A payment link carries one amount |
| A contradiction built from a blog post a month old | "his blog is 1 month old; many things have changed since then; look at today" | Today's pages decide. Old content is history |
| A yearly plan flagged as against a rule the author's own team had set | "of course it may, why not; don't restrict it yourselves" | Recommend what's best for their business |
| Ten agents of pricing research ending in "send price-survey emails first" | "you did all of this for few pricing emails" | Decide, compared with what's live; read real numbers at 30/60/90 days |
| The founder's own live card payment counted as the first customer | (caught on the platform read) | Check the payer against the founder and the legal-notice name |
| "One avoided fine pays for 50 months" | (caught by the independent review) | The ROI uses the payer's own loss |
| A market share hard-coded into the skill | stale within hours: the live read was different | Quote the data file or script output of the day, never a remembered number |
| A free-tier gap that flipped direction between two reads of the same data | | A gap that flips on a re-read is noise; don't build a model on it |
| A rewrite (new buyer, new menu) went out on the old version's review | "keep quality first" | Anything beyond the review's own fix list gets a fresh review |

## 2. What the checker refuses (`scripts/check-audit.mjs`)
The checker refuses a draft for each of these.

| Refused | Why |
|---|---|
| "score", "grade", "out of 100", "/100" | Founders want what to change, not a mark |
| An em dash | House style |
| "+NN%" or "NN% more" at $0 | No revenue to take a percentage of |
| "projection" or a % in the headline | The headline is a verified or arithmetic fact |
| A roast line without `(verified)` or `(arithmetic)`; no "What they get back" line | Defensible or cut |
| No dated walk, no "Where a buyer gets stuck" | The audit starts as a buyer |
| Fewer than 2 models; a model with no precedent row; fewer "works if" lines than models | Three legs per model |
| No "Ranked by money"; no When / Do this plan | Money order, 10 days |
| At $0, no "Later, once you have paying customers" | The parking lot keeps ladders out of a $0 audit |
| Paid ads, affiliates or featured slots recommended at $0 | None of the surveyed first customers came from ads (`first-paid-customers.md`) |
| Phrases that quote a private sample ("small products we reviewed", "non-earners", "with no revenue evidence") | A sample of who came to you is not the market |
| Unfilled `<placeholders>` | |
| No `<audit>-review.md`, or one without "What changed after", or with "pending fixes" | The author is the worst reviewer of their own file |

## 3. His own founding offer: the pattern
A membership for bootstrapped founders, priced in EUR and USD, VAT included, sold through a merchant of record. The founding offer went through several rounds in a few weeks. Each change came from what real visitors did, mostly seen in session replays. Ask the core's `evidence` (topic: pricing) for the rounds with dates.

| Round | What changed | Why |
|---|---|---|
| First | A low first month, then the regular monthly price | Built as a **paid trial** (trial days + a trial price). A per-payment price override would have charged the low price every month, forever |
| Next | Many plans: monthly, yearly and founding versions, in two currencies | Too many plans to explain. Cut back |
| Next | Founding became yearly by default, locked | Replays showed people closing a yearly checkout they didn't expect. Since then the amount sits next to every Join button, and a closed checkout asks "What stopped you?" |
| Next | One monthly and one yearly founding price, both locked while they stay | A second "today, then later" price was one more number to explain. The card shows the real charge big, the per-month figure small |
| Next | The button names the amount; a ROI multiplier and a seat counter came off | Every claim had to be true that day |
| Next | One price line, identical beside every Join | A visitor read a line as both "pay now" and "first month free" and closed the checkout in seconds |
| Close | The founding offer ended on its deadline; the regular price took its place; founding members kept theirs | A deadline is real only if it holds |

The guarantee is months, not money back: "Not worth more than you paid after 3 months? Tell me, and I'll add 3 months free."

**What carries over to your offer:** build an intro price as a paid trial, not a recurring discount; one price line, identical everywhere, with the amount the card will see; never two numbers that can be read as "pay now" and "free" at once; a real deadline that holds; the ROI line is one of the buyer's own customers ("One customer on your monthly plan pays it back"), not a multiplier.
