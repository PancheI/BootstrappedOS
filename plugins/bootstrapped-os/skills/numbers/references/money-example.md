# Illustrative example

A made-up business. All names and numbers are invented to show the format.

---

## The business

**Pixel & Pine** - a two-person design agency (one founder, one part-time designer). Sells website design as fixed packages, plus a monthly care plan. Invoices from an invoicing tool, card payments for the care plan through Stripe.

## What the founder asked

"/money-review for September. Also: should we raise the care plan price?"

## What the agent found

- Invoicing tool: 3 website packages invoiced in September. 2 paid, 1 sent on 25 Sep and not paid yet.
- Stripe: 18 care-plan customers at the start of the month, 17 at the end. 1 new, 2 cancelled. 1 card failed on 28 Sep.
- A second income stream the notes didn't mention: 2 one-off "extra page" add-ons, paid by card.
- Bank statement: 11 paid tools. 3 not opened in over 30 days.
- Pricing page says care plan "79 / month". Stripe charges 89 for customers who joined since July. Older customers pay 79.

## The review it wrote

```markdown
# Money review - September

Source: invoicing tool + Stripe, pulled 1 Oct. Bank statement for costs.

| Line | This month | Last month | Note |
|---|---|---|---|
| Revenue, gross (paid) | 7,773 | 6,540 | packages 6,000 (2 paid) · care 1,413 · add-ons 360 |
| Fees (payment) | 52 | 58 | Stripe only; packages paid by bank transfer |
| Refunds | 0 | 0 | |
| Revenue, net | 7,721 | 6,482 | arithmetic |
| New customers | 3 | 2 | 2 packages, 1 care plan |
| Lost customers | 2 | 0 | both care plan; reason: "site is finished, don't need changes" |
| Unpaid / failed | 2 | 1 | 1 invoice (3,000, 6 days), 1 card (89, 3 days) - not in revenue |
| Costs, total | 1,140 | 1,140 | from cost audit |
| **Left over** | 6,581 | 5,342 | arithmetic, paid money only |

**Income streams counted:** packages, care plan, add-ons
**One action (by 10 Oct):** fix the pricing page - it says 79, new customers are charged 89.
**Not checked:** the part-time designer's invoice for September (not received yet), so costs may be low.
```

Two things the agent did on purpose:
- The unpaid 3,000 invoice is **not** in revenue. Booked is not paid.
- It found the add-ons stream in Stripe before writing "left over". The founder's notes only listed packages and care plans.

## On the price question

```markdown
# Price change - care plan

**Live today:** page says 79; checkout charges 89 to customers since July (checked 1 Oct)
**Customers paid last month:** 10 at 79, 7 at 89 (Stripe)
**New price:** 89 on the page. No new increase.
**Applies to:** new customers. Existing 79 customers stay on 79.
**Why:** the page and the checkout disagree today. That must be fixed before any new increase. Both cancellations said "don't need changes", not "too expensive".
**What I'll watch for 30 days:** care-plan sign-ups after a package; cancel reasons.
**What would make us go back:** none needed; this matches what new customers already pay.
```

My recommendation: **don't raise it this month. Make the page say 89.** The bigger lever is the cancel reason: offer the care plan as "3 changes a month included", so finished sites still see the value. That is next month's action, not this one.

## Cost audit (part)

| Tool | What it does | Cost / month | Last used | Keep / cancel | Why |
|---|---|---|---|---|---|
| Stock photo site | photos for client sites | 29 | 52 days ago | cancel | free library covers recent projects |
| Second form builder | old contact form | 19 | 4 months ago | cancel | site builder has forms |
| Video call upgrade | longer client calls | 15 | 2 days ago | keep | used weekly |

## What the founder decided

- Changed the pricing page to 89 the same day. The agent opened the page and a test-mode checkout afterwards: both said 89.
- Cancelled the two unused tools (the founder did it).
- Sent the day-3 reminder for the failed card (drafted by customer-emails, checked against Stripe first).
- Held the invoice reminder until day 14: this client always pays late, but pays. Logged as an exception, with the reason.

## Why this was the right call

The founder asked about raising a price. The numbers said the price wasn't the problem: the page was wrong, and customers left because they stopped seeing value. One fix, this week, with a check that it worked.
