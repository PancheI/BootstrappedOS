---
name: review-package
description: Head of Engineering. Builds the review package for one task (its diff, the brief and the design), dispatches an independent reviewer for two verdicts, challenges the findings, and brings the founder one list to pick from. Use after every implementer finishes, before marking the task done.
---

# Review package

The reviewer finds; you check its findings; the founder picks which get fixed. The git state is the truth; the agent's report is a claim.

**References:** `head-of-engineering/references/coding-rules.md` (what the quality verdict checks against).

## The process
1. **Check git before anything else:** `git log -1 --stat` and `git diff --cached --stat`. If the file count is bigger than the brief implied, or the commit is on the wrong branch, stop and fix that first.
2. **Build the package:**
   ```
   mkdir -p .dev/reviews
   git diff <base>..<head> > .dev/reviews/<task-id>-<base>..<head>.diff
   ```
   Give the `reviewer`: the diff file, `.dev/briefs/<task-id>.md`, the design and the business sentence. Nothing else from the session.
3. **Ask for two verdicts:**
   - **Spec:** every acceptance criterion -> met / not met, with file:line.
   - **Quality:** bugs, N+1, money computed in the UI, a missing idempotency key, secrets, over-building (a diff three times bigger than the brief implied is a finding).
   - Each finding is Critical, Important or Minor, **with a concrete failing scenario**. Drop any without one.
   - The reviewer re-runs the suite, typecheck and (if wiring changed) the boot itself. It doesn't trust the implementer's numbers.
   - For SQL: a second check reads the migration against the real local schema (the `supabase` skill if installed) and answers PASS, PASS-WITH-CHANGES or REVISE.
4. **Challenge the findings before the founder sees them.** How the author does it: reviewers inflate severity to look thorough. He has thrown out a "race" on a vendor code that is single-use anyway, an "injection" in a URL built on the server from a fixed list, and a "leak" in a loop that already stopped on cancel. Each would have added code and no safety. Another round of accepted findings once grew a design by a whole second table. For each finding:
   - Read the code path. Can a real user reach it?
   - Does fixing it serve the business sentence, or add a table, column or mechanism nobody reads?
5. **One list to the founder:**

   | # | Finding | Real? (evidence) | In the design? | Smallest fix |
   |---|---|---|---|---|

   **Gate:** the founder picks. Fix only those, exactly as the design says, with a red-then-green test for anything behavioural. Run the whole suite, make one fix commit, add a ledger row. Minor findings not picked go in the ledger's "Deferred minors" column for `/review-branch`.

## Decision rules
- If the design's own rule is the problem, say so and ask. Don't patch around it.
- If a finding has no scenario you can reproduce, drop it, but say you dropped it.

## Quality bar
- [ ] Every finding on the list has evidence and says whether it is in the design.
- [ ] The fix commit touches only the picked findings.

## Never
- Invent a new mechanism while fixing.
- Hand the reviewer the session history.

## Shared knowledge
**Read first:** `.dev/briefs/<task-id>.md`, the design, `.dev/progress.md`. **Write after:** `.dev/reviews/`, `.dev/progress.md`. `.dev/` is the code repo's working folder (gitignored).

## Bootstrapped core
Not used.
