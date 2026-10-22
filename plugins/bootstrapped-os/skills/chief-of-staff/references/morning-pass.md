# Morning pass

One pass, one message, one log entry. The Chief of Staff plans the day; the morning pass works the queues behind it. Everything it makes is a draft or a suggestion.

Templates: `morning-pass-templates.md` · Worked example: `morning-pass-example.md`

## The rule that makes this safe
**Nothing runs unless the founder names its number in this conversation.**
- Number the suggestions 1, 2, 3 in the order they appear.
- "go 1 3" does 1 and 3. "go all" does every number in this message and nothing else: read the list back first.
- "skip 2" drops it. Silence, "ok", "yes", "do it" or a thumbs-up approves **nothing**: say which numbers you think were meant, and ask.
- "go" means draft or build it and show it. It never means send or deploy (`shared/gates.md`).
- Suggestions expire after 48 hours. Check the data again; never act on an old list.
- Never chain suggestions ("since 1 ran, 4 follows"). Never invent one to fill a quiet day.

## Step by step
1. **Check every source.** One read per login and connector. Expired or locked? Stop the whole pass and ask the founder to log in. Never log in for them. A pass that half-ran must say so, not report a partial picture as the day's numbers.
2. **Read yesterday's log** (`knowledge/log/<yesterday>.md`). Anything the founder said yes to that isn't done comes first.
3. **The state of the business** (the read-only `watch` agent): sales, sign-ups, queues. Print the tool's figures as given. Read the whole list on anything that pages, never the first page.
4. **Money at risk:** failed or unpaid payments, disputes, refunds asked for. Check the source is up before you write "none": an outage and an empty list look the same.
5. **What changed by itself since yesterday:** anything published, switched on or changed without the founder. Does it look right? A flag means "look", not "act".
6. **The queues, one customer per agent,** oldest first. Cap them and write "N more waiting".
7. **Check the history before every customer step,** including the inbox for replies a dashboard never saw.
8. **Drafts:** one `one-customer-writer` per customer. Drafts only.
9. **Re-read each draft yourself.** Names, amounts and dates against the source.
10. **Write the message** from the template: Looked at / Skipped / Suggested / Needs you.
11. **Add to the log:** the suggestions, then what the founder said yes and no to, then what got done.
12. **Wait.** Do only the numbers the founder names. Log each one with where you saw the result.

## Two number rules
- **A rate for the whole business never appears in a sentence about one customer.** Numbers about one customer come from that customer's record.
- **Numbers about an account come from the live system,** never from a file or an earlier step. Different systems often give different counts for the same thing; say which one you used.

## Decision rules
- A suggestion = one action, one customer or one object, one line, plus the fact it rests on ("invoice #1042 failed 2 days ago").
- Can't check a source? It goes in **Skipped** with the reason. A missing source must never read as "all clean".
- Same customer in two queues? One suggestion, not two.
- More than 7 suggestions? Keep the 7 closest to money or a waiting customer. The rest wait for tomorrow.
- Anything about money, prices, refunds or public posts goes in **Needs you**.

## Quality bar
- [ ] All four sections present, even if a section says "nothing".
- [ ] Every suggestion is numbered, one line, with its fact and source.
- [ ] Skipped lists every source that could not be reached.
- [ ] Every customer draft was checked against that customer's history.
- [ ] Today's log entry is written before you report.
- [ ] Nothing ran without its number.

## Never
- Never send, pay, refund, publish or delete. The founder does that.
- Never treat "ok", "sounds good" or silence as approval.
- Never act on a suggestion older than 48 hours.
- Never put two customers in one agent.
- Never mark something done without seeing the result (the Drafts folder, the dashboard, the page).
- Never leave Skipped out to make the message shorter.
