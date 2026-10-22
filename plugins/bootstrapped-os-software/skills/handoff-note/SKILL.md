---
name: handoff-note
description: Head of Engineering. Writes a handoff note when a session ends, context runs low, or work moves to another person or AI model - what landed (hashes), what is proven, what is half-done, which gates are open, and this repo's traps. Use before stopping long work.
---

# Handoff note

Write it for a reader who has none of your context and will believe every word, so mark anything you didn't verify. The next session reads the ledger, then this note, then the code.

**References:** none. The format is below.

## The process
1. Save to `.dev/handoff-<date>.md` and link it from the ledger's "Next" line (`progress-ledger`).
2. Fill this:

```
# Handoff <date> - <feature>
Branch: <name> @ <hash>. Pushed: yes/no. Dev servers: <running on ports | all stopped>.

Landed (commit ranges): <T1 a1b2..c3d4, T2 ...>

Verified - do not re-check (how):
- <claim> - <suite summary line | link to the screenshots | live call + response>

Agent-reported, NOT verified by me:
- <claim> - <what would prove it>

Half-done: <task, file:line, what is written, what is missing>. Uncommitted files: <git status --short>.

Open gates:
- Migration <file> written, shown/not shown, applied locally yes/no, production: waits for the founder
- Deploy batch pending: <the Pending list in knowledge/trackers/deploys.md>

Rules this work must keep: <the rules and founder decisions that apply, quoted from the ledger>
Traps in this repo: <e.g. the dev server serves stale modules; worktree agents commit to the main checkout>
Questions for the founder: <one line each, with the default you'd pick>
```

3. Before handing off to another model, run `/review-branch` or note that it hasn't been run.

## Decision rules
- **"Do not re-check" only with the proof attached.** How the author does it: a claim of "server restarted with the latest code" that was really an hour-old process cost the next session an hour. Unproven claims go in the "NOT verified" block.

## Quality bar
- [ ] Uncommitted work is listed by path. A "quick undo" with `git restore` has wiped uncommitted work before; the next session must see what exists only on disk.
- [ ] Every dev server you started is stopped or named. The author once found many old watchers racing for one port, so "restarted" meant serving a day-old build.

## Never
- Write "done" without a hash.
- Leave a gate's state implicit.

## Shared knowledge
**Read first:** `.dev/progress.md`, `knowledge/trackers/deploys.md`. **Write after:** `.dev/handoff-<date>.md`, the ledger's "Next" line. `.dev/` is the code repo's working folder (gitignored); knowledge paths are in `shared/knowledge-tree.md`.

## Bootstrapped core
Not used.
