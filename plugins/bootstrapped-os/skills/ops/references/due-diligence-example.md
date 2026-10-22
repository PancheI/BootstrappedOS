# Illustrative example

A made-up business, a made-up client and made-up links (`.example` domains don't exist). All names and numbers are invented to show the format.

---

## The business

**Northline Studio** - a two-person video agency. Makes short product videos for software companies. Usually 3-6 clients at a time, paid 50% upfront and 50% on delivery.

## What the founder asked

"Use ops: check Corvant Group. They want 6 videos a month for a year, paid 60 days after each invoice. That would be about half our revenue. Should we sign?"

## What the COO did

1. Looked in `knowledge/checks/`: one earlier memo, a client on 45-day terms in 2025 who paid 3 months late. Decision then: "deposit required for terms over 30 days".
2. Searched the inbox: 4 emails from Corvant's marketing lead. One mentions "our standard supplier terms are 60 days, non-negotiable".
3. Opened Corvant's website in the browser. The careers page loaded; the "Suppliers" page blocked the fetch tool but loaded fine in the real browser.
4. Found the company in the public register, with the latest filed accounts.
5. Read independent reviews from freelancers and agencies.
6. Filled the gate and the type checks for a **big client**.

## The memo it wrote

```markdown
# Corvant Group - due diligence (DRAFT)

**Type:** big client
**Asked by:** founder, 15 Oct - sign a 12-month deal, 6 videos a month, 60-day payment terms
**Suggested decision:** go ahead with a condition - because the company is real and pays, but 60-day terms on half our revenue is a cash risk we can't carry without a deposit

## Gate
| # | Check | Evidence (link) or "not found (searched: ...)" |
|---|---|---|
| 1 | Legal entity and country | Corvant Group Ltd, registered 2014, accounts filed on time: https://company-register.example/corvant-group-ltd |
| 2 | Website live, what they sell, prices (verbatim) | Live 15 Oct; sells HR software; "Plans from 49 per user / month": https://corvant.example/pricing ; supplier terms "Invoices are paid 60 days from receipt": https://corvant.example/suppliers |
| 3 | Founder(s) and public footprint | CEO and marketing lead have public profiles matching the company since 2016 and 2021: https://corvant.example/about |
| 4 | Reviews / complaints (independent sources) | 3 freelancer forum posts say "pays on day 60, never earlier, never later"; 1 says invoices were rejected for a wrong PO number: https://freelance-forum.example/t/corvant-payment-terms |
| 5 | Our own history with them: emails, payments, disputes | New client, no payments yet; 4 emails since 2 Oct, terms stated as non-negotiable (inbox search "corvant", 15 Oct); not found (searched: payment tool, invoicing tool, knowledge/checks) for any earlier work |
| 6 | Red flags | Ask about it: 60-day terms for half our revenue; invoices rejected without a PO number: https://freelance-forum.example/t/corvant-payment-terms |
| 7 | Decision proposed + why | Go ahead with a condition because they are real and pay on day 60, but we need a 3-month trial with a 30% deposit on each monthly batch before a 12-month deal |

## Type checks
- Are they who they say: yes, register and website match (row 1, 2).
- Can they pay: filed accounts show a profitable company (register link above).
- Payment terms they ask vs ours: 60 days vs our 50% upfront. Big gap.
- Scope written down: draft scope email from 9 Oct lists 6 videos, 60-90 seconds, 2 revisions each.
- Share of our revenue: about half (arithmetic, from last 3 months' invoices). A dependency.

## Red flags, sorted
- Stop: none - identity, company and payment history check out.
- Ask about it: 60-day terms on a deal this size; PO numbers needed on invoices.
- Note only: they work with two other video agencies (their case-study page).

## Earlier checks
- 2025 client on 45-day terms paid 3 months late -> rule since then: deposit for terms over 30 days.

## The one ask
"Can we start with a 3-month pilot, with 30% of each month's batch paid upfront, and 60 days on the rest?"

## Not checked
- Whether their PO system can handle a deposit invoice - only they can answer.
```

## The checker

```text
$ python3 scripts/check-memo.py knowledge/checks/2026-10-15-corvant-group.md
PASS
```

## What the founder decided

Sent the one ask (the founder wrote and sent it). Corvant agreed to a 3-month pilot with a 20% deposit and asked for the PO number on every invoice. The founder accepted 20%. The memo was updated with the reply, re-checked (PASS), and marked FINAL.

## Why this decision

Nothing about Corvant was wrong. The risk was ours: half our revenue arriving 60 days late. The COO didn't hunt for problems or pile on questions. It found the one thing that would change the answer, asked it once, and left the decision to the founder.

A new rule went into `knowledge/rules.md`: "Big client over a third of revenue -> always check payment terms against our cash, not just whether they pay."
