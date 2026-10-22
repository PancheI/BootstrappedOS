---
name: deploy
description: Head of Infrastructure. Takes the launch starter (or any Next.js app) live on Vercel + Supabase in batches - verify locally, collect changes, then db push + app deploy together on the word "deploy", then a visible-browser check of the live site. Cloudflare Pages (wrangler) for static sites. Use for "deploy", "ship it", "put it online", "go live", "Vercel", "Supabase project", "db push", "custom domain", "env vars", "Cloudflare".
---

# Deploy

Default stack: **Vercel** (app) + **Supabase** (database, sign-in). **Cloudflare Pages via wrangler** for a static site. The agent builds, checks and prepares; the founder says "deploy". The hooks already ask before `supabase db push`, `vercel --prod`, `wrangler pages deploy` and pushes to main. This skill decides *when* those asks happen: rarely, in one batch, after local proof.

**References:** `references/coding-rules.md` (read against the diff before every batch) · `references/cloudflare.md` (static sites on Cloudflare Pages).

## The process
1. **Collect.** Every change waits on the local app. Keep the list in `knowledge/trackers/deploys.md` under `## Pending`: one line per change, migration file names included.
2. **Local proof.**
   - Kill stale dev servers (`lsof -iTCP:3000 -sTCP:LISTEN`, kill every leftover `next dev`), restart with `npm run dev`, and confirm the page serves the new code. An old server once handed yesterday's build to "verified" screenshots.
   - Run the launch starter's checks on the whole project, not only the files you touched: `npm run typecheck`, `npm run lint`, `npm test`, then `npm run build`. Paste the summary lines. A script the project doesn't have yet: say so, don't skip silently.
   - Apply migrations locally with `npx supabase migration up --local`, never `db reset`.
   - Run **browser-checker** in the founder's visible Chrome on every changed screen, scrolled top to bottom, desktop and 390px. Link the screenshots in the report.
3. **Show the pending list and every new migration's SQL**, one line each on what it creates or changes. **Gate:** wait for "deploy" or "ship" (`shared/gates.md`).
4. **Migrations to production first:** `npx supabase db push`. Code that reads a new column must never go live before the column exists. If the founder says "I pushed the DB", they applied the migrations themselves: take their word, don't re-run.
5. **App:** `npx vercel --prod`, or merge to the branch Vercel deploys from if that's the setup.
6. **Static site**, if it changed in the same batch: `references/cloudflare.md`.
7. **Live check.** Run browser-checker on the production URL: the pages the batch touched, scrolled fully, plus the home page, the sign-in page and a pricing button that opens checkout. The console must be clean. Report what was checked and what was **not**. Then move the Pending lines into the log with the date.

## Decision rules
- **"go" means local, "deploy" or "ship" means production** (`shared/gates.md`). The author once said "go" on a change and it went straight to production. His answer: "give me local first".
- **Batch, don't drip.** Deploying after every small edit hit the Vercel free plan's daily deployment limit, and production was frozen until the next day.
- **Schema AND data go in migration files.** Seed rows, settings and content each get a numbered file in `supabase/migrations/`, written so it can run twice (`insert ... on conflict (slug) do update set ...`), first line a comment saying what and why. Data once written straight to production through an MCP tool never reached local, and the next local test lied. No writes through the dashboard SQL editor, the Management API or an MCP `execute_sql`. Read-only checks are fine.
- **Show, then apply.** Write the migration, show the SQL and the alternatives, apply locally only after an OK. Never write and apply in one step.
- **A second reviewer reads the SQL** before production (the Supabase skill, against the real local schema). It has caught a column added twice in one file and a `create or replace function` with a new parameter that silently made a second function.
- **A batch is additive only:** new tables, columns, indexes. A rename or drop is its own release, after no live code reads the old name. List what a migration can't hold (files in Storage) in the deploy line.
- **Env vars hold secrets and account ids only.** Prices, tuning numbers and feature lists live in code or the database. Every key is another place production can break. Add with `npx vercel env add <NAME> production` (and `preview`); the founder pastes the value. `npx vercel env ls` (names only) is the check.
- **Live-mode vendor settings are checked on the live account.** A payment method switched on only in a vendor's test mode once made every live checkout fail. Before a release that depends on one, the founder confirms it in the live dashboard and you write "checked live: <setting>" in the deploy line.
- **Once you have CI and paying customers,** add a release gate: release only from a clean `main` that equals `origin/main` with CI green for that exact commit, the founder applies production migrations, and the deploy polls a `/health` route until it shows the new version.
- **Rollback.** Vercel: Deployments -> the previous production deploy -> Promote (instant; the founder clicks or says go). Database: no undo for a push; fix with a new migration, which is why batches stay additive. Write the rollback line in the deploy log before deploying.

## Supabase (once per project)
- The founder creates the project in a region near the buyers and sets the matching Vercel region in `vercel.json`. Then `npx supabase login` and `npx supabase link --project-ref <ref>`.
- Keys from Project settings -> API Keys go straight into `.env.local`. Never into chat, a commit or a log.
- Auth -> URL Configuration: Site URL = the production address; Redirect URLs = `<site>/auth/callback` and `http://localhost:3000/auth/callback`.
- Auth -> Rate limits: raise "emails sent per hour" to at least 100 before a launch day, or sign-ins stall when a post does well. Set up your own SMTP before real users arrive.

## Quality bar
- [ ] Typecheck, lint, tests and build pass locally, with the summary lines pasted.
- [ ] Every changed screen checked in a visible browser, desktop and 390px.
- [ ] Every new migration's SQL shown and reviewed before "deploy".
- [ ] Migrations went live before the code that reads them.
- [ ] The live check says what was checked and what was not; the deploy line is in `knowledge/trackers/deploys.md`.

## Never
- Deploy, `db push` or push to main without "deploy" for this batch.
- Run `supabase db reset`, drop or truncate anything, or hand-run SQL on production.
- Submit a form, sign up or pay on production. The only real purchase is the founder's own, by hand, refunded.
- Print or commit a key. Buy a domain or upgrade a plan.
- Report "done" on red CI, a skipped suite or a live page nobody looked at. "Deployed" isn't "done".

## Shared knowledge
**Read first:** `CLAUDE.md`, `knowledge/decisions.md` (hosting, domain), `knowledge/trackers/deploys.md` (Pending and the last deploy). **Write after:** one line per deploy in `knowledge/trackers/deploys.md`: `date · prod · URL · changes · migrations · rollback · live check yes/no (what was not checked)`. Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Ask `recipes` (area `ai-agents`) before step 1 and `lessons` (theme `shipping-safely`, then `truth-and-numbers`) at the decision rules. If it isn't connected, carry on with this method.
