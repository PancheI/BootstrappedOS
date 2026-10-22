# Launch starter

A one-page site and a working product, ready to deploy: landing page, product page, pricing with AgentaOS checkout, magic-link sign-in and a signed-in area, a Supabase waitlist, PostHog analytics, privacy and terms, sitemap, robots and a social image. Every service is optional; the site runs without it and says what's missing.

Two files hold everything you'd change:
- `src/config/product.json`: name, promise, buyer, the problem in their words (each quote linked), steps, FAQ, legal details.
- `src/config/pricing.json`: your pricing models, once. The page, the checkout and `npm run plans` all read it.

## Use it
The landing-page skill copies this folder into your project for you. To do it by hand, copy `templates/launch-starter` from the installed `bootstrapped-os-software` plugin (Claude Code keeps plugins under `~/.claude/plugins/`) or from a clone of the repo:
```bash
cp -r <path-to>/bootstrapped-os-software/templates/launch-starter ~/my-startup && cd ~/my-startup
npm install
cp .env.example .env.local      # fill only what you have
npm run dev                     # http://localhost:3000
```
Before every commit: `npm run typecheck`, `npm run lint` and `npm test` (the test checks `pricing.json`; add your own next to it in `tests/`). Versions are pinned exactly, and `.npmrc` keeps new installs pinned too.

## Payments (AgentaOS)
Disclosure: AgentaOS is the author's own company. To use another provider, replace `src/lib/agentaos.ts` (the checkout) and the two scripts in `scripts/`.

1. Put a test key (`sk_test_...`) in `.env.local` as `AGENTAOS_API_KEY`.
2. `npm run plans` shows what it would create from `pricing.json`. `npm run plans -- --yes` creates them and saves each id into `pricing.json` right after it is created. Running it again skips plans that already exist.
3. The pricing buttons now open a real checkout (test mode: no money moves). On localhost the buyer stays on the checkout's own success page; AgentaOS only returns buyers to an https address. VAT, receipts and payouts are handled by AgentaOS as merchant of record.
4. Once the site is on https (set `NEXT_PUBLIC_SITE_URL` in production), the buyer lands on `/thanks` after paying, with a "Sign in to start" link (same email as the checkout).
5. Going live: see "Go live" below.

## Go live (AgentaOS)
`npm run golive` prints what's left, read-only:
```
[x] Tried it: a test product and a test payment
[ ] Verification: not submitted yet: fill it in the AgentaOS dashboard
[ ] Payout account: add one in the AgentaOS dashboard
[x] Open questions: none
[ ] Can go live: not yet
```
Verification and the payout account are yours to fill in the AgentaOS dashboard (they are your legal and bank details; no script submits them). When it says "Can go live: yes": put the live key (`sk_live_...`) in `.env.local` and in Vercel, run `npm run plans -- --yes --live`, then make one real purchase yourself and refund it.

## Login (Supabase magic link)
1. Set `SUPABASE_URL` and `SUPABASE_PUBLISHABLE_KEY` (Project settings -> API Keys; the publishable key is safe to expose).
2. Supabase dashboard -> Authentication -> URL Configuration: Site URL = your address; add `<your-site>/auth/callback` (and `http://localhost:3000/auth/callback`) to Redirect URLs.
3. To show the 6-digit code in the email too: Authentication -> Emails -> Magic Link, add `{{ .Token }}` to the template. Without it the link alone works.
4. For real users, set your own SMTP (Authentication -> SMTP); the built-in sender is rate-limited and for testing only.

How it works: `/login` emails a link and a code, `/auth/callback` turns the link into a session, `src/proxy.ts` keeps the session fresh, `/app` checks who is signed in on the server (shows the email, "your plan" and sign out). No extra table is needed; add one (with row level security) when a page needs to store something per user. Without the env vars, `/login` says what's missing.

## Waitlist (Supabase)
The table is in `supabase/migrations/0001_waitlist.sql`. Apply it with the Supabase CLI: `supabase link` to your project, then `supabase db push` (the gates ask you first). Don't paste SQL into the dashboard's SQL editor: a change made there never reaches your migration files. Then set `SUPABASE_URL` and `SUPABASE_SECRET_KEY`.

## Analytics (PostHog)
Set `NEXT_PUBLIC_POSTHOG_KEY`. The events are listed in `src/lib/analytics.tsx`. Paid comes from AgentaOS, not analytics. Analytics run without cookies (`persistence: "memory"`), so no cookie banner is needed and the privacy page says so. If you turn cookies on, update the privacy page and add a consent banner.

## Deploy (Vercel)
`npx vercel` for a preview, `npx vercel --prod` to go live (the gates ask you first). Add the same env vars in the Vercel project settings, then set `NEXT_PUBLIC_SITE_URL` to your https address (the checkout needs it to send buyers to `/thanks`) and add `<your-site>/auth/callback` to the Supabase Redirect URLs.

## Get found
After deploy: submit `<your-site>/sitemap.xml` to Google Search Console and Bing Webmaster Tools, then run `/launch-week`.
