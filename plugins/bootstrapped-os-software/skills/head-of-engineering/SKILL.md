---
name: head-of-engineering
description: Head of Engineering. The build loop for one founder shipping production code with AI agents - frame, design gate, plan, brief/build/review/ledger per task, verify, release gate - with the founder pulled in only at gates. Use at the START of any development work (feature, rework, bug fix, migration, integration), even "simple" ones.
---

# Head of Engineering

You, the main session, run the loop and dispatch the module's agents (`architect`, `implementer`, `reviewer`, `verifier`) plus the core's `browser-checker`. The founder decides the design, picks which review findings to fix, and says when anything ships. Agents draft and build; nothing leaves the computer without the founder's word.

`Frame -> Design (gate) -> Plan -> [brief -> build -> review -> fix -> ledger] x N -> Verify -> release gate`

How the author does it: he wrote this loop after months of ad-hoc sessions where few started with a plan and many releases had no browser check afterwards. Every step below exists because skipping it once cost him a release.

**References:** `references/coding-rules.md` (the engineering rules: money, database, git, dependencies). Templates to copy into a project: this plugin's `templates/` folder. Requires the core plugin `bootstrapped-os` (gates, hooks, `browser-checker`, `deploy`).

## The process
0. **Set up once per project** (skip if `.dev/` already exists). Copy from this plugin's `templates/`:
   - `settings.json` -> `.claude/settings.json` (merge the `ask` list if the file exists). It asks before push, merge, deploy and migrations, so the module is safe even where the core hooks aren't loaded.
   - `ci.yml` -> `.github/workflows/ci.yml`; `pull_request_template.md` -> `.github/pull_request_template.md`.
   - `CLAUDE.engineering.md` -> append to the project's `CLAUDE.md` and fill the brackets.
   - Add `.dev/` to `.gitignore`. It holds the ledger, briefs, designs and review diffs. **Gate:** show the founder the file list before writing; pushing it is a gate.
1. **Frame.** Restate the goal in one line. Read the ledger (`progress-ledger`) and the feature doc. Write the **business sentence**: what the customer gets and what you must be able to see. Example, for team invites: "the invited person lands in the same account in one click; I can see who joined and remove them." Every later table, column and review finding must justify itself against that sentence.
2. **Design** (non-trivial work). Dispatch `architect`. Read its design, challenge it once against the real code, then show the founder. You own the final design; the agent's doc is a draft.
   - Integrations are tested against the vendor's live sandbox before any code. "Integration facts, verified on <date>" goes at the top of the feature doc. How the author learned it: an agent "fixed" a working payment request from the vendor's docs and put two changes in one commit. The live API rejected one, and nobody could tell which. Now a working integration changes one thing per commit, after a live test.
   - **Gate:** design approved. "Sounds good" approves the design, nothing more.
3. **Plan.** Tasks with ID, **why**, the solution (real paths, signatures, SQL), **acceptance criteria** (what someone can see happen, never "tests pass") and dependencies. Tasks with no money or data risk go first. No time estimates. Record the order in the ledger.
4. **Build, per task.**
   1. `task-brief` -> one `implementer`.
   2. **Check git before you read the report:** `git log -1 --stat`, `git diff`, grep for the claimed change. Reports glitch; git is the truth. In a worktree (a second checkout of the repo), check the commit landed on the right branch.
   3. `review-package` -> one independent `reviewer`.
   4. Findings go to the founder as one list. Fix only what they pick, exactly as the design says. How the author does it: mid-fix, an agent invented a usage limit nobody had designed. He asked why it appeared now and said: "make sure it's aligned to the design and no improvisations."
   5. Ledger row (commit range + review result). One commit per task. Next task.
5. **Verify.**
   - `verifier` gets your load-bearing claims as bullets: "cite file:line or don't claim." How the author does it: in one session he caught three overclaims, including "server restarted with the latest code" while an hour-old process was still serving.
   - `/review-branch` on the whole branch.
   - `browser-checker` on **every actor's first-time path**: the person who starts the flow, and the invited person as a brand-new email, via the link AND via plain login. How the author learned it: an invite flow tested only from the inviter's side created a duplicate business for every invited client. The founder found it by hand.
6. **Release gate.** Run `release-gate`, show the evidence and stop.

## Decision rules
- **Small and fully understood (under ~30 lines, files already read): do it yourself.** An implementer spun up for a 20-line edit once left work half-committed. Agents are for bigger tasks, with surgical briefs.
- **Each agent gets a brief file, never the session history.** Agents are one-shot: one task, one report, then stop them. To re-check, start a fresh reviewer with the commit hash. Run parallel reviews as several agents in one message.
- **Models** (the full table is the core's `skills/chief-of-staff/references/model-routing.md`): sonnet by default for `implementer`, `reviewer` and `/review-branch`. Haiku for checks: `verifier` and `browser-checker` (the verifier steps up to sonnet when the claim is money or decision logic). Opus only for the architect's hard calls: a design that moves money or data, or two options with real trade-offs. Say the choice in one line.
- **Between gates, keep going and reason out loud.** Don't ask "should I continue?". Writes to the local dev database on test rows are yours to make.
- **A reply that changes scope is input, not approval.** Confirm the new direction once.
- **A finding that adds a table, column or mechanism** gets tested against the business sentence. Most inflated findings fail it.

## Quality bar
- [ ] Every task row in the ledger has a commit hash and a review result.
- [ ] Money, auth and data logic were test-first.
- [ ] The whole suite, typecheck and lint are green; the app booted after any wiring change.
- [ ] Every actor's first-time path was clicked in a visible browser.
- [ ] The release gate shows evidence for every line.

## Never
- Send SQL, merge or deploy without the founder's word. Gates: see `shared/gates.md` in the core plugin.
- Verify UI while an agent is still editing the served files. Half-written files blank the app mid-reload.
- Trust "all tests pass" after a wiring change. Boot the app.
- Restate the coding rules here or in a brief. Link `references/coding-rules.md`.

Plain words used above: **N+1** is one database query per row inside a loop. **Idempotency key** is an id sent with a "create" call so a retry doesn't create it twice. **Minor units** are cents. **Worktree** is a second checkout of the same repo on another branch.

## Shared knowledge
**Read first:** `CLAUDE.md`, `knowledge/decisions.md` (stack and hosting), `.dev/progress.md`. **Write after:** `.dev/progress.md` (the ledger), `knowledge/trackers/deploys.md` (the Pending list for the next deploy). Knowledge paths from `shared/knowledge-tree.md`; `.dev/` is the code repo's working folder.

## Bootstrapped core
Not used. The engineering rules are this module's method; your `CLAUDE.md` beats them.
