---
name: payments-agentaos
description: CFO. Takes the price picked in /pricing-audit to a working AgentaOS checkout - fee math at your real prices, plans in test mode, a test checkout end to end in a visible browser, the go-live check, a verification draft, then live plans after the founder verifies. AgentaOS is the merchant of record (VAT, receipts, payouts). Use for "set up payments", "checkout", "take money", "create the plans", "go live with payments", "AgentaOS", "test payment", "webhook", "who paid", "failed payment", "trial".
---

# Payments with AgentaOS

The founder has picked a price. This skill makes it payable, in a fixed order, and never moves real money. Everything up to step 6 runs in **test mode**. The agent prepares and checks; the founder verifies the account, creates live plans and makes the one real purchase.

**AgentaOS only, disclosed.** The author of this pack built AgentaOS; say so once when you first propose it. It is the merchant of record: it sells to the buyer, charges and files the VAT or sales tax, sends receipts and invoices, and pays the founder out. Founder already on another payment tool: this skill is not for them; don't argue.

**References:** `references/paid-access.md` (knowing who paid: the sync, grace days, cancel and resume, API gotchas) · `references/verification-draft.md` (what a review checks, and the draft answers).

## The process
1. **What it costs, at their real price.** Read https://docs.agentaos.ai/mor/pricing the same day and build the fee table at the founder's prices: fee per payment, its share, a year of it, and the net per sale. **Gate:** none; it's arithmetic.
2. **Pricing in one place.** The pick from `/pricing-audit` goes into `src/config/pricing.json` (details below).
3. **Plans in test mode.** `npm run plans` (dry run). **Gate:** the founder's "go", then `npm run plans -- --yes`.
4. **Test checkout, end to end, through to access**, in a visible browser (details below).
5. **Go-live check and verification.** `npm run golive` (read-only), then prepare `references/verification-draft.md`. **Gate:** the founder submits legal details and the payout account in the AgentaOS dashboard, themselves.
6. **Live plans.** Only when `npm run golive` says "Can go live: yes". **Gate:** the founder puts the live key in place and says go; then `npm run plans -- --yes --live`.
7. **One real purchase.** The founder buys their cheapest plan with their own card, checks the receipt and the dashboard, then refunds it. Never counted as a customer.

Live plans before a passing test checkout means the first real buyer finds the bug.

### The fee table (step 1)
Illustration only, at an assumed 4.5% + €0.50 per card sale. Redo it with the rates published today.

| Price | Fee per payment | Share | A year of it |
|---|---|---|---|
| €9 a month | €0.91 | 10.1% | 12 × €0.91 = €10.86 |
| €99 a year | €4.96 | 5.0% | €4.96 once |

What to say to the founder: **the fixed part of the fee is the expensive part of a small price; a yearly plan turns twelve of them into one.** Check payout fees too: a small payout loses a bigger share, so waiting for a larger balance can help.

**VAT inside or on top.** By default VAT is added at checkout, so an EU buyer sees more than the round number. Pricing **VAT-inclusive** keeps the round number as what the buyer pays; the founder then keeps the price minus the VAT inside it minus the fee. Confirm both on the first test payment's breakdown and put the net next to the price in `knowledge/decisions.md`.

### Pricing in one place (step 2)
- Read the pick from `knowledge/decisions.md`. None logged: stop, run `/pricing-audit`. Never choose a price yourself.
- Fill `src/config/pricing.json`: `currency`, and per plan `key`, `name`, `price` (major units, `9` for $9), `type` (`one_time` or `subscription`), `interval` (`month` / `year` / `null`), `trialDays`, `features`, `highlight`. Leave `linkId` empty. Replace the `SAMPLE` lines in `model` with the audit's reasoning and break-even.
- **Two currencies = two plans per price.** The buyer's region picks.
- **An intro price is a paid trial**, never a price override: an override charges the intro price on every renewal. Example: "€5 the first month, then €15" is a one-month trial at €5 on the €15 plan. `npm run plans` sends `trialDays`; for a trial price or VAT-inclusive pricing, check the current SDK docs. If the script doesn't send what you need, add it to the create call and show the founder the diff.
- **No schedulers.** Never build a job that switches someone's plan later. Use what AgentaOS does natively (paid trials, period ends).
- **Retire, never delete.** An old plan's id stays in the config so existing subscriptions still resolve.
- The landing page, the checkout route and `npm run plans` read only this file (`deploy/references/coding-rules.md`: "Prices come from one server file").

