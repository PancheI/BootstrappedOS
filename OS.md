# Bootstrapped OS: the org

This page is the only list of roles, agents, skills, commands and models. Other files link here instead of repeating it.

You are the CEO. Your AI company has six departments. The **Chief of Staff** (your Claude Code session) runs them: it sends each job to the right role, picks the model by how hard the job is, and stops for your yes at every gate. Every role shares one memory, `knowledge/`, and the safety gates stop anything that sends, ships, pays or deletes without you.

```
                                   CEO (you)
                                       │
                               Chief of Staff
                     runs the stages · picks the model · gates
                                       │
     ┌───────────────┬─────────────────┼──────────────────┬────────────────┬───────────────┐
  STRATEGY        FINANCE        PRODUCT & ENG         GROWTH        SALES & CUSTOMERS   OPERATIONS
  Research        CFO            Design                Growth            Sales            Analytics
  Idea Critic     Grants         Infrastructure        Content           Support          Watch
  Positioning                    Engineering           Creative Dir.     Customer Writer
  Brand                          Browser Checker
```

## The departments

| Department | Role | Agent | Skills | Commands | Tools | Model |
|---|---|---|---|---|---|---|
| **Office of the CEO** | Chief of Staff | your session | chief-of-staff, ops | `/day0` `/start-from-zero` `/morning` `/run-ops` `/where-are-we` `/log-decision` | Claude Code, `knowledge/` | your default |
| **Strategy** | Head of Research | `head-of-research` | idea-finder | inside `/start-from-zero` | web search, Chrome, Reddit RSS | opus |
| | Idea Critic | `idea-critic` | idea-finder | inside `/start-from-zero` | web, Chrome | opus |
| | Head of Positioning | `head-of-positioning` | positioning | inside `/start-from-zero` | web, Chrome | opus |
| | Brand Designer | `brand-designer` | brand-brief | inside `/start-from-zero` | domain lookup, Google Fonts | sonnet |
| **Finance** | CFO | `cfo` | pricing-audit, payments-agentaos, numbers | `/pricing-audit` `/money-review` | AgentaOS, public pricing pages | sonnet (opus for the pick) |
| | Head of Grants | `head-of-grants` | grants-and-credits | `/grants` | web, Chrome | sonnet |
| **Product & Engineering** | Head of Design | `head-of-design` | landing-page | inside `/start-from-zero` | launch starter, Chrome, design kit | sonnet |
| | Head of Infrastructure | `head-of-infrastructure` | deploy | inside `/start-from-zero` | Vercel, Supabase, Cloudflare, GitHub | sonnet |
| | Head of Engineering (software module) | `architect` `implementer` `reviewer` `verifier` | head-of-engineering, task-brief, review-package, release-gate, progress-ledger, handoff-note | `/feature` `/review-branch` `/ship` | Claude Code, GitHub, Supabase | sonnet |
| | Browser Checker | `browser-checker` | (any) | `/check-live` | Chrome | haiku |
| **Growth** | Head of Growth | `head-of-growth` | launch; growth module: head-of-growth, head-of-seo | `/launch-week`; growth module: `/critique-page` `/check-funnel` `/seo-brief` | Search Console, Bing, IndexNow, PostHog | sonnet |
| | Head of Content | `head-of-content` | content-posts, lead-magnets | `/post-from-a-win` `/content-week` `/lead-magnet` | LinkedIn, X | sonnet |
| | Creative Director | `creative-director` | video module: launch-video, creative-director | inside `/start-from-zero` (needs the video module) | ElevenLabs, Remotion | sonnet |
| **Sales & Customers** | Head of Sales | `head-of-sales` | buyer-signals, sales-outreach | `/first-customers` | LinkedIn and X by hand, Gmail drafts | sonnet |
| | Customer Writer | `one-customer-writer` | (one person per run) | inside sales and support | Gmail drafts | haiku |
| | Head of Support | `head-of-support` | support-inbox, customer-emails | `/triage-inbox` `/write-emails` | Gmail | sonnet |
| **Operations** | Head of Analytics | `head-of-analytics` | numbers | `/weekly-review` | PostHog, AgentaOS | sonnet |
| | Watch | `watch` | (read-only sweep) | you can schedule it (Claude Code scheduled tasks or cron), because it only reads | read-only | haiku |

**Model** is the Claude model a role uses: haiku for cheap, simple checks, sonnet for normal work, opus for hard judgement. The Chief of Staff can move a job up a level when a result fails. The rules: [`model-routing.md`](plugins/bootstrapped-os/skills/chief-of-staff/references/model-routing.md).

How each role works, step by step: [`guides/`](guides/).

## The two ways you use it
- **Starting from zero:** `/start-from-zero` runs [the stages](plugins/bootstrapped-os/shared/stages.md) in order, from Strategy to the first customers. One stage at a time; you approve each.
- **Already live:** `/day0` asks your revenue. At $0 you start on Sales, Growth, Content and Grants; Support switches on when customers arrive. Your rhythm at $0: `/first-customers` daily, `/weekly-review` on Mondays, `/grants` monthly. With customers: `/morning` daily, `/weekly-review` on Mondays, `/grants` and `/money-review` monthly.

## What you install
| Package | What's inside | For |
|---|---|---|
| **`bootstrapped-os`** (core) | every role above except Head of Engineering and the growth and video skills | every founder |
| **`bootstrapped-os-software`** | Head of Engineering's four agents and the launch starter | founders who build software |
| **`bootstrapped-os-growth`** | conversion and SEO depth | founders selling from a website |
| **`bootstrapped-os-video`** | launch videos and the advanced film pipeline | founders who make launch videos |

Each module needs the core plugin. Shared by all: `knowledge/` (one memory), the starter lessons in [`claude-md-starter.md`](plugins/bootstrapped-os/lessons/claude-md-starter.md), the safety gates ([`shared/gates.md`](plugins/bootstrapped-os/shared/gates.md)) and the model routing.
