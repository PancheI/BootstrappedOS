# Architecture: the skeleton

Bootstrapped OS is a skeleton you build on. Add a role, a skill, a command or a module without editing the rest. This page is the contract that makes that work. Every file in the repo follows it.

## The layers

| Layer | Lives in | Owns | Changes when |
|---|---|---|---|
| **Your knowledge** | your project: `CLAUDE.md`, `knowledge/` | your facts, rules, decisions, customers, numbers | you work; it always wins |
| **Bootstrapped core** (members) | an MCP server, `bootstrapped-core` | the author's plays, lessons, directories, funding, evidence | weekly, with no update on your side |
| **The method** (this repo) | `plugins/` | roles, steps, gates, templates | a release |

The order matters. Your files beat the core, and the core beats the method's defaults. A skill never hard-codes a number that belongs to you or to the author. It reads `knowledge/` or asks the core.

## One place for each thing

| Thing | The only place it is written | Everything else |
|---|---|---|
| Roles, agents, skills, commands, models | [`OS.md`](OS.md) | links to OS.md |
| The `/start-from-zero` stages | [`plugins/bootstrapped-os/shared/stages.md`](plugins/bootstrapped-os/shared/stages.md) | names the stage, never its number |
| What every agent reads first, writes after, and the core line | [`shared/agent-contract.md`](plugins/bootstrapped-os/shared/agent-contract.md) | one line: "Follow the agent contract." |
| What needs the founder's yes, and what "go" means | [`shared/gates.md`](plugins/bootstrapped-os/shared/gates.md) | one line: "Gates: see shared/gates.md." |
| The `knowledge/` folder tree | [`shared/knowledge-tree.md`](plugins/bootstrapped-os/shared/knowledge-tree.md) | uses those paths, no others |
| Which model for which job | [`skills/chief-of-staff/references/model-routing.md`](plugins/bootstrapped-os/skills/chief-of-staff/references/model-routing.md) | agent frontmatter holds the default only |
| The author's own numbers (days, cost, revenue) | [`example-my-setup.md`](example-my-setup.md) | never repeated; link to it |
| The author's plays and evidence | the Bootstrapped core | skills ask `recipes` / `evidence`; no private figures in the repo |

When two files disagree, the file in the middle column is right. Fix the other one.

## The shapes

Copy a template from [`templates/`](templates/). Don't invent a new layout.

- **Agent** (`agents/<role>.md`): [`templates/new-agent.md`](templates/new-agent.md). Frontmatter `name`, `description` (`[Department]` + the job, no stage number), `model`. Then the job, Skills, Tools, the contract line, Done means, Rules and why, How agents fail, Hand back.
- **Skill** (`skills/<name>/SKILL.md`): [`templates/new-skill.md`](templates/new-skill.md). The job, references, The process (numbered), Decision rules, Quality bar, Never, Shared knowledge, Bootstrapped core.
- **Command** (`commands/<name>.md`): [`templates/new-command.md`](templates/new-command.md). Uses one skill or agent, Read first, numbered steps, Hand back, the gates line.
- **Guide** (`guides/NN-<role>.md`): [`guides/_template.md`](guides/_template.md). Outcome, set it up, you should see, the routine, one real example, one memory, Avoid.

## Adding something

- **A skill:** copy `templates/new-skill.md` into `skills/<name>/SKILL.md`. Add one row to OS.md. Nothing else changes.
- **A role:** copy `templates/new-agent.md`. Add one row to OS.md and one guide. The Chief of Staff routes by OS.md.
- **A stage:** edit `shared/stages.md` only.
- **A module:** a new folder under `plugins/` with its own `.claude-plugin/plugin.json` that says `Requires: bootstrapped-os`, plus one entry in `.claude-plugin/marketplace.json`. Modules use the core's `shared/` files. They don't copy them.

## Safety

The hooks in `plugins/bootstrapped-os/hooks/` enforce `shared/gates.md`. Change one, change the other, and add a test case to `hooks/test-hooks.sh`. Every commit runs `scripts/check-sensitive.sh`, so no keys, personal data, local paths or private business figures get in.
