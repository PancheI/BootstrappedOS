---
name: release-gate
description: Head of Engineering. The checklist before merging to main or deploying - whole suite and CI green on the exact commit, migrations additive and reviewed, live-mode settings checked, a smoke run with vendors stubbed, every actor's first-time path clicked, a rollback line. Shows the evidence and stops for the founder's word.
---

# Release gate

Show each line with its evidence (a pasted summary line, a link, a file name). A box without evidence counts as unchecked. The founder decides whether it ships.

**References:** `head-of-engineering/references/coding-rules.md`. Hosting comes from `knowledge/decisions.md` (default: Vercel + Supabase).

## The process
1. **Code**
   - [ ] **Whole suite** green locally (paste the summary line), typecheck and lint clean. Not only the files you touched.
   - [ ] **CI green for this exact commit:** `gh run list --workflow=ci.yml --commit $(git rev-parse HEAD) --json conclusion`. Needs `.github/workflows/ci.yml` (the head-of-engineering "Set up once" step). "Pushed" isn't "done" while CI is pending or red.
   - [ ] App **booted** from a clean start after any wiring or config change (stale dev servers killed first).
   - [ ] Every ledger row: review clean or the founder's picks fixed; acceptance criteria met with evidence.
   - [ ] `git diff --cached --stat` or the PR file count matches the work. No stray design files, no `.env`, no key in the diff.
   - [ ] The branch was cut from `origin/main`, not local main.
2. **Data**
   - [ ] Every migration in the batch is **additive**, was shown, was reviewed against the local schema (by the `supabase` skill if installed, otherwise by the reviewer), and is applied locally.
   - [ ] Data changes (seed rows, content, settings) are migration files too, written to run twice.
   - [ ] The order is agreed: migrations to production **before** the code that reads them.
3. **Outside services**
   - [ ] **Live-mode settings** the release depends on (payment methods, webhooks, sender domains, rate limits) were confirmed by the founder **on the live account**, not assumed from test mode. How the author learned it: a setting turned on in test mode only broke the live checkout minutes after a release. It was "believed done".
   - [ ] Smoke run with every vendor-facing route **stubbed before the first page load** (at the network level; an in-page `fetch` patch is lost on reload). Afterwards, the vendor dashboard and the server log show nothing was created. How the author learned it: twice a smoke run created real, paid sessions at a vendor.
4. **Screens**
   - [ ] `browser-checker` in the founder's visible Chrome on every changed screen, **scrolled top to bottom**, desktop and 390px. A glance at the top once missed a duplicated form lower down.
   - [ ] **Every actor's first-time path:** new account, invite link, plain login without the link, refresh, back, direct URL. Fresh emails never used before.
   - [ ] One page or folder with the screenshots (for example a private Artifact): step, what it proves, pass or fail, and what was not checked.
5. **Rollback**
   - [ ] One line, written now: how to put the previous version back on your host (on Vercel: promote the previous deploy), and for the database, the forward-fix migration if one would be needed.
6. **Stop.** "Ready to <merge|deploy> <what>. Migrations: <files>. Rollback: <line>. Not checked: <list>. Ship?" **Gate:** see `shared/gates.md` in the core plugin.
7. **After shipping**
   - Tags: `git ls-remote --tags origin | grep vX.Y.Z` must return the tag. How the author learned it: a release commit and its tag sat unpushed for days while production stayed on the old version.
   - The health or version endpoint reports the new version (poll it; "deploy accepted" isn't "running").
   - `browser-checker` on the live URL, look and click only. Report what was checked and what was not, then add the deploy line.

## Decision rules
- If a box has no evidence, it is unchecked. Say so in "Not checked"; don't tick it.
- If CI isn't set up, say "CI not set up" instead of ticking the CI box.

## Quality bar
- [ ] Every ticked line has evidence next to it.
- [ ] The rollback line exists before the founder is asked.

## Never
- Merge, push, tag or deploy before the founder's word.
- Let a smoke run reach a real or paid vendor.

## Shared knowledge
**Read first:** `.dev/progress.md`, `knowledge/decisions.md`, `knowledge/trackers/deploys.md`. **Write after:** `knowledge/trackers/deploys.md` (one dated deploy line), `.dev/progress.md` (Status). Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Not used.
