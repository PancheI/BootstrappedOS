# Head of Engineering (software module)

**Software built in small, checked steps.** A design you approve, code written test-first, an independent review, a browser check, and a release checklist before anything goes live. You approve the design and say when it ships.

**What the module adds:** four agents (architect, implementer, reviewer, verifier), the build loop and its skills, the `/feature`, `/review-branch` and `/ship` commands, and the launch starter that the landing-page stage copies. It needs the core plugin (`bootstrapped-os`).

## Set it up (2 minutes, once)
1. Install the core first ([INSTALL.md](../INSTALL.md)), then the module:
   ```
   claude plugin install bootstrapped-os-software@bootstrapped-os
   ```

   **You should see** `✔ Successfully installed plugin: bootstrapped-os-software@bootstrapped-os`.

## For each change (your time: 10 minutes)
1. Type `/feature` and the change in one line, for example `/feature add a "what stopped you?" question to the cancel screen`.

   **You should see** a design and a task list, and then it stops. Nothing is built until you approve.
2. Reply `go`. It builds each task, gets a separate review, and shows you the result locally.
3. Type `/review-branch` for one last review of the whole change.

   **You should see** one list of findings, the most serious first. It fixes nothing until you pick.
4. Type `/ship`.

   **You should see** a checklist with evidence (tests, migrations, a check in the browser). It merges or deploys only when you write "deploy" or "merge".

## What a good result looks like
```
Design: cancel screen asks "what stopped you?" (3 choices + free text), saved to cancel_reasons
Tasks: 1 migration (adds a table)  2 form + save  3 show reasons in the Monday review
Risk: migration is additive, no data changes
Waiting for your go.
```

## One memory
The build keeps its own ledger in `.dev/progress.md`, so a long build survives a fresh session. Decisions you make go to `knowledge/decisions.md` like every other role.

## Avoid
- **Approving a design you didn't read.** Read the task list; it is what gets built.
- **One session running for days.** Ask for a handoff note before you stop.
- **"go" as "deploy".** `go` builds and shows locally. Only "deploy" ships.

**Files behind this role:** `plugins/bootstrapped-os-software/` (agents, skills, commands, `templates/launch-starter`)
