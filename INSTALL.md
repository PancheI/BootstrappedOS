# Install Bootstrapped OS (10 minutes to install, 15 to set up, no coding)

Each step says exactly what to type and what you should see.

## You need
- A computer: macOS 13 or newer, or Windows 10/11.
- A paid AI plan that runs Claude Code (Pro or higher). The OS itself costs nothing extra.
- Nothing else. The OS is free and open source; a Bootstrapped Makers membership adds the knowledge core (optional, see CONNECT.md).

Never used a terminal? Read the official 2-minute [terminal guide for new users](https://code.claude.com/docs/en/terminal-guide) first. A terminal is just a window where you type a command and press Enter.

## 1. Install Claude Code (3 min)
Open **Terminal** (Mac: press Cmd+Space, type "Terminal", Enter) or **PowerShell** (Windows: Start menu, type "PowerShell", Enter). Paste one line and press Enter:

- Mac: `curl -fsSL https://claude.ai/install.sh | bash`
- Windows (PowerShell): `irm https://claude.ai/install.ps1 | iex`

Then type `claude` and press Enter, and sign in with your AI plan in the browser window that opens. Type `/exit` when you're back.

**You should see** a version when you type `claude --version`, e.g. `2.x.x (Claude Code)`.
**`claude` not found?** Close the terminal, open a new one, try again. Still nothing: [install troubleshooting](https://code.claude.com/docs/en/troubleshoot-install).

## 2. Add Bootstrapped OS to Claude (1 min)
In the terminal, paste these two lines, one at a time:

```
claude plugin marketplace add PancheI/BootstrappedOS
claude plugin install bootstrapped-os@bootstrapped-os
```

**You should see:**
```
✔ Successfully added marketplace: bootstrapped-os
✔ Successfully installed plugin: bootstrapped-os@bootstrapped-os (scope: user)
```
Claude keeps its own copy, so there is nothing to unzip or keep in a folder.

## 3. Connect the Bootstrapped core (members, 2 min, optional)
Members put their key in one environment variable and the agents use the author's lessons, directories, grants and results while they work: [CONNECT.md](CONNECT.md). Skip this and everything still runs on the method alone.

## 3b. Optional: install the tools the author uses (5 min)
The same plugins and connectors the author runs (Superpowers, code review, GitHub, Supabase, PostHog, Chrome DevTools, Resend, Vercel, AgentaOS and more):
```
git clone https://github.com/PancheI/BootstrappedOS ~/bootstrapped-os
bash ~/bootstrapped-os/setup/setup.sh
```
Then inside Claude Code, type `/mcp`: a list opens; pick each service and sign in in the browser. Type `/chrome` to connect the Claude in Chrome extension ("Enabled by default"). Your agents check pages in that visible Chrome.

## 4. Open your company folder and run /day0 (15 min)
Make one folder for your company (or use your website's code folder). In the terminal:

```
cd ~/my-company
claude
```
Then type `/day0` and press Enter. It asks 5 short questions, writes your `CLAUDE.md`, creates your `knowledge/` folder and gives you three first wins. Commands may show as `/bootstrapped-os:day0`; both work.

**At $0 revenue,** your first win is `/first-customers`: Day 0 gives you your buyer, the problem in their words and a price.

What to do on your first day, step by step: [guides/01-chief-of-staff.md](guides/01-chief-of-staff.md).

## Design kit (optional, free, recommended)
The Head of Design runs these if they're installed (the author's own landing-page process). They're by their authors, not part of this pack; install them from their pages:
- **impeccable** (Apache-2.0): github.com/pbakaus/impeccable
- **taste-skill**: github.com/Leonxlnx/taste-skill
- **frontend-design** (Anthropic, Apache-2.0): github.com/anthropics/skills
- **copywriting**: github.com/coreyhaines31/marketingskills
- **page-cro**: github.com/openclaudia/openclaudia-skills

## Add a module later (optional)
```
claude plugin install bootstrapped-os-software@bootstrapped-os   # you build software
claude plugin install bootstrapped-os-growth@bootstrapped-os     # you sell from a website
claude plugin install bootstrapped-os-video@bootstrapped-os      # you make videos
```

## Update to a new version
```
claude plugin marketplace update bootstrapped-os
claude plugin update bootstrapped-os@bootstrapped-os
```
What changed: [CHANGELOG.md](CHANGELOG.md).

## Is it safe?
Nothing sends, publishes, pays, deploys or deletes without you saying yes. See for yourself: [guides/00-how-agents-stay-safe.md](guides/00-how-agents-stay-safe.md) shows how to run the gate tests in two commands.

Stuck? Open an issue on GitHub, or bring it to the next live workshop (bootstrappedmakers.com).

## Advanced: watching a run
Run `/start-from-zero` in a normal Claude Code window and you see every stage live; `knowledge/progress.md` shows where it is at any time. For a run started in the background with `claude -p ... --output-format stream-json --verbose > run.jsonl`, open a second terminal: `python3 ~/bootstrapped-os/setup/watch-run.py run.jsonl`.
