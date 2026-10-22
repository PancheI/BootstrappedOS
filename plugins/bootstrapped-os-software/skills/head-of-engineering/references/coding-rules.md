# Engineering rules (the only copy in this module)

Every agent and skill in the software module links here. Paste the rules that apply into your project's `CLAUDE.md` under "Invariants", and add your product's own. Gates (what needs the founder's yes, and what "go" means) are not here: they are in the core's `shared/gates.md`.

## Money and data
1. **The backend owns every number.** Totals, prices and statuses are computed on the server. The UI only shows them. Money is stored in integer minor units (cents).
2. **Money, auth and data logic are test-first.** Write the failing test, see it fail, implement, see it pass. A decision with several inputs is tested across the full table of combinations, not one rule at a time.
3. **Prices come from one server file.** The browser sends a plan key, never an amount.
4. **Idempotency key on every external "create" call** (a charge, a plan, a session), or a check that it already exists. A retry must never create a second one.
5. **Don't copy what a vendor already holds** (payments, identity, bank details). Store a reference and read the rest when needed.
6. **No N+1.** A query inside a loop over rows becomes one batched query or a join.

## Database
7. **Schema and data changes are migration files**, written to run twice, shown to the founder before they are applied. Never paste SQL into a dashboard, never write to production through an API or MCP, never `db reset`.
8. **Row level security is on in the same migration that creates the table.** Batches are additive; renames and drops ship in a later release.

## Keep it simple
9. **Nothing without a named reader.** No new table, column, env var, setting or layer unless you can name the code that reads it. Extend what exists.
10. **Env holds secrets and account ids only.** Constants live in code; per-customer settings live in the database.
11. **Don't solve a UI problem by hiding the feature,** and don't fix a server problem by adding a question to a one-tap screen.

## Git and dependencies
12. **Stage explicit paths, never `git add -A`.** A broad add once pulled a folder of private design files into a pull request. Check `git diff --cached --stat` before each commit.
13. **Branch from `origin/main` after `git fetch`,** never from local main. The main session cuts the branch; agents don't.
14. **Never undo with `git checkout` or `git restore`.** Reverse the edit instead; a "quick undo" has wiped uncommitted work.
15. **Pin exact dependency versions that are at least 7 days old** (`save-exact=true` in `.npmrc`; check with `npm view <pkg> time`). That avoids a package that is published, then pulled.
16. **No "pre-existing".** A lint, type or runtime error in a file you touch is fixed in the same commit.
17. **Boot the app after a wiring change** (providers, imports, exports). Tests and typecheck don't see the whole dependency graph.
18. **Run the whole test suite,** not only the files you touched. A new field on a shared result breaks strict assertions in sibling tests.

## Small security rules
No personal data in URLs or analytics events · check the session on the server in every route; hiding a button isn't access control · a `next=` redirect must start with `/` and not `//` · secret keys only in server files · tests and smoke runs never reach a paid or real vendor.
