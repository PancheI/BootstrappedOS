# Money (the monthly part of the numbers skill)

Money in, money out, one action a month. Works with any setup: Stripe, Paddle, Lemon Squeezy, PayPal, a shop platform, an invoicing tool, or exported CSVs.

Templates: money-templates.md
Worked example: money-example.md

## Monthly money review (`/money-review`)
1. **Pull from the payment tool**, not from notes. Last full month and the month before.
2. **List every income stream first** (plans, one-off sales, services, affiliate income), then every cost. Then compute.
3. **Fill the review table:** revenue, new customers, lost customers, unpaid/failed, refunds, top 5 costs. Each with last month next to it and its source.
4. **Run the cost audit:** every paid tool, what it costs, when it was last used, keep or cancel.
5. **Check the pricing page** against the checkout (checklist). Open both in a real browser.
6. **Pick ONE action** for the next 10 days. Write it as a proposal for the founder.

## Changing a price
1. Write the price-change plan from the template: today's live price, the new price, who it applies to, the date, what you'll watch.
2. Compare with what customers paid last month. Not with a theory.
3. Give one decided recommendation. Not "let's survey first".
4. The founder makes the change. Afterwards, open the page and a test checkout and confirm they match.
5. **Grep every copy of the price.** The author's price line lived in the app, the site pages, the blog, a page builder script and `llms.txt`; a change in one place left old numbers in four. Search for the old amounts and the old wording ("first month free", "today for the year") until nothing is left.
6. **Existing customers keep what they signed up for.** The author's retired plans stay in the config so their subscriptions keep resolving; only new customers see the new price.

## Getting paid
- **Failed payments and unpaid invoices:** the routine lives in the customer-emails skill (`skills/customer-emails/SKILL.md`, "Failed payment: day 0, 3, 7"). This review counts them and checks each one went out.
- **Access while a renewal is retried:** keep access a few days past the period end so a late renewal never locks anyone out (`skills/payments-agentaos/references/paid-access.md`).
- **Someone closed the checkout:** ask "What stopped you?" once, and save the answer where you can count it.

## Cancels
- One optional reason on the cancel form. Count them every month: too expensive / no time / no results yet / got what I needed / moved elsewhere / other.
- One save offer per reason (the author's: 20% off the next renewal; next month free; 3 more months under the guarantee), **one per customer ever, none in the first 30 days**, checked on the server, so cancelling to get a discount doesn't work.
- The founder applies any credit. The review reports offers made and kept.

## Refunds
- One written policy, linked next to the buy button and in the receipt. Apply it the same way every time; exceptions are the founder's call, logged.
- **An alternative the author uses: more time, not money back.** "Not worth more than you paid after 3 months? Tell me, and I'll add 3 months free." It keeps the customer and the cash; check it against consumer law where you sell (EU buyers keep their legal withdrawal right either way).
- The agent drafts the reply. The founder presses refund.

## Decision rules
- **The price on the page = the price charged.** Any mismatch is the action this month.
- **One main offer.** At most a monthly/yearly or small/large choice. Before adding a plan, name what it replaces.
- **Raise prices for new customers.** Keep existing customers on their price unless the founder decides otherwise.
- **The payment tool is the truth** for money facts. Don't keep a parallel spreadsheet of what it already holds.
- **Booked is not paid.** An invoice sent is not revenue until it is paid.
- **Small numbers** (under ~10 customers a month): report counts, skip percentages.

## Quality bar
- [ ] Every figure names its source and has last month next to it.
- [ ] All income streams and all costs listed before any profit sentence.
- [ ] Revenue says gross or net (after fees and refunds).
- [ ] Pricing page and checkout checked in a browser on the same day.
- [ ] Exactly one action, dated within the next 10 days.
- [ ] Nothing was changed. Everything is a proposal.

## Never
- Never move money, issue a refund, change a price, cancel a subscription or send an invoice without the founder's explicit go for that action.
- Never make a real payment from automation or a test. Use test mode.
- Never quote a price or fee from memory. Read it from the live page or the tool.
- Never promise a refund or a discount in a draft. "I've passed this to <founder>" is enough.
- Never lead with a projection ("on track for 10k").
- Never give a 90-day plan. Ten days, ordered by impact.

## Shared knowledge and core
Same as `SKILL.md`: the monthly review goes in `knowledge/numbers.md`; price, refund and policy decisions in `knowledge/decisions.md` after the founder's go.