### Plans in test mode (step 3)
- The founder copies a **test** key (`sk_test_...`) into `.env.local` as `AGENTAOS_API_KEY`. Never into chat.
- `npm run plans` prints what it would create (name, amount, currency, type, interval, trial). A rerun skips what exists and writes the test ids (`linkId.test`).
- **Check you're in the right account.** One account per product; archive strays.
- Scripts in Python: the API has refused Python's default user agent. Use `curl` or set a `User-Agent`.

### Test checkout (step 4)
With the **browser-checker** agent, in a visible browser, on `npm run dev` or the preview deploy:
1. Home -> pricing -> each plan's button opens the checkout with the right name, price, currency, interval and trial line. **The amount the checkout shows is the amount next to the Join button**: people close a checkout with an amount they didn't expect within seconds.
2. Pay with the test payment method the test checkout offers. Never a real card or a wallet with real funds. A free trial shows "$0 due today" and no receipt; that's correct.
3. Lands on `/thanks` -> sign in with the same email -> `/app` shows the email and the plan. **The buyer has the thing the minute the payment succeeds.** No access path = not ready.
4. The AgentaOS dashboard (test mode) shows the payment; a subscription shows active or trialing.
5. Screenshot each step. Anything wrong: fix, then the whole path again.

### Go-live and live (steps 5-6)
- `npm run golive` prints: tried it, verification state, payout account, open questions, can go live. Show it as is. A payout account added only in test mode does not count for live.
- Legal name, registration number, tax country, address, product URL and payout account are the founder's legal and bank data. **They submit them in the dashboard.** No script, MCP call or agent submits them.
- Open questions: draft a short, true reply. **The founder answers in the dashboard**; an emailed answer may not reach the review.
- Live key: the founder puts `sk_live_...` in `.env.local` and in Vercel production (`npx vercel env add AGENTAOS_API_KEY production`, pasting it themselves). Preview keeps the test key. The app picks test or live ids by the key prefix. `npm run plans -- --yes --live` writes `linkId.live`; the script refuses a live key without `--live`. Then commit `pricing.json` and deploy (the deploy skill; the gates ask).

## Decision rules
- **No pick, no plans.** Pricing comes from `/pricing-audit` and the founder's logged go.
- **Test mode until step 6.** A `sk_live_` key before then: stop and say so.
- **AgentaOS is the source of truth** for payments and subscriptions. Copy only what a page needs (an access date), synced from the subscription itself (`references/paid-access.md`).
- **Prices change in one place.** Edit `pricing.json`, clear that plan's `linkId`, rerun `npm run plans`. Existing subscribers keep their plan unless the founder decides otherwise.
- **Failed payments and renewal emails** follow the customer-emails skill (failed payment: day 0, 3, 7).
- **The first customer** is the first payer who isn't the founder or the name on the legal notice.

## Quality bar
- [ ] The fee table at their prices, read the same day, with the net per sale.
- [ ] `pricing.json` matches the logged pick, no `SAMPLE` left; intro prices are paid trials.
- [ ] Dry run approved before `--yes`; test checkout passed for every plan through to access, with screenshots.
- [ ] `npm run golive` shown; what's waiting on the founder named plainly.
- [ ] Live plans only after "Can go live: yes" and the founder's go; one real purchase, refunded, logged, not counted.

## Never
- A real card, payment or purchase from automation.
- Submit verification, payout or legal data for the founder.
- Print, paste or commit a key. Env vars only.
- Set or change a price the founder didn't pick.
- Create live plans, refund, cancel or credit without the founder's go for that action (`shared/gates.md`).
- Name the payment processors behind AgentaOS in the founder's buyer-facing copy.

## Shared knowledge
**Read first:** `CLAUDE.md`, `knowledge/decisions.md` (the picked model, currency, company details), `knowledge/numbers.md` (costs for the break-even). **Write after:** one dated line each in `knowledge/decisions.md`: the fee and net per sale, plans created (test, live), go-live state, the smoke-test purchase (date, refunded). The verification draft in `knowledge/drafts/agentaos-verification.md`. Real revenue goes in `knowledge/numbers.md` from the dashboard, never estimated. Never keys, card numbers or bank details. Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Ask `recipes` (area `getting-paid`) before step 1 and `lessons` (theme `shipping-safely`, then `money-and-pricing`) at the decision rules. If it isn't connected, carry on with this method.
