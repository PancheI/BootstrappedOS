# Morning pass templates

---

## 1. The message

```markdown
# Morning pass - <date>

**Looked at:** <source> (<what, count>) · <source> (<what, count>) · ...
**Skipped:** <source> - <why it could not be checked>   (write "nothing skipped" only if true)

## Suggested
1. <action> - <customer/object> - because <fact> (<source>)
2. <action> - <customer/object> - because <fact> (<source>)
3. ...

## Needs you
- <decision only you can make> - my pick: <answer> because <reason>

Reply "go 1 3", "skip 2", or "go all" (I'll read the list back first).
These suggestions expire <date + 48h>.
```

Writing a suggestion line:
- Good: `2. Draft day-3 reminder - Ana (yearly plan) - because her renewal failed on 12 Oct (Stripe)`
- Bad: `2. Follow up with failed payments` (no person, no fact, no source)

---

## 2. The log entry

Add to `knowledge/log/YYYY-MM-DD.md`. One file per day. Never edit yesterday's file.

```markdown
## <time> morning pass

### Suggested
1. <same line as the message>
2. ...

### You said yes
- 1, 3 (founder: "go 1 3", <time>)

### You said no
- 2 (founder: "skip 2") - <reason if given>

### Done
- 1: <what happened and where you saw it: "draft saved in Gmail Drafts">
- 3: <...>

### Skipped sources
- <source> - <why>
```

---

## 3. Queue order (paste into CLAUDE.md to change it for your business)

```markdown
## Morning pass queue order
1. Failed / unpaid payments
2. Customers waiting for a reply (oldest first)
3. New sign-ups / orders / bookings since yesterday
4. Open refunds and disputes
```

Shop? Add "orders not shipped after 2 days" at 2.
Coach or agency? Add "sessions tomorrow without prep notes" at 2.
