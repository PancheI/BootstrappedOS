# Example: how I run my company with this system

I'm Panche. I run a one-person company: Bootstrapped Makers and AgentaOS. This page is the only place in the repo with my own numbers. Your tools will differ; the jobs stay the same.

## What I pay each month

| Job | My tool | $/month |
|---|---|---|
| Chief of Staff and every role | Claude Code (Max plan) | 100–200 |
| Code and deploys | GitHub, Vercel, Supabase, Cloudflare | 0 (free tiers) |
| Search | Google Search Console, Bing Webmaster Tools | 0 |
| Sales | LinkedIn and X, by hand | 0 |
| Voice | ElevenLabs | 0 (startup credits) |
| Knowledge | `CLAUDE.md` and the `knowledge/` folder | 0 |
| Analytics | PostHog | 0 (free tier) |
| Video | Remotion | 0 |
| Payments | AgentaOS (my own) | 0 |
| **Total** | | **$100–200, plus startup credits** |

You don't need my setup. An AI plan that runs Claude Code (from $20 a month) plus free tiers is enough to start. Per role: [`ai-team-cost.csv`](ai-team-cost.csv).

## My day
- **Find people who ask.** Every morning, with coffee, I ask Claude for 3 to 5 posts from the last week (X, LinkedIn, Reddit) where someone asks a question my product answers. I write the replies myself. AI finds the people; I don't let it write my messages. ([`guides/04-sales.md`](guides/04-sales.md))
- **Three design options.** For any page or design change, I ask for three options: bold, middle and safe. Then I pick one. ([`guides/11-growth-module.md`](guides/11-growth-module.md))
- **Read PostHog daily.** I look at where people stop on the page, and ask Claude to improve the page from that. ([`guides/07-numbers.md`](guides/07-numbers.md))
- **"go" means build and show me locally.** Only "ship" or "deploy" goes to production ([`shared/gates.md`](plugins/bootstrapped-os/shared/gates.md)).

## What it did in 114 days (25 Jun to 16 Oct 2026)
- 1,033 active hours with Claude Code; 3,313 agents; 59% of code changes made by agents.
- 791 releases; 616 video renders; 416 voice-overs and soundtracks; 109 customer emails drafted (I sent them all myself).
- Time: 64% product, 24% marketing and video, 11% ops, finance and customer emails.
- AgentaOS: about $10k a month in recurring billing running through it, two months after the 10 Aug 2026 launch. That is sellers' billing, not my company's own revenue.
- The honest part: 48% of my releases went out without a browser check, and only 6% of sessions started with a plan. That is why this system has gates.
