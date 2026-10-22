# Head of Support

**Every customer message labelled, with a short reply drafted.** Problems become tasks, and people about to leave are flagged. You read the drafts and press send.

Starts once you have customers. At $0, `/day0` leaves it out of your rhythm.

## Set it up (10 minutes, once)
1. Connect your email (Gmail or Outlook connector), or be ready to paste messages in. Connectors: `/day0` tells you which ones fit your tools.
2. Write your refund and cancellation rules once, in one line each, in `knowledge/rules.md`. The agent never promises a refund or a date on its own.

## Every day (10 minutes)
1. Type `/triage-inbox`.

   **You should see** a short report: how many messages, the ones that need you today (each with a draft and a yes/no question), labels, tasks created, and what it couldn't check.
2. Read each draft, edit it if you want, and send it yourself.

## What a good result looks like
```
Inbox: 9 messages, 7 tickets · account checked for 7 of 7
Need you today:
1. Mara - refund, wrote twice, bug confirmed in the log - draft ready, needs your yes/no
2. Tom - can't log in, magic link expired - draft ready
Labels: how-to 3 · bug 2 · refund 1 · billing 1
Saved-reply candidate: "how do I change my plan?" asked 3x this month
Not checked: Stripe disputes (no connector)
```
The draft for Mara names her exact problem in line 1, in under 60 words, and leaves the refund to you.

## One memory
Every customer touch goes in `knowledge/customers.md`, one dated line each. Sales sees who is unhappy before writing to them, and the Monday review counts the problems.

## Avoid
- **Letting it promise refunds or dates.** Those are your call; the draft asks you.
- **Answering the same question five times.** Turn it into a saved reply, an FAQ line or a fix.
- **A reminder to someone who already replied.** The agent searches the inbox first; if your inbox isn't connected, check yourself.

**Files behind this role:** `plugins/bootstrapped-os/agents/head-of-support.md`, `skills/support-inbox/`, `commands/triage-inbox.md`
