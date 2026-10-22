# The one-page pricing audit

Save as `knowledge/checks/YYYY-MM-DD-pricing-audit.md`. One page. Each finding said once. Tag every figure: `verified`, `arithmetic` or `projection`. Delete any section that would be empty rather than padding it.

```markdown
# <Product>: <one line on what they could sell, built from a verified fact>

<Two sentences: what the buyer meets today, and the direction of the change. No digit here is a recommendation.>

## Who buys
<One line: the person who hands over money, quoted from your own pages.>

## Where you are today
| Your number | What it means | Source, date | Tag |
|---|---|---|---|
| <price / plan> | | <page, date> | verified |
| <revenue / customers, or "not public"> | | <payment tool / page> | verified |
| <costs per month, if known> | | numbers.md | verified |

## What a buyer sees
<Date, time (UTC), the path walked, the wall it stopped at. Nothing bought.>
**Where a buyer gets stuck:** <one sentence>

## Why would anyone pay?
**<Price>? Why would <buyer> pay it, when <one verified fact>?**
- <a fact a buyer would throw back at the price, under 12 words> (verified)
- <another, e.g. the alternative's price next to theirs> (verified)
- **What they get back:** <arithmetic in the buyer's unit, on the founder's own claims> (arithmetic) <or: no verified basis yet>

**What else gets them that:** <alternative 1, price, date> · <alternative 2> · doing nothing / DIY

## Ways to charge for it
| | A · <name> (recommended) | B · <name> |
|---|---|---|
| The offer | | |
| Who already charges this way | <named product, quote, date> | |
| Why it fits you | | |
| Why it might not | | |

## The numbers (projections, not forecasts)
| Model | Base | Other | Risk | Inputs, and works if |
|---|---|---|---|---|
| A | | | | |
| B | | | | |

- Your $1,000 month: <$1,000 ÷ price = N customers> (arithmetic). Market: <line, n, source, date, correlation only>.
- The assumption the ranking hangs on: <one sentence>.

## What we'd do
Ranked by money: A <value>, B <value>. Start with <X> because <one clause>.

| When | Do this |
|---|---|
| Days 1-2 | |
| Days 3-4 | |
| Days 5-10 | <the route's first action: who, how many, what to offer (grade)> |

**Starting offer:** <row from first-paid-customers.md> (<grade>). **Route:** <row> (<grade>).
Current customers keep their price.

**Before you change the price:** <at most three lines, only if they block the model>

**Later, once you have paying customers:** <parking lot>

---
Read <date>: <pages walked>, <precedent pages>, <data sources with dates>. A draft: you decide.
```

## Before handing back
1. `node scripts/check-audit.mjs knowledge/checks/YYYY-MM-DD-pricing-audit.md --stage zero` (or `--stage paying`). Fix until it prints OK.
2. **Independent review.** Dispatch a fresh agent with only the page path, the product URL and this brief: "You did not write this. Try to falsify it. Re-fetch every competitor and precedent price from its own page and confirm the quote and date. Re-read the founder's prices and terms live. Recompute every row from its stated inputs. Flag any assumed rate shown as fact, any model without a precedent, any roast line that claims more than it shows, any ROI whose loss falls on someone other than the payer. Return CONFIRMED or a numbered list with the line and the evidence. Do not rewrite the page."
3. Save its answer as `knowledge/checks/YYYY-MM-DD-pricing-audit-review.md`. Fix the page (never argue in chat), then add a `## What changed after` section listing each fix. Run the checker again.
4. Changed more than the review asked for? Run a new review.
