# Running /start-from-zero

How the Chief of Staff runs the track. The stages, their roles and what each needs are in `shared/stages.md`; this page is how to run them.

## Before the first stage
1. **The intake, once.** Ask the founder for: their domain expertise; their rough idea (2-3 sentences, however vague); who they can reach this week; what they have complained about themselves; what they won't do; and what they have already built, tried or sold, and where that evidence lives (project folders, docs, a payments dashboard, customers). Save it to `knowledge/founder.md`. If the working folder's parent holds earlier projects, look before asking.
2. **The tools check** (`tools-check.md`). Show the table. Name each stage that needs a module or account the founder doesn't have, and say it will be skipped until they add it.
3. **Skip what's done.** Read `CLAUDE.md` and `knowledge/`. Any stage already done there is skipped, and you say so.
4. **Say the model plan in one line** (from `model-routing.md`), for example: "opus for research, the critic, positioning and the pricing pick; sonnet for the rest; haiku for checks".

## During each stage
- **One role agent per stage.** You dispatch; agents never dispatch each other. Brief each one in under 150 words: the stage, the files to read, what to hand back.
- **Pick the model per job** (`model-routing.md`). Set it on each dispatch. Escalate to opus when a result fails its check or the founder rejects it.
- **Save tokens.**
  - Time-box every research or critic agent to about 20 minutes. It writes its file as it goes and hands back what it has when the time is up.
  - Run at most two searches at once.
  - Never research a problem the founder didn't want.
  - Don't read the agents' or skills' own files yourself; they load them. Don't re-read knowledge files you already summarised.
- **Show progress.** At the start of each stage print "▶ <stage>: <agent> started"; at the end, "✅ <stage> done in M min: <result in one line>". Keep `knowledge/progress.md` as a table: stage, agent, model, status (⏳ / ✅ / ⛔), started, minutes, tokens, one-line result. Take tokens and time from each agent's completion report, never estimate them.
- **Check every hand-back before the founder sees it.** Hold it against the skill's quality bar. For the idea stage: the founder's history mined, every channel covered or marked blocked, links re-opened, a gap verdict per problem, inside the domain. If it fails, send it back or escalate the model. Don't make the founder ask for what the skill already requires.

## The idea stage is a loop
1. **History first** (`head-of-research`): what the founder built, tried, sold and heard, into `knowledge/founder-history.md`. If they already run a business in this domain, ask which target this run is for: a new product on their assets (the default), a new wedge for the existing business, or a clean start.
2. **Wide:** 6-10 distinct problems inside the domain, from real buyer signals in the last 60 days, each with a gap check.
3. **Attack** (`idea-critic`): try to kill each one.
4. **Gut check:** show the survivors in one line each and ask if the founder would spend a year on any of them. If none, look for new segments with the pain bar (5+ buyers who said it themselves, a measurable loss, it happens again and again, someone already pays for a workaround). Otherwise research fixes the ones they want and the critic runs a second round.
5. **Narrow:** the top 3 survivors as wedges (one buyer, one job, one painful moment), scored, with the critic's pick. The founder picks. No linked signal = no idea; say so instead of padding.

## Stage notes
- **Positioning:** if "why would anyone pay?" has no good answer, the wedge goes back to the idea stage.
- **Brand:** show the top 3 wedges side by side first, each marked with how it uses the founder's domain and how close it is to their rough idea. The founder picks, mixes or rewords.
- **Pricing:** the picked model goes into `pricing.json` once.
- **Landing page:** copy the launch starter from the software module into the project, fill `product.json` and `pricing.json`, and show screenshots.
- **Deploy:** the gates ask before each push to main, migration and production deploy.
- **Product, payments and login:** the smallest version that delivers the promise. AgentaOS plans in test mode (`npm run plans`, dry run first), the checkout tested end to end in test mode, magic-link login and the signed-in area, then `npm run golive` to show what's left. The founder submits their own account verification.
- **Launch video:** about 30 seconds, from the live product's real screens, with captions.
- **Launch and first customers:** get found, then the first 20 people with the problem and one lead magnet. Agents find people and suggest the angle; the founder writes and sends.

## After each stage
1. Add one line to `knowledge/retro.md`: what the founder had to correct, and whether it belongs in their `CLAUDE.md`.
2. Log each decision in `knowledge/decisions.md`, one dated line.
3. Show the result, ask "go to <next stage>?", and wait. "go" means the next stage, built and shown locally; only "ship" or "deploy" means production (`shared/gates.md`).

## At the end
- One screen: what's live (URLs), what's in test mode, what waits on the founder, and the next three actions.
- A cost block in `knowledge/progress.md`: tokens per stage, the total, the most expensive stage and why, and one way to make the next run cheaper.
- Hand over to `/first-customers` as the daily routine.
