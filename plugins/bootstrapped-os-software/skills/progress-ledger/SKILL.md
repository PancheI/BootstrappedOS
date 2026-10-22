---
name: progress-ledger
description: Head of Engineering. Keeps the progress ledger (.dev/progress.md) that survives context compaction - design link and approval, verified integration facts, the founder's decisions in his words, one row per task, gate status. Use at the start of a session, after every task, and before stopping.
---

# Progress ledger

The ledger is the recovery map for long builds. Read it first after any compaction or new session, before the code. Update it after every task, not at the end of the day. If it isn't in the ledger, it didn't happen.

**References:** none. The format is below.

## The process
1. **Open** `.dev/progress.md`: one section per feature, newest at the top. How the author does it: his long builds (a billing feature, a sign-up flow reworked four times in one day) survived many compactions because the ledger, not the chat, held the state.
2. **Start each section with the same blocks:**

```
## <feature> - goal: <one line>
Design: <doc link> v<N>, approved <date> ("<founder's exact word>")
Branch: <name>, cut from origin/main <hash>. Pushed: yes/no (push is a gate)
Status: building | verifying | gate: merge | gate: deploy | done

Integration facts, verified live on <date>:
- <what the vendor really does, tested in the sandbox, not read in the docs>

Decisions (founder's words, dated):
- <date>: "<quote>" -> <what it means for the build>   e.g. "reuse the setting we have" -> no new table

| Task | Commit(s) | Review | Deferred minors | Proof |
|------|-----------|--------|-----------------|-------|
| T1 send the invite email | a1b2c3d | clean | - | 6 tests, red then green |
| T2 accept the invite on sign-in | e4f5a6b + fix c7d8e9f | 2 fixed (founder picked) | naming in invites.ts | whole suite green |
| T3 remove a member | f0a1b2c | clean | - | booted clean; NOT pushed |

Suites: <files>/<tests> (last full run <date>)
Verified by me in Chrome: <screens> -> <link to the screenshots>
Next: T4. Waiting on: <nothing | founder: deploy | founder: "I pushed the DB">
```

3. **After every task,** add or update its row. A fix gets its own hash on the same row.
4. **Before stopping,** set Status and "Next", and link the handoff note if you wrote one (`handoff-note`).

## Decision rules
- If you changed the design mid-build, add a "Deviations" block: what changed and which reviewer intent was kept.
- If you didn't re-run it or see it yourself, it goes in the handoff note's "NOT verified" list, not the Proof column.

## Quality bar
- [ ] Every task row points at real commit hashes, not "done".
- [ ] The Proof column holds only what you re-ran or saw.
- [ ] Founder quotes are verbatim and dated. They settle later arguments with reviewers ("no new table" was his call, not a reviewer's).
- [ ] Gate state is a line, not an assumption: "not pushed = gate", "migration written, not applied".

## Never
- Paragraphs in the ledger. Put them in the feature doc and link it.
- Mix "verified by me" with "agent-reported".

## Shared knowledge
**Read first:** `.dev/progress.md`. **Write after:** `.dev/progress.md`. `.dev/` is the code repo's working folder (gitignored); knowledge paths are in `shared/knowledge-tree.md`.

## Bootstrapped core
Not used.
