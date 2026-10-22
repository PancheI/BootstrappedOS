---
description: Triage customer messages - label, draft replies, create tasks, flag who might leave.
---

Use the `support-inbox` skill and the `head-of-support` agent for $ARGUMENTS (my unread customer messages: the email connector if available, otherwise what I paste).

**Read first:** `knowledge/customers.md`, `knowledge/how-to/voice.md`.

1. Group by person. Read their account in the system of record before the thread. Can't see it? Write "account not checked".
2. Before any reminder or chase, search the inbox for their reply. Replied = review again, not a reminder.
3. One `one-customer-writer` per reply. The ask or answer in line 1, thanks after. At most 3 asks, each one that would change what we do.
4. Check every fact a reply relies on yourself; list what you checked and what came from an agent.
5. If the tool that replies is logged out, stop and tell me. Never reply from another inbox.

**Hand back:** the drafts, and the 3 that need me today. Drafts only. Gates: `shared/gates.md`.
