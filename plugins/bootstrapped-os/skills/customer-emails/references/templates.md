# Customer email templates

Each one is built the way the author builds his: subject = the fact, preheader = the reassurance, two or three short lines, one button, first name. Fill the [brackets]. `[CONFIRM]` = a fact the founder must check. Swap "signup" for "order" or "booking" if you sell products or services.

---

## 1. Welcome (first sign-in)
**Subject:** `Welcome to [business]` · **Preheader:** `[the result your story proves, in under 10 words]`
```
[One line: what you help people do, and how (not a course, hands-on...).]
I'm [founder]. [One true line of proof, with a link to where it's public.]
The first thing to do: [the one 5-minute step that gets a result].

[Button: Start with [step] ([n] min) →]
[Founder] · [role]
```
The author's proof line links to the public article that featured him. A claim with no public source does not go here.

## 2. Day 1-3: back to the free thing
**Subject:** `You left before the best part` · **Stop if:** they used it.
```
Hi, you signed up yesterday, but you haven't [opened the free thing] yet.
It's [n] minutes: [what it gets them]. It's the first thing I'd fix if I were starting again.

[Button: Read it now ([n] min) →]
[Founder]
```

## 3. Day 3-7: what's inside (no prices)
**Subject:** `What's behind the paywall` · **Preheader:** `The full list, no fluff.`
```
Hi, here's everything inside:
→ [item 1: funding or money in, first]
→ [item 2: time saved]
→ [item 3: more customers]
[Your guarantee, one line, if you have one.]

[Button: See membership →]
[Founder]
```
Order the list the way the author does: grants and credits, then time saved, then revenue.

## 4. The day before a deadline
**Subject:** `The [offer] ends [day]` · **Preheader:** `Last chance: [day] at midnight.` · **Stop if:** they already have it.
```
Hi, short one. The [offer] ends [day] at midnight ([city]). After that, it's gone for good.
[At most one line: what they'd miss.]

[Button: Claim my [spot / offer] →]
[Founder]
```
Only if the deadline is real and already announced. Never move a deadline you printed.

## 5. Failed payment, day 0 (from the payment event)
**Subject:** `Your payment didn't go through` · **Preheader:** `Your access stays on while the card is retried.`
```
Hi,
The renewal of your [plan] didn't go through. Usually it's an expired card or a bank limit.
Your access stays on for now, and the card is tried again automatically over the next days.
[If there's no self-serve card update:] If your card changed, reply and I'll sort it out with you.

[Button: See my plan / Update my card]
[Founder]
```
Day 3 and day 7: same body, new subject. The routine and its stop rule: `../SKILL.md`, decision rule "Failed payment: day 0, 3, 7".

## 6. Renewal notice (the 4 facts)
**Subject:** `Your [plan] renews on [date]` · **Preheader:** `[amount] on [date]. Cancel any time before then.`
```
Hi,
A heads-up: your [plan] renews on [date], in [n] days.
You'll be charged [amount], [tax] included, then every [month/year] until you cancel.
Nothing to do if you're staying.

[Button: See my plan]
Not for you anymore? [Cancel in one click] before [date] and nothing more is charged.
[Founder]
```

## 7. Cancellation proof
**Subject:** `Cancelled: your access runs to [date]` · **Preheader:** `Nothing more will be charged. You keep access until [date].`
```
Hi,
Your [plan] is cancelled. You keep everything until [date], and nothing more will be charged.
Changed your mind before then? One click and nothing changes.

[Button: Resume my [plan]]
[Founder]
```
At the same time, to the founder: `Cancel: [email] · [reason]`, their words quoted, a link to reply.

## 8. Save offer applied
**Subject:** `Done: your offer is on your account`
```
Hi,
[The offer, stated as done: "Your plan carries on, and your next month is on us."]
Glad you're staying. [One line about the next real thing they'll get.]

[Button: See my plan]
[Founder]
```
Send it only after the founder applied the credit and marked it done. Offers by reason: `../SKILL.md`, "Save offers match the reason".

## 9. Member hasn't joined in (day 2-6 after paying)
**Subject:** `You're a member, but you haven't met anyone yet` · **Stop if:** they posted.
```
Hi, you haven't said hi in [the community place] yet.
One minute, in [the intro channel]: who you are, what you build, your one blocker.

[Button: Say hi →]
[Founder]
```

## 10. The last one in the series (day 24-30)
**Subject:** `Should I stop writing to you?` · **Preheader:** `My last note in this series.`
```
Hi, this is my last note in this series. I don't want to clutter your inbox.
If the timing isn't right, no hard feelings: your free account stays, and [the free thing] is yours.
If it is, everything I know is inside: [3 items, plain].

[Button: See membership →]
[Founder]
```

## 11. One-to-one founder note (to a customer you know)
3-5 lines plus an optional PS: **one fact from their account, one observation, one question that invites a reply, an offer to help.** No bullets, no headings.
```
Hi [name], [one fact from their account, with dates].
[One observation: what that fact usually means.]
So how is [the thing that decides their next step] going? Is there anything I can do to help?
PS. [one optional line: a new thing that fits them]
[Founder]
```
Long versions with an insight paragraph read as a report. The short one reads as a person.

---

## Timing, stop rules and sent-once keys (give this to whoever sets up the tool)

| Email | Trigger | When | Stop when | Sent-once key |
|---|---|---|---|---|
| Welcome | first sign-in | 0 | - | person + welcome |
| Back to the free thing | signup | day 1-3 | they used it | person + kind |
| What's inside | signup | day 3-7 | they paid | person + kind |
| Deadline | offer end date | day before | they have it | person + kind |
| Failed payment | payment failed | 0 / 3 / 7 | payment succeeds | subscription + failure date + day |
| Renewal notice | period end | [n] days before | they cancelled | subscription + period end + n |
| Cancellation proof | cancelled | 0 | - | subscription + period end |
| Member intro nudge | first payment | day 2-6 | they posted | person + kind |
| Last one | signup | day 24-30 | they paid | person + kind |

Global rules: one email a day per person, none on the signup day, each kind once.
