# Support reply templates

Fill the [brackets]. Delete any line that doesn't fit. Every reply: under 80 words, answer first, signed by a person.

## Tone rules (the author's)
- **The ask or the answer first, the thanks after.** Warmth before the request makes people answer the warmth.
- **Use their words.** If they said "the export button", don't say "the reporting module".
- **Say what to add, not what is missing.** Not "we could not find your invoice details" but "it'd help to have your invoice email". Start with what already works, then the one thing left.
- **Warmth comes from plain words, not extra sentences.** The author's first "warm" emails were too long. Target: 1 greeting line, 1-2 lines on the one thing, a list of 1-3 items if needed, 1 closing line.
- **Sign with the founder's first name.** Not "The Team", not "Support".
- **Same voice for angry and happy people:** calm, warm, direct. Name the exact thing that went wrong.

## Saved lines (reuse word for word)
Keep the founder's approved lines in `how-to/email-lines.md` and reuse them as they are. Good starting lines:
- An acknowledgement: "Thanks for writing. I'm looking into this today and will reply as soon as I know more." No date the founder hasn't set.
- When everything is fine but one thing: "Looks good, one step left: [the one thing]."
- When you need one detail: "To sort this out, could you send [the one thing]?"

## Escalation rule
The agent drafts. The founder decides anything that costs money, sets a date or changes an account.

| Trigger | What the agent does |
|---|---|
| Refund, credit, discount | Draft with `[FOUNDER: yes/no?]`, top of the report |
| They want a date for a fix or feature | Draft without a date; the founder adds one or not |
| Chargeback, lawyer, privacy, data deletion, public threat | One holding line only ("Got this, I'm on it personally today."), red flag in the report |
| Second message with no answer | Top of the report |
| Answer not found in the product or docs | Write "not found", ask the founder; never guess |

---

## 1. How-to
"How do I...?", "Where is...?"
```
Hi [name],

Here's how:
1. Open [page, as named on screen].
2. Click [button].
3. You'll see [result].

Did that work?
[Founder]
```
Check every step in the product today. Second time this month? Add "FAQ candidate" to the report.

## 2. Bug
```
Hi [name],

Thanks for flagging this. I can see it too: [the problem, in their words].
I'm on it and will write the moment it's fixed. [FOUNDER: add a date?]

Meanwhile: [workaround, if a real one exists].
[Founder]
```
Can't reproduce it:
```
Hi [name],

I tried [what you tried] and it worked for me, so I'm missing something.
Could you send a screenshot of the screen where it breaks?
[Founder]
```
Task: what happened / what they expected / steps / account / device / when.

## 3. Refund request
```
Hi [name],

Got it. [FOUNDER: refund [amount]? yes / no / partial]
[If yes:] I'm refunding [amount] today. Banks usually show it within [days].
[If no:] [Your policy in one kind line.] What I can do: [alternative].

If you have a second, what didn't work for you? It helps me fix it.
[Founder]
```
Never write "I've refunded" until the founder pressed the button.

## 4. Billing / failed payment
```
Hi [name],

Your [plan] renewal on [date] didn't go through. Usually it's an expired card or a bank limit.
Your access stays on for now, and the card is tried again over the next days.
[If there is a self-serve link:] You can update the card here, it takes a minute: [link]
[If not:] If your card changed, tell me and I'll sort it out with you.
[Founder]
```
Read the payment dashboard first: the automatic failed-payment emails may already have gone (see customer-emails, decision rule "Failed payment: day 0, 3, 7"). Don't send a fourth. "Charged twice" or "wrong amount": state what the dashboard shows. The founder approves any fix.

## 5. Feature request
```
Hi [name],

That makes sense for [their use, in their words]. I've written it down with your note.
I can't promise a date, but I'll tell you if it ships.
[If something already does part of it:] The closest thing today is [how].
[Founder]
```
Log: date, customer, exact words, plan, how many others asked.

## 6. Angry customer
```
Hi [name],

You're right: [the specific thing that went wrong]. That's on me.
Here's what I'm doing: [one concrete action, founder-approved].
[If they lost something: what you'll do about it, founder-approved.]

I read every reply myself.
[Founder]
```
Never defend, never quote policy, never match their caps. If you don't know what to offer, flag it. Don't send a holding reply that says nothing.

## 7. Cancellation
```
Hi [name],

Done. You won't be charged again, and you keep access until [date].
[FOUNDER: cancel now or at period end?]

If you have ten seconds: what made you cancel? One line is plenty.
[Founder]
```
If the reason is fixable (a bug, a missing how-to), answer that first and let them choose. Never block or guilt. Offer only the save offer the founder set for their reason (customer-emails, decision rule "Save offers match the reason"), once per customer, never in their first 30 days.

## 8. Sales question (before they buy)
```
Hi [name],

[Direct answer: yes / no / how.]
[One fact for their case: price, limit or what's included, true today.]
[If it's not a fit, say so and say what would fit.]

What are you hoping to use it for? I'll tell you honestly if it fits.
[Founder]
```
They named a company, a team size or asked for a call? Pass to `head-of-sales`.
