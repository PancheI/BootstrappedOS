# Security

Bootstrapped OS runs agents on your computer with access to your tools, so safety issues matter most.

## Report a problem privately
Use **GitHub → Security → Report a vulnerability** on this repository. Please don't open a public issue for a security problem.

Especially wanted:
- a way an agent can send, publish, deploy, pay or delete **without** asking you first (a gap in `plugins/bootstrapped-os/hooks/`);
- a skill that leaks data from your `knowledge/` folder somewhere it shouldn't go;
- secrets that could end up in a commit.

You'll get a reply within 3 working days. Fixes ship as a new version with credit to you, unless you prefer not.

## Your keys
Your `BOOTSTRAPPED_KEY` and any API keys belong in environment variables, never in files in your project. If a key leaks, revoke it at once (for the core: Account → Your Bootstrapped key → Revoke) and make a new one.
