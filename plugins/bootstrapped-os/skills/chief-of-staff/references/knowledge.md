# The shared knowledge base (kept by the Chief of Staff)

The AI team forgets everything between sessions except what is written down. Write it once, in the right place, short enough to read every time.

Templates: `knowledge-templates.md` · Worked example: `knowledge-example.md` · The folder tree: `shared/knowledge-tree.md` (the only paths any role uses).

## Which knowledge wins
Use three sources, in this order:
1. **The founder's own `knowledge/`** (their customers, decisions, rules, numbers) and their `CLAUDE.md`. Facts about their business and their rules always win.
2. **The Bootstrapped core** (general lessons, directories, programmes, the author's results). It fills what their files don't cover. Say how fresh each answer is.
3. **The method and live sources** (official pages, live pricing pages) when neither has it.

When the core disagrees with the founder's rule or numbers, follow the founder, mention the difference once in one line, and ask whether to save the core's point in `knowledge/rules.md`. Never overwrite their files with core answers.

## Where things go

| What | Where | Read by |
|---|---|---|
| A rule for every task ("never send without my go") | `CLAUDE.md` | every role, every session |
| A rule learned for one topic | `knowledge/rules.md` (one heading per topic) | the role that topic belongs to |
| A whole repeatable process or saved answer | `knowledge/how-to/<task>.md` | every role, people |
| A decision (what, why, what would change it) | `knowledge/decisions.md` | every role, before asking the founder anything |
| A customer or lead conversation | `knowledge/customers.md` | sales, support, customer emails, content |
| This week's numbers | `knowledge/numbers.md` | Chief of Staff, CFO, content |

## The format: rule, why, how to apply
Each rule is short and carries its reason, so a session can judge edge cases. An invented example, in `knowledge/rules.md` under "Customer emails":

```markdown
### Keep emails short (since 3 Mar)
Emails: 40-80 words, one button, no repeated story.

**Why:** the founder, 3 Mar: "nobody reads past the second line" - after three
drafts in a row each added another paragraph.

**How to apply:** when you add something, cut something; re-read the whole
email and remove duplicates before showing it. Related: Email tone.
```

And the index every session reads first, one line per entry (`knowledge/INDEX.md`):

```markdown
- [Keep emails short](rules.md#keep-emails-short) — 40–80 words + one button; replace, don't append (since 3 Mar)
- [Studio price](decisions.md#2026-03-10) — one plan, $29/mo; yearly = 10x monthly (since 10 Mar; replaces the two-plan offer)
- [Batch deploys](rules.md#batch-deploys) — check locally, collect, deploy only when asked
```

What makes it work:
- **The index line states the rule itself,** so the line alone is often enough.
- **Why = the founder's words in quotes + the date + what went wrong.** The incident lets the AI judge edge cases; a bare rule gets applied blindly.
- **Replacements show in the index line** ("since 10 Mar; replaces ..."), so an old rule can't come back from an old file.
- **Related links** connect rules that pull against each other (short vs. warm; fast vs. checked).

## Decisions go into the skill the same turn
A decision that lives only in a planning file gets missed: the next session follows the skill and builds the old version. Planning files don't load in a new session; skills and `knowledge/` do. So when the founder decides a format, address, rule or workflow, edit the skill (or `CLAUDE.md`) **and** write it into `knowledge/` in the same turn, with the date and their words.

At the end of an ops day, write a retro in `knowledge/log/<date>.md`: miss, cause, fix, and which file the fix went into.

## Step by step: logging a decision (`/log-decision`)
1. Write it in the decision format: date, decision, why, what would change it, what it replaces.
2. Missing "why" or "what would change it"? Ask once. Those two lines are the point.
3. Search the log for an older decision on the same topic. If one exists, mark it "Replaced by <date>".
4. Does the decision change how the team works? Update the matching skill, `knowledge/rules.md` or `CLAUDE.md` line **in the same session**.
5. Show the founder the entry and the files you changed. Save after their OK.

## Step by step: turning a correction into a rule
1. Spot it: the founder corrected the same thing twice, or said "always", "never" or "remember".
2. Write it as **rule + why + how to apply** (template).
3. Pick the place with the table above. Default to `knowledge/rules.md`; `CLAUDE.md` only if it applies to nearly every task.
4. Check for a clash with an existing rule. Mark the old one replaced. Newer wins.
5. Tell the founder in one line which file changed.

## Weekly cleanup (Friday, 10 minutes)
Use the cleanup routine in the templates: merge duplicates, mark replaced rules, delete dead ones, keep `CLAUDE.md` to one screen, check `knowledge/INDEX.md` points at real files, back everything up.

## Decision rules
- **Said twice -> write it down.** Needed in every task -> `CLAUDE.md`. A whole process -> a skill or a how-to page.
- **One rule, one entry; one process, one checklist.** Ten small rules that are really steps of one task get merged into its how-to page.
- **Approval words are rules too.** "go" = build and show locally; only "deploy" or "ship" goes to production (`shared/gates.md`). Write the founder's words down the first time they're misread.
- **Measured beats theory.** A rule backed by a real result outranks general advice. Note the evidence.
- **`CLAUDE.md` over one screen?** Move topic rules into `knowledge/rules.md` and leave a one-line pointer.
- **Customer notes:** what they said and the next step. No opinions.

## Quality bar
- [ ] Every decision has a "why" and a "what would change it".
- [ ] Every rule has a why and a "how to apply".
- [ ] No two rules contradict; replaced rules say "Replaced by <date>".
- [ ] `CLAUDE.md` fits on one screen.
- [ ] `knowledge/INDEX.md` has one line per entry and no dead links.
- [ ] Durable files live in the project or the notes tool, never in a scratch or temp folder.
- [ ] Backed up (a private git repo works).

## Never
- Never save a decision without showing it to the founder first.
- Never delete an old rule silently. Mark it replaced, with the date.
- Never re-ask a decision that is already logged.
- Never store passwords, card numbers or private customer data in `knowledge/rules.md`.
- Never give the AI team the whole workspace when one page answers the question.
- Never keep the only copy of something in a temp folder.

## Rules behind this
- The core's `lessons` (theme `memory-and-rules`): write it into the skill the same day, never re-ask a settled decision, one checklist per task, mark the old rule replaced, measured evidence beats theory, keep durable files out of scratch folders.
- The free starter rules in [`lessons/claude-md-starter.md`](../../../lessons/claude-md-starter.md) use the same pattern: one rule, one line on why.
