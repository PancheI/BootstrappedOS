# Head of Analytics and CFO: numbers and money

**Five numbers every Monday and one change; one money review a month.** The Head of Analytics finds where people drop. The CFO checks what came in, what didn't, and what it cost. You pick the change.

## Set it up (15 minutes, once)
1. Connect your analytics (PostHog, Google Analytics or Plausible) and your payment tool, or be ready to paste a CSV export. No connector is needed to start.
2. Exclude yourself: your own visits, your team, and test payments. Ask: "Set up the exclusions for my analytics."
3. Add one question where people leave (cancel screen, closed checkout): "What stopped you?"

## Every Monday (15 minutes)
1. Type `/weekly-review`.

   **You should see** five numbers (visitors, leads, buyers, why people didn't buy, what broke), each with last week beside it and its source, the biggest drop, and ONE change for this week.
2. Make that one change. Next Monday's review judges it.

## On the 1st of the month (10 minutes)
1. Type `/money-review`.

   **You should see** revenue, customers won and lost, unpaid and failed payments, refunds, cancel reasons, costs, and one action, each with last month beside it. It changes nothing.

## Between Mondays (5 minutes)
Open your analytics, look at where people stop on your page, and ask Claude to improve the page from that. Small, daily, one thing at a time.

## What a good result looks like
```
Visitors 310 (290) · calls booked 14 (13) · buyers 3 (3)
Why not: 4 answers, 2 say "forgot the call" · 1 booking error
Biggest drop: booked → held (14 → 8)
Change: a reminder 2 hours before each call. Check next Monday: calls held.
```
Money: "Pricing page says 79, checkout charges 89. Fix the page by Friday."

## One memory
The numbers go in `knowledge/numbers.md`, newest on top, one dated line each. The morning brief, Content and Grants all read the same numbers, so there is one set of numbers everywhere.

## Avoid
- **Counting your own visits and test payments.** Exclude them first.
- **Changing five things at once.** One change a week, or you can't tell what worked.
- **Percentages on tiny numbers.** Under about 20, say the count.

**Files behind these roles:** `plugins/bootstrapped-os/agents/head-of-analytics.md`, `agents/cfo.md`, `skills/numbers/` (money in `references/money.md`), `commands/weekly-review.md`, `commands/money-review.md`
