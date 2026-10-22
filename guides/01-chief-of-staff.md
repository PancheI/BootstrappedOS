# Chief of Staff

**Your right hand.** It knows your business, tells you each morning what matters, and hands every job to the right role. You answer with a number.

## Set it up (30 minutes, once)
1. Open your company folder in the terminal and start Claude:
   ```
   cd ~/my-company
   claude
   ```
2. Type `/day0`.

   **You should see** a table of your tools (✅ or ❌), with the line to fix each ❌.
3. Answer its 5 questions. It asks them one at a time and waits for each answer:
   - What kind of business? (software, agency or services, online shop, creator or coach, other)
   - Which tools do you use for email, payments, analytics, notes and social?
   - Your goal this month? (first customers, more revenue, save time, launch something, grants and credits)
   - How do you ship? (code, a no-code site builder, you don't)
   - Revenue today? ($0, under $1k a month, more)
4. Read the `CLAUDE.md` it shows you, and say yes to save it (or tell it what to change).

   **You should see** it create your `knowledge/` folder, recommend the modules and connectors that fit your answers (with the exact install lines), say which roles start now, and give you three first things to do.

## Every day (5 to 30 minutes)
**At $0 revenue,** start with `/first-customers`. That is your daily routine until the first payments come in. Then `/weekly-review` on Mondays and `/grants` once a month.

**Once you have customers:**
1. Type `/morning`.

   **You should see** a short brief: yesterday's numbers, money at risk, who is waiting on you, and 3 things for today.
2. Type `/run-ops` when you want the drafts done.

   **You should see** a numbered list of proposals. Nothing happens yet.
3. Reply with the numbers you approve, for example `go 1 3`.

## What a good morning looks like
```
1. Reply to the customer waiting since Friday          → Head of Support
2. Draft the email for the expired card                → Head of Support
3. Add "what stopped you?" to the cancel screen        → Head of Engineering
Needs you: should the agency discount be 20% or 30%? My pick: 20%.
```
You type `go 1 2` and it drafts both. You send them.

## One memory for the whole team
`/day0` creates a `knowledge/` folder: your customers, decisions, rules and numbers. Every role reads it before a job and adds one line after. When Sales logs a reply today, Support already knows tomorrow.

Made a decision? Type `/log-decision` and say it in one line. It saves the decision and why, so nobody asks again.

## Avoid
- **A huge CLAUDE.md.** Keep it to one screen; put details in `knowledge/`.
- **Saying the same thing twice in chat.** Turn it into a rule in `knowledge/rules.md`.
- **"ok" is not "go".** It only acts on the numbers you type.

**Files behind this role:** `plugins/bootstrapped-os/skills/chief-of-staff/`, `plugins/bootstrapped-os/commands/day0.md`
