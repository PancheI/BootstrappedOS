# Market benchmarks

Aggregated pricing facts about small software that earns $0 to $5k+ a month, for placing a founder's price. The figures are not in the open version: they come from the Bootstrapped core for members. **The normal path is live precedents only:** `scripts/place-my-price.mjs` runs without them and says so in one line. A member's agent can save the core's answer as a JSON file and pass it with `--benchmarks <file>`. Audits quote any figure with its n, date and "correlation only".

## What they measure

| Block | What it measures |
|---|---|
| By stage ($0, under $200, $200-999, $1k-5k, $5k+) | What each subscriber pays; share with a yearly plan, a free tier, any trial, a card-up-front trial; subscription vs one-time or lifetime only; cheapest monthly list price |
| By entry price (under $10, $10-19, $20-49, $50+) | Share earning anything; monthly revenue of those earning |
| A $1,000 month | How many charges a real $1,000 month took |
| First sale | Time from founding to a first sale |
| First sale to a $1,000 month | Share that got there after a first sale, and how fast |
| Price changes after launch | Share of public launches that changed their entry price, or any pricing field, after launch day |

Sources: public revenue listings, walks of those products' public pricing pages, and public launch pages. Check a listing site's terms before you quote its data to customers; some ask for written permission.

## Privacy rules
1. **Aggregates only.** No name, URL or one company's revenue. Percentiles are of prices, not companies.
2. **n ≥ 20 per cell.** Smaller cells are suppressed.

## Members
Ask `bootstrapped-core` → `evidence` (topic: pricing) for the current figures, each with its n and date.
