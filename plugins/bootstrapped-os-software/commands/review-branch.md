---
description: One review of the whole branch before merging - one list of findings for you to pick from.
---

Use the `reviewer` agent with the `review-package` skill for $ARGUMENTS.

**Read first:** `.dev/progress.md` (the design link and the ledger's "Deferred minors").

1. `git fetch`, then build the package from the whole branch diff against `origin/main` (not one task).
2. Dispatch the `reviewer` on sonnet with the diff, the approved design and the business sentence.
3. Challenge its findings as `review-package` says.

**Hand back:** one list of findings, Critical first. Fix nothing until I pick. Gates: `shared/gates.md`.
