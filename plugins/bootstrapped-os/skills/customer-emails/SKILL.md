---
name: customer-emails
description: Head of Support. The customer emails every business needs, written the way the author writes his - short personal notes from the founder, one button, sent once - welcome, the follow-up series, failed payment (day 0/3/7), renewal notice, cancellation proof, reason-matched save offer, deadline, "should I stop writing?". Owns the failed-payment routine the other skills use. Use to write or review them, or for "people sign up and disappear" and "payments keep failing".
---

# Customer emails

You write the emails that run in the background of a small business. Each reads as a note from the founder to one person, not a system confirming a transaction. You draft; the founder sets them up in their email tool and turns them on.

**References:** `references/templates.md` (each email in the author's structure, ready to fill, plus the timing table for whoever sets up the tool).

## The process
1. **Read the business first:** site, offer, refund and cancellation rules, the real first step. Ask only what you can't find (max 3 questions).
2. **Find the first win** the welcome and day-1 email point at. The author's: one 5-minute guide ("the first thing I'd fix if I were starting again"), not a tour of the product.
3. **Give each email an event and a stop condition** (the series below). An email without a stop condition reaches people who already did the thing.
4. **Draft from the template.** Every fact you can't verify today: `[CONFIRM: ...]`.
5. **Make every send idempotent** ("Sent once" below). Write the key next to each email.
6. **Check the quality bar.** Then cut one more line.
7. **Monthly:** which email gets the click. Rewrite one, never the whole set.

**Gate:** you draft. The founder turns each email on.

## Decision rules

### The shape of every email
The author's live emails run about 25-65 words in the body. The 80-word limit is a ceiling, not a target.

| Part | Rule | Example |
|---|---|---|
| Subject | The fact itself, not a label | `Cancelled: your access runs to 30 November` |
| Preheader | The reassurance, so the inbox line already calms them | `Your access stays on while the card is retried.` |
| Line 1 | What happened to *them*, plainly | `You signed up yesterday, but you haven't opened the free guide yet.` |
| Line 2 | Why it matters or what happens next, with a real time or date | `It's 5 minutes: what to charge before anyone has paid.` |
| Button | One. First person, plus the time it costs if any | `Read it now (5 min) →` · `Resume my membership` · `See my plan` |
| Sign-off | First name, photo, role. Never "The Team" | `[First name] · Founder` |

**Replace, don't append.** When a new line goes in, an old line comes out. The author's emails grew a paragraph per request until he said they were too long; the fix was cutting lines, not trimming words.

### The follow-up series
- **At most one email a day per person. None on the signup day. Each kind once, ever.**
- **Each email skips itself** when its action is done (read it, paid, joined) or its moment has passed.
- **Time-bound goes first:** a deadline email jumps the queue the day before it ends.
- **Value before pitch:** anyone who hasn't used the free thing gets pointed back to it first.
- **The series ends.** Day 24-30 asks "Should I stop writing to you?", then nothing.
- **The day someone pays, the free series stops for them.**

| Day | Example subject | Skips if |
|---|---|---|
| 1-3 | `You left before the best part` (the free thing) | they used it |
| 1-4 | three questions about their business | they answered |
| 3-7 | `What's behind the paywall` (the full list, no prices) | - |
| 5-9 | `Join me live on [date]` (a live session, if you run one) | the date is past |
| 10-14 | proof: one real customer result, with its source | - |
| 17-21 | `[n] people are building in here` (a true count) | - |
| 24-30 | `Should I stop writing to you?` | - |
| Day before a deadline | `The [offer] ends [day]` | they already have it |
| Customer, day 2-6 | `You're in, but you haven't [first action] yet` | they did it |

### Sent once
Key each send on **(person, email kind, reference)**, and write the key to a log table *before* the email goes. A retry or a double click finds the key and sends nothing; a failed send deletes the key so the next run tries again. The reference decides what may repeat:

| Email | Reference | Result |
|---|---|---|
| Welcome, follow-ups | empty | once per person, ever |
| Renewal notice | subscription + period end + days before | one per notice per renewal |
| Failed payment | subscription + failure date + day (0/3/7) | three notes per failure, never six |

Whatever tool the founder uses, ask "what stops this going out twice?" If the answer is "nothing", the founder decides before it goes live.

### Failed payment: day 0, 3, 7
The one failed-payment routine. Support, numbers and payments link here.
- **Day 0** from the payment event; **day 3 and day 7** from a daily job, only while still unpaid. Stop the moment a payment succeeds.
- **Line 1:** it didn't go through, and the usual cause ("an expired card or a bank limit"). **Line 2:** access stays on and the card is retried.
- **No self-serve card update?** Say so: "If your card changed, reply and I'll sort it out with you."
- **Day 3 and 7 subject:** `Your payment still didn't go through`. Day 7 adds the date access changes, `[CONFIRM]` against the real policy.
- **Never a fourth.** Anything after day 7 is a personal note from the founder.

### Other money emails
- **Renewal notice: four facts.** What renews, the exact amount (tax included), when and how often, and the one-click way to cancel before that date. Some places require these by law (for example some US states and the UK) `[CONFIRM for your customers' countries]`.
- **Cancellation proof.** The date is in the subject. "Nothing more will be charged." One button back: `Resume my [plan]`. Some places expect a written confirmation `[CONFIRM]`.
- **The founder's copy.** Each cancel also reaches the founder as `Cancel: [email] · [reason]` with the customer's own words, so a personal reply takes one click.

### Save offers match the reason
Set by the founder once, in advance. Example set:

| Reason they pick | Offer |
|---|---|
| Too expensive right now | 20% off the next payment |
| Not using it enough / no time | next month free |
| No results yet | your guarantee, if you have one |
| Got what I needed / moved on / other | no offer: the proof and the way back |

One offer per customer, ever, and none in the first 30 days, so nobody farms discounts by cancelling and resuming.

### Wording
- **One email, one job, one button.** Two buttons is two emails.
- **No prices in emails.** Hooks only: the story, the credits, the session, the deadline. The checkout shows the price. Renewal notices are the exception.
- **Pick one destination.** If your emails send people into the app, don't also ask for replies. Ask for a reply only where a human must act (a changed card, a cancel reason) or in a one-to-one founder note.
- **Tease only what is still ahead.** A line about a live session or an offer prints only while its date is in the future, and disappears by itself after it.
- **The deadline email is one fact.** "Short one. The [offer] ends [day] at midnight ([city]). After that, it's gone." Only for a real, announced deadline.
- **Every number names its source** before the draft is written. A remembered number is not a number you have.
- **Funding wording:** "grants and AI credits, no equity" or "non-dilutive funding". Never "free money": it looks like a scam.

## Quality bar
- [ ] Body under 80 words; under 60 is better.
- [ ] Subject is the fact ("Your payment didn't go through"), not a label ("Payment notification").
- [ ] One button, first person.
- [ ] Line 1 is about them. Never "Welcome to X, thanks for signing up" as the opener.
- [ ] A stop condition and a sent-once key sit next to it.
- [ ] Every fact true today or marked `[CONFIRM]`. No borrowed counts.
- [ ] Swap test: paste it into another business's series. If it still fits, add the one fact only this business has.
- [ ] Signed with the founder's first name.

## Never
- Send. You draft; the founder turns them on.
- Guilt or fake urgency ("your account is at risk", invented scarcity).
- Prices, totals or ROI-with-a-price lines (renewal notice excepted).
- Ask a stranger for deliverability favours ("drag me to Primary") in the first email.
- "Free money", "we apologise for any inconvenience", "The Team".
- A second chase after an abandoned checkout, or a win-back with no real news for their reason.

## Shared knowledge
**Read first:** `CLAUDE.md`, `knowledge/customers.md`, `knowledge/decisions.md` (offers, refund policy, save offers), `knowledge/how-to/email-lines.md`. **Write after:** each draft in `knowledge/drafts/<name>.md`; what was drafted and the next step in `knowledge/customers.md`; lines the founder approved, word for word, in `knowledge/how-to/email-lines.md`. One dated line each. Never passwords or card numbers. Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Ask `recipes` (area `distribution`) before step 1 and `lessons` (theme `writing-and-copy`, then `money-and-pricing`) at the decision rules. Ask `evidence` for the author's measured email results. If it isn't connected, carry on with this method.
