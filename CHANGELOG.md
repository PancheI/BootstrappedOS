# Changelog

## Unreleased (22 Oct 2026): the skeleton
- One contract for the whole repo: [`ARCHITECTURE.md`](ARCHITECTURE.md) says where each fact lives. Shared rules in `plugins/bootstrapped-os/shared/` (agent contract, gates, stages, the `knowledge/` tree), and templates for new agents, skills, commands and guides in `templates/` and `guides/_template.md`.
- `OS.md` is the only list of roles, skills, commands and models. README links to it instead of repeating it.
- Guides 02-12 rewritten in one shape: what you get, how to set it up, what you should see, one example, what to avoid. Role names match `OS.md`.
- Private figures removed from the method. The author's own numbers live only in [`example-my-setup.md`](example-my-setup.md).
- `QUICKSTART.md` now points to `INSTALL.md` and the first guide.

## 5.0.0 (21 Oct 2026): open source
- MIT licence. Install straight from GitHub: `claude plugin marketplace add PancheI/BootstrappedOS`.
- Open method, paid knowledge: lessons, launch directories, grants and AI credits, pricing benchmarks and the author's results moved to the Bootstrapped core, which members connect with one key (CONNECT.md). Without a key every step still runs on the method.
- New: Head of Sales finds buyer signals (3 real people asking, with drafted replies).
- Repo safety: a check blocks keys, emails, phone numbers and local paths in every commit and pull request.

## 4.1.0
- Cheaper to run: the Chief of Staff (your session) runs on your default model; it picks each agent's model by task hardness (opus for judgement, sonnet for normal work, haiku for checks); agents default to Sonnet, Haiku for simple jobs (watch, browser-checker, one-customer-writer), Opus for research, the idea critic and positioning. /start-from-zero briefs agents in under 150 words and doesn't re-read files.
- Positioning stage (1b), outcome-first hero rules, progress.md and a live run monitor with LLM calls per stage.

## 4.0.0
- Reorganised by stage. Each stage has a named role, a real agent and the exact tools it uses: Chief of Staff (your session) runs the track; new agents head-of-research, brand-designer, cfo, head-of-design, head-of-infrastructure, creative-director, head-of-growth, head-of-sales, head-of-content, head-of-analytics, head-of-support, head-of-grants. `/start-from-zero` dispatches one per stage.
- Only tools the author really uses: Viktor, Gojiberry, Outrank and Linear removed; tasks live in `knowledge/` and GitHub. Connectors add GitHub, Vercel, Supabase and Cloudflare (wrangler).
- New: a gate asks before creating live payment plans (64 tests).
- Pricing benchmarks for the CFO. In 5.0.0 they moved to the Bootstrapped core.

## 3.1.0
- `/first-customers`: a 30-day first-customer playbook on the Sales hire (one buyer, one problem, one price; people who know you; people who show the problem; the ask; count and fix one drop), with the founder's real launch as the example.
- `/day0` asks your revenue today. At $0 it leads with Sales, Launch, Content and Grants & credits and parks Support, money review and Ops.
- Safety gates: now catch force pushes written as `+main` or `refs/heads/main`, `--mirror`, deleting the main branch, `rm` aimed at `~/`, `.`, `*` (split flags and sudo too), lowercase destructive SQL and SQL files, payment API calls and payment CLI commands that move money, releases, repo deletes, cloud and container wipes. If the command can't be read (no python3 or jq), the gate asks instead of allowing. 61 tests.
- "Free money" is now Grants & credits (`/grants`); `/customer-emails` is now `/write-emails` (it clashed with the skill's name).
- Fixed contradictions: agents may build code only with a separate reviewer and verifier; video source cap is 25% everywhere; one spine for the system, other references per beat; parallel video agents only after the lead locks the style kit.
- 8 new lessons from 11,603 of the founder's own messages (87 in total): finish the loop, change only what was named, keep the raw voice, one set of numbers everywhere, keep brands apart, read the code before concluding, CI green before done, answer every point. Headline rounding: allowed only if still true today.
- Real runs added to the Sales, Content, Numbers, Launch and Grants worked examples.
- New commands: `/check-live` (walk your site as a buyer, visible browser, never pays) and `/where-are-we` (done, in progress, blocked on you, next three). Content reads your best posts from `knowledge/how-to/voice.md`.
- `/start-from-zero`: zero to launched in 8 approved stages, with new skills idea-finder (real signals to a niche wedge), brand-brief, landing-page, deploy (Vercel + Supabase, Cloudflare optional) and payments-agentaos (plans from pricing.json, test checkout, go-live check). The software module ships a launch starter: landing, product, AgentaOS checkout, Supabase waitlist and magic-link login, PostHog, legal pages, sitemap and social image.
- `/pricing-audit`: walk your product as a buyer, 2-3 pricing models with live precedents and break-even on your costs, ranked by money, one pick and a 10-day rollout; every figure tagged verified / arithmetic / projection. Worked example from a real audit, disguised.
- `/lead-magnet`: one free useful thing from real buyer questions and proof, give vs hold, posts, DMs and follow-ups.
- Video: `launch-video` rewritten (first film in an afternoon) with the founder's real run; the studio pipeline is marked advanced and optional.
- `ai-team-cost.csv` added: what each role costs on a budget and in the author's setup.

## 3.0.0
- 9 hires, no padding: Chief of Staff absorbs the morning pass and the knowledge base; Numbers absorbs Money; Ops absorbs due diligence; new Launch and Grants & credits hires.
- One shared knowledge base per business (`knowledge/`): every hire reads before and writes after.
- Every hire rewritten with a step-by-step process, quality bar, templates and a worked example.
- Lessons moved inside the plugin so every install has them; each hire links the lessons behind it.

## 2.0.0
- Reusable for any small business: core plugin (10 hires) + software, growth and video modules.
- `/day0` personalises CLAUDE.md from 4 questions.
- Lessons library: 79 rules from 629 saved notes, with a paste-ready CLAUDE.md starter.
- Tool-neutral guides; new content and launch-video skills; my setup as an example.

## 1.0.0
- First release.
