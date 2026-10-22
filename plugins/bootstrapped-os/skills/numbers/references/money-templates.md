# Money templates

Copy, fill, adapt. Amounts in your own currency.

---

## 1. Monthly money review table

Add it at the top of `knowledge/numbers.md`, under a `## Money review - <month>` heading.

```markdown
# Money review - <month>

Source: <Stripe / Paddle / shop / invoicing tool / CSV>, pulled <date>.

| Line | This month | Last month | Note |
|---|---|---|---|
| Revenue, gross | | | |
| Fees (payment, platform) | | | |
| Refunds | | | <n refunds> |
| Revenue, net | | | arithmetic |
| New customers | | | |
| Lost customers (cancelled / not renewed) | | | top reason: |
| Unpaid / failed (open at month end) | | | <n customers, oldest days> |
| Costs, total | | | from cost audit |
| **Left over (net revenue - costs)** | | | arithmetic |

**Income streams counted:** <plans, one-off, services, other>
**One action (by <date, within 10 days>):** <action> - because <line in the table>.
**Not checked:** <anything you couldn't pull>
```

---

## 2. Pricing page checklist

Open the pricing page and the checkout side by side, on desktop and on a phone.

- [ ] Same price on the page, the checkout and the receipt (including currency).
- [ ] Tax shown the same way everywhere ("incl. tax" or "+ tax", never mixed).
- [ ] Monthly vs yearly: the yearly saving is arithmetic you can check.
- [ ] At most 2-3 options. One is clearly the main one.
- [ ] What you get is written as outcomes, in plain words, before the feature list.
- [ ] The refund policy is one click from the buy button.
- [ ] Buy button goes straight to checkout. No extra sign-up step unless needed.
- [ ] Every claim on the page is true today (counts, "used by", guarantees).
- [ ] Trial, discount or founding offer: the end date or condition is written down.
- [ ] Test checkout completed in test mode. No real card.

---

## 3. Price-change plan

```markdown
# Price change - <product/plan>

**Live today:** <price> (checked on <page URL>, <date>)
**Customers paid last month:** <range or average, from payment tool>
**New price:** <price>
**Applies to:** new customers from <date> / existing customers from <date> / existing stay on old price
**Why:** <one or two lines, from real numbers or customer words>
**What I'll watch for 30 days:** <checkout starts -> paid; "what stopped you?" answers mentioning price>
**What would make us go back:** <e.g. paid checkouts drop by half for 2 weeks in a row>
**Existing customers told:** <date, which email, drafted by customer-emails> (only if they are affected)

Founder: changes the price in <tool> -> the agent checks page, checkout and receipt match.
```

---

## 4. Refund policy template

Put it on its own page, link it next to the buy button and in the receipt email.

```markdown
## Refunds

**<14> days, no questions.** If it's not right for you, email <address> within <14> days of paying and we refund the full amount.

- **Subscriptions:** cancel any time in <where>. You keep access until the end of the period you paid for. We don't refund part-months after the <14> days.
- **Physical products:** return within <30> days, unused. Broken or wrong item? Send a photo and we replace it or refund it, your choice, and we pay the return.
- **Services / coaching:** full refund before the first session. After that, unused sessions are refunded.
- **How long:** refunds go back to the original payment method within <5-10> working days.

Questions: <address>.
```

Pick the lines that fit your business and delete the rest. Check that it matches local consumer law where you sell; this template is a starting point, not legal advice.

---

## 5. Failed-payment schedule

The schedule lives in the customer-emails skill (`skills/customer-emails/SKILL.md`, "Failed payment: day 0, 3, 7"). Use its emails; in the review, count failed payments open at month end and check each email went out once.

---

## 6. Cost audit table

```markdown
| Tool | What it does for us | Cost / month | Billed | Last used | Keep / cancel / downgrade | Why |
|---|---|---|---|---|---|---|
| | | | monthly / yearly (renews <date>) | | | |

**Total / month:** <sum> (arithmetic)
**Cancel candidates:** <tools not used in 30 days>
**Renewals in the next 60 days:** <tool - date - amount>
```

Sources: bank or card statement for the last 2 months, plus the tool's billing page. A tool nobody opened in 30 days is a cancel candidate. The founder cancels.
