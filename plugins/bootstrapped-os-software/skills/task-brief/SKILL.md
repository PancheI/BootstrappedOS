---
name: task-brief
description: Head of Engineering. Writes one implementer brief for one task, as a file the implementer reads (never the session history) - exact file:line anchors, values and test assertions, so the agent has no room to wander. Use before dispatching any implementer.
---

# Task brief

One page in `.dev/briefs/<task-id>.md`. The implementer reads only this and the files it names.

How the author does it: he stopped trusting thin briefs after implementers went sloppy on missing context: a seed row matched by name instead of id, a status field that clashed with the framework's own, a revenue figure counted twice in the UI. Since then a brief names the exact line, the exact value and the exact assertion. If you can't write those, the task isn't ready to hand off: do it yourself or plan it further.

**References:** `head-of-engineering/references/coding-rules.md` (copy only the rules that apply into "Invariants").

## The process
1. Fill this template:

```
# <ID> <title>
Why: <the problem, one line; quote the business sentence if this touches money or data>
Goal: <what exists when done, observable>

Work in: <absolute repo or worktree path>. cd there first; use absolute paths.
Read first: <path:line-range>, <path:line-range>
Change: <path:line> -> <exact change>   (one line per edit)
Signatures / SQL: <function, endpoint or migration file name + body>
Values: <exact constants, copy, prices - nothing for the agent to invent>

Acceptance criteria (each one checkable):
- <behaviour> -> proven by <test name + assertion | curl + expected body | screen + what shows>
- <behaviour> -> proven by ...

Tests to write first (money/auth/data): <test file, case names, the input table>
Invariants that apply: <the relevant lines from coding-rules.md and CLAUDE.md>
Skills to use: <e.g. supabase for SQL, if installed>

Out of scope: <files and concepts NOT to touch; "no new tables, columns, env vars or helpers">
Migrations: write the file, DO NOT apply it.
Git: stage explicit paths only. One commit "<ID>: <title>". Don't push.
Deliver: commit hash, `git diff --stat`, the WHOLE suite's summary line, "booted clean" if wiring changed.
```

2. Read it back as the implementer would: is there anything left to guess? If yes, add the value or the line.
3. Dispatch one `implementer` with the file path.

## Decision rules
- If the brief needs two commits, it is two tasks.
- If the work isn't on the main checkout, the "Work in" line is mandatory. How the author learned it: agents told only the worktree's path still edited the main checkout and committed to the wrong branch, more than once.

## Quality bar
- [ ] Every acceptance criterion says how it is proven.
- [ ] "Whole suite", not "tests pass". How the author learned it: a PR went red in CI because the agent ran only the files it touched, while a new field broke strict assertions in two sibling test files.
- [ ] "Out of scope" names concepts, not only files. "No new limit, flag or table" stops the most common over-build.

## Never
- "Apply" in a brief. The implementer writes the migration; you show it and it is applied after the gate.
- Paste the session history.

## Shared knowledge
**Read first:** the design, `.dev/progress.md`. **Write after:** `.dev/briefs/<task-id>.md`. `.dev/` is the code repo's working folder (gitignored).

## Bootstrapped core
Not used.
