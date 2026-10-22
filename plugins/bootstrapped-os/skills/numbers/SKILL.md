---
name: numbers
description: Head of Analytics (with the CFO for money). The Monday note (five numbers vs last week, where people drop, why they did not buy, ONE change) and the monthly money review (revenue, failed payments, refunds, cancel reasons, costs, price page vs checkout, one action), with the author's counting rules (floors for small numbers, the payment tool beats analytics, capped lists are never counts, your own card is never a customer) and his replay routine. Works with PostHog, Google Analytics, Plausible, AgentaOS, Stripe, Shopify, Paddle or a CSV. Use for /weekly-review, /money-review, "how are we doing", "why did X drop", "why nobody buys", refunds, failed payments, unpaid invoices, costs.
---

# Numbers & Money

Five numbers and one change every Monday. One money review on the 1st. The agent pulls, counts and drafts the note; the founder picks the one change. **No connector?** Export last week's CSV from your analytics and payment tool into the project; that's enough on day 1.

**References:** `references/templates.md` (the Monday note, funnel, queries, replay review) · `references/money.md` (the monthly money review, price changes, refunds, cancels) · `references/money-templates.md` and `references/money-example.md` (its tables and a worked month).

## The five numbers (last 7 days, your own visits excluded)
1. **Visitors** and the top 3 places they came from.
2. **Leads:** sign-ups, trials, bookings, email subscribers.
3. **Buyers:** completed payments from the payment tool, plus revenue.
4. **Why people didn't buy:** their own words, from a question you asked.
5. **What broke:** errors, complaints, refunds, failed payments.

## The process
1. **Read last week's note.** What was the one change? Did it ship? Judge it today.
2. **Pull each number from its source**, source beside it. Re-run the query; never a number from memory or an old note.
3. **Exclude yourself and tests:** your IP or country, your team's emails, test-mode payments, **and any live payment from your own card or the name on your legal notice** (a test, never a customer).
4. **Fetch every page of a list** before you count it. A page is not a total; a list the tool marks recent-only or capped is never printed as a count.
5. **The funnel table:** visitors -> lead -> started checkout -> paid. Find the biggest drop.
6. **Read why:** answers to "What stopped you?", support emails, cancel reasons. Quote them.
7. **Watch the recordings at the leaking step** (PostHog, Clarity, Hotjar), starting with closed checkouts (`templates.md` §5).
8. **Pick ONE change** aimed at the leaking step: what should move, and how you'll check next Monday.
9. **Write the Monday note** from the template, at the top of `knowledge/numbers.md`. **Gate:** the founder picks whether the change happens.
10. **On the 1st:** the monthly money review (`references/money.md`).

## The author's counting rules
| Rule | Where it came from |
|---|---|
| **Opened, completed and live are three different numbers.** Say which one a figure counts. Payment tool wins for money; analytics is for the funnel. Report both when they differ, say which you used | A headline count of "payments" turned out to count checkouts opened, not payments made |
| **Check tracking before explaining a move** (a broken event, a bot spike, a test order). Check the sign-up event fires before you read channels | One event was undercounted for weeks by a tracking gap in his launch funnel |
| **Under 10 at a step: counts, no percentage. A comparison needs 5+ per side and 3+ events** | The floors his pricing dataset uses before any share is quoted |
| **A gap that flips when you re-read the same data is noise** | A free-tier gap changed direction after a re-read of the same data |
| **A number that moves during the day (30-day growth) is not quoted as a percentage** | Same dataset rule |
| **A stable total can hide two errors that cancel.** Check the reasons, not the sum | A review whose total didn't move had one line too high and one too low |
| **Count only what's yours, true today.** No imported users, no "seats left" you can't show | His own site: counts show only his own members |
| **Never compare different-length periods; never a business average in a sentence about one customer** | |

## Decision rules
- **Failed payments:** follow the customer-emails skill (`skills/customer-emails/SKILL.md`, "Failed payment: day 0, 3, 7"). This skill counts them; it doesn't repeat the routine.
- **Under ~50 real visitors a week:** the change is about getting visitors (outreach, posts, one channel). Don't redesign pages on noise.
- **No "why" answers yet:** this week's change is the question itself: "What stopped you?" after a closed checkout (save the answer on your server), in the cancel flow, or in a follow-up.
- **Closed checkouts in under ~5 seconds** usually mean the price line surprised them, not the price. The author's fix after replays: the exact amount the checkout will show sits next to every Join button, and no line can be read as both "pay now" and "free".
- **Last week's change can't be judged yet:** say so, keep it one more week, no second change on top.

## Quality bar
- [ ] Every number has last week beside it and names its source; own visits, team, tests and own-card payments excluded, and the note says how.
- [ ] Tagged verified / arithmetic / projection; the funnel shows counts at each step.
- [ ] "Why" uses real quotes. Exactly one change, aimed at the leaking step, with its check.
- [ ] Last week's change has a verdict: worked, didn't, or too early.

## Never
- Invent a number or fill a gap with an estimate. Write "not tracked".
- Lead with a projection.
- Suggest more than one change.
- Change tracking, pages or prices yourself. Propose; the founder decides.
- Move money, refund or cancel a subscription. The founder presses the button.

## Shared knowledge
**Read first:** `CLAUDE.md`, `knowledge/numbers.md` (last week), `knowledge/decisions.md` (last week's one change, prices and policies set). **Write after:** the five numbers and the one change at the top of `knowledge/numbers.md`; the monthly review there too; price, refund and policy decisions in `knowledge/decisions.md` after the founder's go. One dated line each. Never passwords or card numbers. Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Ask `recipes` (area `pricing`) before step 1 (the author's funnel and checkout plays) and `lessons` (theme `truth-and-numbers`, then `money-and-pricing`) at the decision rules. If it isn't connected, carry on with this method.
