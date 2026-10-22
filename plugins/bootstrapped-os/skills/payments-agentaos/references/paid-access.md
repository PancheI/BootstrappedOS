# Knowing who paid: how the author built it

His membership app (Next.js + Supabase, AgentaOS embedded checkout, Oct 2026) unlocks access from AgentaOS, never from the browser. Build this once there's a price live; the shape below survived real renewals, failures and cancels. Check names against the current `@agentaos/pay` types and the docs before writing it: integrations are verified live, not from memory.

## The shape
- **One column decides access:** `paid_until` on the member's row. Paid = `paid_until` in the future (a manual comp date can sit beside it; take the later).
- **One function writes it:** `syncSubscription(subscriptionId, userId?)`. It re-reads the subscription from AgentaOS and writes the same fields every time. The success page and every webhook call it. **Running it twice, or on events out of order, gives the same row.** The webhook body is a trigger, not the data.
- **The checkout carries your user id** in `metadata` (`checkouts.create` from the plan's link id). The first payment finds the member by that id; renewals find them by the stored subscription id.

## The rules in his sync

| Situation | What the sync writes | Why |
|---|---|---|
| `active` or `trialing` | `paid_until` = period end + **3 days** | A renewal that lands a few hours late never locks anyone out |
| `past_due` or `unpaid` | `paid_until` = period end + **10 days**; `payment_failed_at` set once | Access holds while the renewal is retried; most recoveries land within 10 days |
| No period end yet (a trial just started) | Period end = now + the plan's first period (31, 90, 365 or 366 days) | Otherwise a trial member has no access date |
| `canceled` | `paid_until` = `effectiveCancelDate` (or now) | Access runs to the end of what they paid for |
| Cancel scheduled | `cancel_at_period_end` stored; status stays `active` until the period ends | AgentaOS keeps a scheduled cancel "active". Show "Cancels <date>" and replace Cancel with Resume, or the member sees a live Cancel button on a cancelled plan |
| A founding plan paid | `is_founding = true` | The founding price stays theirs |
| Event's `livemode` differs from the key's mode | ignored | Test events never touch live members, and the reverse |

## The webhook route
- `src/app/api/webhooks/agentaos/route.ts` reads the **raw** body (`await req.text()`) and `x-agentaos-signature`, then `agentaos().webhooks.verify(body, signature, AGENTAOS_WEBHOOK_SECRET)`. A `WebhookVerificationError` answers 400. No secret or key set: 503.
- `checkout.session.completed`: take `metadata.subscriptionId` (and `metadata.userId` on the first payment); not a subscription, ignore.
- `subscription.created`, `.renewed`, `.updated`, `.canceled`, `.payment_failed`: `syncSubscription(event.data.id)`.
- Point the webhook at `<site>/api/webhooks/agentaos` in the dashboard; the signing secret goes in env vars. Test it with a test checkout, then once live.

## API gotchas he hit (Oct 2026; recheck, the API moves)

| Gotcha | What he did |
|---|---|
| No "get subscription by id" | Page `subscriptions.list({ limit: 100, offset })` until found or `hasMore` is false |
| Resuming a scheduled cancel | Check the current SDK and docs for a resume call. If there isn't one, the member resumes from the dashboard or by replying to you |
| Discount codes can't be made with an API key (403) | Owner session in the dashboard only; a code hits the first payment of a new subscription, never a renewal |
| Credits (a free month, 20% off) | Given in the dashboard as a balance on the customer; the next invoice uses it |
| No self-serve card update (8 Oct 2026) | The failed-payment email said "reply to this email". Check whether it exists now before building a workaround |
| Python's default user agent refused | `curl`, or set a `User-Agent` |
| Retired plans | Keep their link ids in the config so old subscriptions still map to a plan |

## The emails around money
Which emails, when and what they say belong to the customer-emails skill (failed payment: day 0, 3, 7; renewal reminders; the founder's welcome). The sync's part is only this:
- Each email is sent once, keyed in an email log (for example `subscription:failedAt:3`), so a rerun never sends twice.
- `payment_failed_at` from the sync is the clock for the failed-payment emails; `paid_until` and the plan interval are the clock for renewal reminders.
- The daily job's windows are 3 days wide, so a missed run catches up instead of skipping a reminder, and the key stops a second send.

## Keeping a member who cancels
One optional reason on the cancel form, one offer per reason: too expensive → 20% off the next renewal; no time → next month free; no results yet → the guarantee (3 more months free after 3 paid). **One offer per member, ever, and none in the first 30 days of a plan**, checked on the server both when shown and when taken, so nobody farms discounts by cancelling and resuming. The founder applies the credit in the dashboard.

## What not to build
- A table that copies payments, invoices or customers from AgentaOS. Read them when a page needs them (the invoice list with PDFs comes from the API).
- A scheduler that changes plans. Paid trials and period ends do it.
- Access from the browser's "payment succeeded" event. Only the signed webhook or the success page's server call, both through the sync.
