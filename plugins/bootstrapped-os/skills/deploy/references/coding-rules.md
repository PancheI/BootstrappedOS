# Coding rules (read against the diff before every batch)

These are the author's rules from two production apps. Each says what happened. Paste the ones that apply into CLAUDE.md under "Invariants".

## Money and data
1. **The backend owns every number.** Totals, statuses, prices and derived fields are computed on the server and returned ready to render. The UI only displays them. Money is stored as integer minor units (cents). How the author learned it: each invoice screen summed its own totals, and they printed different numbers for the same invoice. Prove correctness with a test against the API response, not by looking at the screen.
2. **Money logic is test-first, with the full table of inputs.** Run the tests on every money path. A buyer-overcharge bug survived per-rule tests because it only showed in one combination of inputs; it was caught at pre-merge review.
3. **Act on exactly the rows you counted.** A job that sums some rows, then marks them done with a fresh query, can mark rows it never counted if anything changes in between. Then the record says one total and the money says another. Mark by the ids you listed, and if the marked total doesn't equal the summed total, undo and skip.
4. **Idempotency key on every external "create" call** (charges, refunds, checkout sessions). On a retry with a different body, derive a new key (`<key>:retry-2`) rather than reusing it.
5. **A vendor setting never loses the sale.** A payment method that wasn't switched on in live mode once made the whole checkout fail. Catch that one known rejection and retry with the basic option, so the buyer sees a working form. Any other error still surfaces.
6. **Prices come from one server file** (`src/config/pricing.json` in the starter). The browser sends a plan key, never an amount, currency or discount.
7. **One source of truth, read at display time.** Don't copy what the vendor already holds (payments, identity, bank details) into your own tables. Store a thin reference and read the rest when needed.
8. **No N+1.** A query inside a loop over rows becomes one batched query or a JOIN. Select only the columns you use. Check every list endpoint for per-row fetches before it ships.

## Database
9. **RLS is enabled in the same migration that creates the table.** No policy means no browser access; add owner-only policies (`auth.uid() = user_id`) only when a page needs them. In the author's app, users read their own rows through RLS and every write goes through server code.
10. **Schema and data changes are migration files**, written to run twice, shown before applying (see the deploy skill). No `db reset`, ever, local included.

## Secrets and config
11. **Secret keys live in files that start with `import "server-only"`.** Only `NEXT_PUBLIC_*` values reach the browser. Never print a key in logs, chat, commits or screenshots.
12. **Env holds secrets and account ids only.** Prices, fee rates and buffers are code constants; per-customer settings live in the database. Before adding a key, name who reads it.
13. **If a service key is missing, the page says what's missing** and the rest of the site still works. Don't fake a value to make it render.

## Dependencies and wiring
14. **Pin versions that are at least 7 days old.** With npm (the launch starter): check `npm view <pkg> time` before adding a dependency and pin the exact version in `package.json`. With pnpm: `minimumReleaseAge: 10080` (minutes) in `pnpm-workspace.yaml`. That blocks the publish-then-yank supply-chain attack. One repo with no guard pulled day-old builds of a deploy tool.
15. **Boot the app after changing wiring.** Tests and typecheck don't see the dependency graph: a full green test suite once passed while the server crashed at startup over one missing export. "Booted clean" goes in the report.
16. **Changing a shared return shape breaks tests you didn't touch.** A new field on a result object fails strict `toEqual` and `toHaveBeenCalledWith` assertions in sibling files. Run the whole suite before pushing.

## Small security rules
No personal data in URLs or analytics events (send it in a request body) · check the session on the server in every route; hiding a button isn't access control · a `next=` redirect must start with `/` and not `//` · tests and smoke runs never reach a paid or real vendor (stub them before the first navigation).
