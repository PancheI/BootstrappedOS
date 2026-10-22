# Contributing

Thank you for making Bootstrapped OS better. It is a set of Claude Code plugins: agents, skills, commands and hooks written in markdown, plus a few small scripts.

## Good first contributions
- A step in a skill that was unclear or wrong when you ran it: say what you expected and what happened.
- A new template or checklist that a role was missing.
- Support for another tool (an email provider, an analytics tool, a payment provider) inside an existing skill.
- Fixes to the install guide for your operating system.

## Before you open a pull request
1. **Turn on the safety check once:** `git config core.hooksPath .githooks`. It blocks commits that contain keys, tokens, email addresses, phone numbers or local paths.
2. **Run the hook tests:** `bash plugins/bootstrapped-os/hooks/test-hooks.sh`. All must pass. Changes to the safety hooks need a new test case.
3. **Keep the autonomy rule:** agents read, draft and propose; they never send, publish, deploy, merge, migrate, pay or delete without the founder. A change that weakens this won't be merged.
4. **Write like the rest of the pack:** short sentences, plain English, one idea per line, no buzzwords, no em dashes.
5. **No private data, ever:** no real customer, merchant or buyer names, no one's revenue but your own, no screenshots with personal data. Use made-up examples.

## What stays out of this repo
Measured knowledge (lesson sets, directory checks, funding lists, benchmarks) lives in the Bootstrapped core, which members connect with a key ([CONNECT.md](CONNECT.md)). If you found a directory, grant or lesson that works, open an issue with the "knowledge tip" template: if it checks out, it goes into the core for everyone.

## Pull requests
One change per pull request, with a short note on why. Say which skill or agent you ran it with and what you saw. Small and tested beats big.

By contributing you agree your contribution is licensed under the MIT licence of this repo.
