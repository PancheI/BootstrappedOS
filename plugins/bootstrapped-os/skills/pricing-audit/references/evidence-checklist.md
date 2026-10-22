# Evidence checklist: 7 checks, in order

Run these on the founder's product before designing a model. The order matters: an earlier check can make later ones moot.

## How to quote the data
- **The market figures are in the Bootstrapped core, not in this file.** They come from the author's own dataset of public revenue listings plus walks of those products' pricing pages. Members get them from the core's `evidence` (see SKILL.md, Bootstrapped core).
- **Without the core:** run each check on the founder's product and back the recommendation with live precedents read from public pricing pages, dated. Never a market figure from memory.
- **Quote any figure with its n, its date and "correlation only".** Founders who show revenue are not all founders, and earners are older on average. Nothing here proves a cause.
- **These lines are about the market, not this founder.** Tag them `verified` as market facts; keep the founder's own numbers separate.
- **Pricing comparisons count only products that sell at least one paid plan.** Free products making nothing would inflate every gap.
- **Placement by stage:** `scripts/place-my-price.mjs` places the founder's price and habits against the benchmarks when given a benchmarks file (members; see `benchmarks.md`). Use its lines for checks 2, 4, 5 and 6. Without one it says "live precedents only" in one line: the normal path.
- **The data moves.** Never copy a number into an audit without its source line.

## The 7 checks

| # | Check on their product | What the data says | Recommend |
|---|---|---|---|
| 1 | **Can a buyer pay today?** Walk to the card field. | No market statistic; it's about this product only. | No working checkout: getting one is step 1 of the rollout, models come after. Not a failure (chicken and egg); see SKILL.md. |
| 2 | **Is there a yearly plan?** | Earners offer one more often than products at $0, and those with one stop earning less often after a sale. | Missing: "add a yearly plan" is the default first model. It raises the payment and holds the customer. |
| 3 | **Is the payment getting bigger or smaller?** With history: compare the first 3 paid months to the latest 3. Without: look for discounts, cheap tiers, "lifetime" on the page. | Products whose average payment rose grew revenue far more than flat or falling ones. | Never discount to win customers. Raise the payment: yearly, a higher plan, a paid add-on. |
| 4 | **Is the entry price very low** (under $10)? | The share making money is similar at every starting price, but earners under $10 make far less a month, and a bigger early payment goes with reaching a $1,000 month more often. Partly mechanical: bigger payments need fewer buyers. Say "predicts", never "causes". | "Cheap isn't buying you more customers; it caps the revenue." Show the break-even at a higher price. |
| 5 | **Recurring or one-time?** | Earners are more often on a subscription and less often one-time or lifetime only. | Suggest recurring only when the product is used repeatedly. Lifetime as an extra next to a subscription, never instead of one. |
| 6 | **Their $1,000 month** | Members: the core has how many charges a real $1,000 month took. | Arithmetic on their own price: "At $X, $1,000 a month = N paying customers." |
| 7 | **Are they on track?** Months since founding, and since the first sale, if known. | A first sale often takes months, and many who got one went on to a $1,000 month later. | Place them, then name one change. Slow is not dead: use it to calm or to push, never to judge. |

## Card up front on a trial
Earners ask for the card at trial start more often than products at $0, and run a trial more often. Pair with the external figure in `first-paid-customers.md` (card-required trials convert ~5x better).

## Only once they have paying customers (parking lot at $0)
Directions only; figures from the core for members, correlation only:
- More paid plans go with making money more often.
- The top plan is a few times the entry plan among money-makers. Check the ratio on the precedents you read live.
- Make the yearly discount a real deal, not "save 5%".
- An Enterprise / "talk to us" plan goes with making money more often, partly because these sell to businesses.
- Bigger revenue bands are mostly more customers, partly a higher price.

## Guardrails: advice the data says NOT to give
- **Don't remove a free plan by default.** Earners don't have one more often than products at $0: no gap in their favour. Exception: a free plan that does the whole job (an unlimited free plan next to a paid one).
- **Don't prescribe "launch on Product Hunt" or "grow your audience" as a pricing fix.** Earners list Product Hunt less often than products at $0. A bigger audience goes with more MRR, but audience can follow revenue as much as cause it, and it's not a pricing change.
- **Don't recommend discounts to get out of a slump.** Of those that fell below half their best month, a minority later beat it; the ones that grew had bigger payments, not cheaper ones.
- **Don't spend the audit on $9 vs $10.** Charm pricing showed no real difference (exploratory, small n).
- **Don't read a slump as failure.** Many paying small SaaS made less last month than half their best month.
- **Don't cite team plans as an earner habit.** No real gap. Recommend one only from the founder's own buyers.
- **Don't read channel lists as "what works".** Channels listed mostly reflect the product type (apps list app stores; B2B lists LinkedIn and SEO).
