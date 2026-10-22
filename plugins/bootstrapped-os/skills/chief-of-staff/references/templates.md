# Chief of Staff templates

Copy, fill, delete what you don't use. Keep each one on one screen.

---

## 1. Morning brief

Save as `knowledge/log/YYYY-MM-DD.md` (or post it where you read things first).

```markdown
# Morning brief - <weekday> <date>

**Yesterday:** <visitors> visitors · <leads> leads · <sales> sales (<source: PostHog / Stripe / shop / not checked>)

## 3 things today
1. <verb + object, under 12 words> - <role>
2. <verb + object, under 12 words> - <role>
3. <verb + object, under 12 words> - <role>

## Blocked / waiting
- <what> - waiting on <who> since <date>
- <what> - blocked by <what is missing>

## Decisions needed
- <yes/no question>? My pick: <yes/no> because <one reason>.
- <question with a number>? My pick: <number> because <one reason>.

**Not today:** <things you saw but parked, comma separated>
**Not checked:** <what you could not look at, and why>
```

Rules for filling it:
- Start each "thing" with a verb: Reply, Fix, Send, Call, Write, Decide.
- A "thing" the founder does is fine. Write "- you" as the role.
- If there are no decisions, write "None today." Don't delete the heading.

---

## 2. Priority rules (paste into CLAUDE.md if you want them everywhere)

```markdown
## How to pick today's 3 things
1. Money at risk today (failed payment, broken checkout, unhappy paying customer).
2. A customer waiting more than one working day.
3. The one change from this week's numbers review.
4. This month's goal.
Everything else -> "Not today". Tie -> the one closer to money in or a customer helped.
```

---

## 3. End-of-week handoff

Add to Friday's `knowledge/log/YYYY-MM-DD.md`. Monday's brief starts by reading it.

```markdown
# Week <nn> handoff - <date>

## Shipped
- <thing that is live or sent, with a link or where to see it>

## Numbers vs last week
| | This week | Last week |
|---|---|---|
| Visitors | | |
| Leads | | |
| Buyers | | |
| Revenue | | |
(Source: <tool>. Full review: <link to numbers note>)

## Still open
- <thing> - next step: <step> - owner: <you / role>

## Decisions made this week
- <date> <decision> -> logged in <decisions file or page>

## Monday, first thing
<one task, one line>
```

---

## 4. Task report (after any routed task)

```markdown
**Did:** <what changed, one line>
**Checked:** <how you know it worked - a page you opened, a number you re-read>
**Not checked:** <what you could not check>
**Open:** <what is left, or "nothing">
```

---

## 5. Routing note (one line, before any task; the role comes from `OS.md`)

`Understood: <task in your words>. Role: <agent> (<skill>). Starting now.`
