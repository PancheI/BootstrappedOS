## Engineering rules (append to your CLAUDE.md; fill the brackets)

### Process
- Use the head-of-engineering skill at the start of any code work. Ledger: `.dev/progress.md`; briefs: `.dev/briefs/`.
- Gates and approval words: `shared/gates.md` in the bootstrapped-os plugin. Production migrations go out only in a deploy batch, after I've seen the SQL.
- Between gates, keep going and reason out loud. Don't ask "should I continue?". Writes to the local dev database on test rows don't need my yes.
- Changes under ~30 lines in files you've read: make them yourself. Bigger work: one brief, one implementer, one commit.
- Check git before trusting any agent's "done" (`git log -1 --stat`, the diff). Agents are one-shot; stop them when they report.
- Review findings come to me as one list (finding · real? · in design? · smallest fix). I pick; you fix exactly that, nothing new.

### Deploy
- Where it runs: `knowledge/decisions.md` [default: Vercel for the app, Supabase for the database].
- Batch: verify locally, keep a Pending list in `knowledge/trackers/deploys.md`. When I say "deploy": migrations first (`supabase db push`), then the app [`npx vercel --prod`], then anything else on the list.
- Done = whole suite green, CI green for this commit, and the live page checked in my visible Chrome, scrolled fully. Report what wasn't checked.

### Database
- Schema and data changes are migration files in `supabase/migrations/`, applied locally with `npx supabase migration up --local` (the gate asks once; say yes for local).

### Rules
- The rule set: `skills/head-of-engineering/references/coding-rules.md` in the bootstrapped-os-software plugin. Copy the lines that matter here.
- [Your product's own: e.g. which vendor is the source of truth for payments, users, content]
