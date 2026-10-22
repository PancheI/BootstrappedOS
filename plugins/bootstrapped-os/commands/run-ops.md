---
description: The full morning pass - read every connected tool, draft what's needed, and give you a numbered list of proposals. Nothing is sent.
---

Use the `chief-of-staff` skill (its morning pass) and the read-only `watch` agent for $ARGUMENTS.

**Read first:** `knowledge/log/` (yesterday), `knowledge/customers.md`, `knowledge/numbers.md`.

1. **Logins first.** One read per connected tool. If one is locked or expired, stop the whole pass and tell me. Don't report half a picture as the day's numbers.
2. **The state of the business:** sales, sign-ups and what's waiting, as the tools print them. Whole lists, not one page.
3. **Money at risk:** failed or unpaid payments and disputes. Check the source is up before writing "none".
4. **Anything that changed by itself since yesterday** (a plan turned on, a page published, a scheduled job). Does it look right? Flag it; don't act.
5. **Customers waiting, oldest first.** Check each person's history first. One `one-customer-writer` per customer, drafts only. If there are many, do the first few and write "N more waiting".
6. **Re-read every draft yourself:** names, amounts and dates against the source.
7. **Write the message:** what you looked at, what you skipped and why, the numbered proposals, and what needs me. A proposal is one action, one line, with the fact it rests on ("invoice 1042 failed 2 days ago"). At most 7, closest to money first.
8. **Log the pass** in `knowledge/log/<date>.md`: the proposals, which I approved, and what was done.

**Hand back:** the message. I reply with numbers: "go 1 3" does 1 and 3, as drafts or local changes; "skip 2" drops 2. "ok", "yes" or silence approves nothing. Nothing is ever sent at any step: I send every message myself. Only "ship" or "deploy" means production. Gates: `shared/gates.md`.
