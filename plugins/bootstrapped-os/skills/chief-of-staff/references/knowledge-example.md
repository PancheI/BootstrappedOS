# Illustrative example

A made-up business. All names and dates are invented to show the format.

---

## The business

**Trailmark** - a SaaS that helps small hiking guides take bookings. One founder. Claude Code for building and for customer emails. Notes in plain files in a private git repo.

## What happened this week

On Monday the founder corrected Claude: "Don't offer a discount in cancellation emails. We decided that in August." On Wednesday, a new customer-email draft offered 20% off to a cancelling customer again.

The founder ran:

`/log-decision No discounts to save cancellations. Ask why they're leaving instead.`

## What the Chief of Staff found first

- `decisions.md` already had an entry from 14 Aug: "Cancellation emails: offer 20% off for 3 months". Never marked replaced.
- `knowledge/rules.md (Customer emails)` still said "Save offer: 20% off".
- CLAUDE.md said nothing about discounts.

So Claude had followed the old rule. The correction on Monday was never written down.

## What it proposed (shown to the founder before saving)

**1. New decision entry**

```markdown
## 2026-10-14 - No discounts to save cancellations
**Decided:** cancellation emails ask why they're leaving and offer a pause. No discount.
**Why:** of 6 customers who took the 20% offer since August, 5 cancelled when it ended (Stripe). It delayed churn, it didn't stop it.
**What would change it:** if a pause offer saves fewer than 1 in 10 cancellations over 2 months.
**Replaces:** 2026-08-14 - Cancellation emails: offer 20% off
**Files updated:** knowledge/rules.md (Customer emails)
```

**2. Old entry marked**

```markdown
## 2026-08-14 - Cancellation emails: offer 20% off for 3 months
**Replaced by:** 2026-10-14 - No discounts to save cancellations
```

**3. Rule file updated** (`knowledge/rules.md (Customer emails)`)

```markdown
**Rule:** Cancellation emails never offer a discount. Ask one question ("what made you decide to leave?") and offer a 1-month pause.
**Why:** 14 Oct - discount takers mostly cancelled when it ended. Replaces the 14 Aug "20% off" rule.
**How to apply:** applies to every cancel or downgrade email. If the customer asks for a discount themselves, don't promise one; pass it to the founder.
```

**4. Index line updated** (`knowledge/INDEX.md`)

```markdown
- [Customer emails](rules.md#customer-emails) - 40-80 words, one button; cancellations: ask why + pause, never a discount (updated 14 Oct)
```

**5. CLAUDE.md:** no change. The rule only matters for customer emails, so it lives in that topic file.

## What the founder decided

"Yes, save all of it." Then: "Also redo Wednesday's draft." The Head of Support redrafted it with the new rule.

## Friday cleanup (same week)

```markdown
- New corrections: 1 (discounts) - done Wednesday
- Duplicates: two "Emails" headings in rules.md -> merged into "Customer emails"
- Clashes: none left
- Dead rules: "post on Twitter daily" (stopped in September) -> marked replaced
- CLAUDE.md: 41 lines, fits on one screen
- Index: 1 dead link (rules.md#emails) removed
- Scratch: a pricing note in a temp folder -> moved to decisions.md
- Backup: committed
```

## Why this works

The founder said it once more, and never again. The old rule can't come back, because it now says "Replaced by". And the decision says what evidence would reopen it, so the founder doesn't have to argue it from memory.
