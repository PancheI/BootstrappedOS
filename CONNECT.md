# Connect the Bootstrapped core

The core is the knowledge behind the method: the author's plays, lessons with their reasons, launch directories (link type, how to submit, traps, date checked), grants and AI credits, and the author's measured results. Your agents ask it while they work. It is for members of [Bootstrapped Makers](https://bootstrappedmakers.com/bootstrapped-os).

## 1. Get your key (1 min)
Sign in at [app.bootstrappedmakers.com](https://app.bootstrappedmakers.com) → **Account** → **Your Bootstrapped key** → **Create**. It starts with `bm_live_` and is shown once. You can revoke it and make a new one anytime.

## 2. Give it to Claude Code (1 min)
Mac or Linux, in Terminal. This line works in zsh (the Mac default) and in bash (most Linux):
```
echo 'export BOOTSTRAPPED_KEY="bm_live_…"' >> ~/.$(basename "$SHELL")rc && export BOOTSTRAPPED_KEY="bm_live_…"
```
It saves the key to `~/.zshrc` or `~/.bashrc`, whichever your shell uses, and sets it for this terminal too.

Windows (PowerShell):
```
[Environment]::SetEnvironmentVariable("BOOTSTRAPPED_KEY", "bm_live_…", "User")
```
Or run `setup/setup.sh`, which asks for it once.

Open a new terminal, start `claude`, and type `/mcp`. **You should see** `bootstrapped-core` in the list, marked as connected.

## 3. Check it works
Ask: `I have 0 customers. How do I get my first 10?`
The answer is one of the author's own plays, with the steps, a template and what happened when he ran it.

## What the core answers
| Tool | What you get |
|---|---|
| `recipes` | Up to 3 of the author's plays, step by step: first customers, pricing, getting paid from a small country, getting found on Google and in AI answers, funding, running on agents. Each with when to use it, a template and the result he measured |
| `lessons` | Up to 5 lessons for a theme or a question: the rule, why it exists, and how often it came up |
| `directories` | Up to 15 directories and launch sites, with the link type seen on a live listing, the cost, how to submit and the traps. Free ones only, unless you ask |
| `funding` | Up to 12 grants and startup credits a small company can apply for, open ones first, filtered by your country and company age if you give them |
| `evidence` | The author's measured results, with the period and the source: launch, sales, pricing, traction, funding |
| `whats_new` | What changed in the core recently |

Answers are small on purpose, and each row carries the date it was checked. A key allows 300 calls a day.

**It improves on its own.** When lessons, directories or grants are added or re-checked, your agents get them the next time they ask. There is nothing to update, download or change on your side.

## Your knowledge comes first
Your own `knowledge/` folder and `CLAUDE.md` stay in charge. The core fills what they don't cover. If the core says one thing and your rules say another, the agent follows you, tells you about the difference once, and asks whether to save it.

## Without a key
Everything still runs. When a step would ask the core, the agent says "Bootstrapped core not connected" once and continues with the method.

## Privacy
Only your question goes to the core (for example "saas, free only"). Your `knowledge/` folder, code and customers stay on your computer.
