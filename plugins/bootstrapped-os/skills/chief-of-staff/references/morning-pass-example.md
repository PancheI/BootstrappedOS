# Illustrative example

A made-up business. All names and numbers are invented to show the format.

---

## The business

**Ferro & Fig** - an online shop selling hand-made ceramic mugs. One founder. Shopify for orders and payments, Gmail for customers.

## What the queues held on Thursday morning

- Shopify: 6 new orders since yesterday. One payment marked "failed" (card declined). One order from Monday still not shipped.
- Gmail: 4 customer emails. One asks where her order is (it is the Monday order). One asks for a refund on a cracked mug, with a photo. Two are product questions.
- Yesterday's log: suggestion 2 ("draft reply to a wholesale enquiry") got a yes, but the draft was never saved.
- The courier's tracking site would not load.

## The message it wrote

```markdown
# Morning pass - Thu 15 Oct

**Looked at:** Shopify (6 new orders, 1 failed payment, 1 unshipped) · Gmail (4 new) · yesterday's log
**Skipped:** courier tracking - site did not load, so I can't confirm where the Monday order is

## Suggested
1. Draft wholesale reply - Studio Nord - because you allowed it yesterday and no draft was saved (log)
2. Draft "on its way today" reply - Mia - because her Monday order is unshipped (Shopify) and she asked (Gmail)
3. Draft card-declined email with a new payment link - order #2207 - because payment failed yesterday (Shopify)
4. Draft answers to 2 product questions - Tom, Lea - glaze is food-safe, sizes on product page
5. Draft refund reply for cracked mug - Sam - photo attached, order 9 days old (Shopify)

## Needs you
- Refund or replacement for Sam (item 5)? My pick: replacement, because the policy says 30 days for breakage and replacement keeps the sale.
- Ship Mia's order today? Only you can pack it.

Reply "go 1 3", "skip 2", or "go all".
These suggestions expire Sat 17 Oct, 08:00.
```

## What it did not do

- It did not say "Mia's order is on its way". It could not check tracking, so it said so in Skipped.
- It did not decide the refund. Refunds are money, so they go in Needs you.
- It put Mia in one suggestion, not two (she was in two queues).

## What the founder replied

"go 1 2 3 4. For 5 send a replacement, draft that."

## The log entry

```markdown
## 08:20 morning pass

### Suggested
1-5 as in the message.

### You said yes
- 1, 2, 3, 4 (founder: "go 1 2 3 4", 08:31)
- 5 changed: replacement instead of refund (founder, 08:31)

### You said no
- none

### Done
- 1, 2, 3, 4: drafts saved in Gmail, seen in Drafts 08:34; the founder sends them
- 5: replacement draft saved in Gmail

### Skipped sources
- courier tracking - site did not load
```

## Why this works

The founder read one message, typed one line, and every customer had a reply waiting in Drafts. The agent sent nothing; the founder pressed send.
