# AGENTS.md

Guidance for AI coding agents (Claude Code, Cursor, Codex) working on this repository.

## What this repo is
Claude Code plugins in markdown: `plugins/<plugin>/agents/*.md` (roles), `skills/<skill>/SKILL.md` (steps with gates), `commands/*.md` (slash commands), `hooks/` (the safety gates). There is no app to build.

## Rules that never bend
1. **Agents draft and propose; the founder decides.** Never weaken a gate in `plugins/bootstrapped-os/hooks/`. Any change there needs a new case in `hooks/test-hooks.sh`, and `bash plugins/bootstrapped-os/hooks/test-hooks.sh` must print "All gate tests pass."
2. **No sensitive info, ever.** Run `scripts/check-sensitive.sh` (turn the pre-commit hook on with `git config core.hooksPath .githooks`). No keys, emails, phone numbers, local paths, or names of real customers, merchants or private people. Use made-up examples.
3. **Method here, knowledge in the core.** Don't add measured datasets, lesson sets, directory lists or funding lists to this repo. Skills ask `bootstrapped-core` (see `CONNECT.md`) and must keep working without it: say "Bootstrapped core not connected: using the method only" once and continue.
4. **The founder's own `knowledge/` wins** over any core answer.

## Style
Short sentences, plain English, one idea per line. No buzzwords, no em dashes. Steps a non-technical founder can follow, each with what they should see.

## Before you open a pull request
- `bash plugins/bootstrapped-os/hooks/test-hooks.sh`
- `bash scripts/check-sensitive.sh --all`
- Say which skill or agent you ran and what you saw.
