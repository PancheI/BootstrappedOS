# Ops automation templates

Copy, fill, adapt.

---

## 1. Automation candidate scoring

```markdown
| Task | Times / month | Minutes each | Minutes / month | Risk (1-3) | Built-in option? | Verdict |
|---|---|---|---|---|---|---|
| | | | (arithmetic) | | | automate / draft only / checklist / leave |
```

**Risk:**
- **1 - reads only:** reports, summaries, checks, alerts to the founder.
- **2 - changes internal data:** copies rows between tools, tags contacts, updates a sheet.
- **3 - reaches the outside or money:** sends, pays, refunds, publishes, deletes.

**Verdict:**
- Risk 1, 30+ minutes / month -> **automate**.
- Risk 2, 60+ minutes / month, with an undo -> **automate after a watch week**.
- Risk 3 -> **draft only**: automate the gathering and drafting; the founder does the last click.
- Under 30 minutes / month -> **checklist**, not an automation.

Sort by minutes / month, highest first, risk 1 before risk 2.

---

## 2. Monitor brief

One per automation. Keep it as one section in `knowledge/trackers/automations.md`.

```markdown
# Monitor: <name>

**Question it answers:** <one line, e.g. "Did any payment fail since yesterday?">
**Source:** <tool + what it reads: "Stripe, failed charges, last 24h">
**Schedule:** <when, in which timezone>
**Runs in:** <Claude scheduled task / cron / GitHub Actions / Zapier / Make / n8n> - exactly one place
**Threshold:** <when it speaks up: "1 or more", "over 3 a day", "any new 1-star review">
**Output goes to:** <email to founder / a Slack channel / `knowledge/log/YYYY-MM-DD.md`>
**When nothing is found:** <it says "checked, nothing found" - never silent>
**When it fails:** <one line to the founder: what failed, when>
**Never does:** <sends to customers, pays, deletes, changes prices>
**Mode:** watch (week of <date>) -> on (from <date>, founder's go)
**Owner:** <founder / which AI role>
**Off switch:** <exact steps>
**Review on:** <date, monthly>
```

---

## 3. Safe-schedule rules (paste into CLAUDE.md)

```markdown
## Scheduled jobs
- Scheduled jobs read and report. Anything that writes runs only when I start it.
- One runner: daily chores in one job, in one place. Each part catches its own error and reports its own line.
- Write down how long the scheduler keeps the job alive. Session schedules die with the session and expire after 7 days.
- Off-minute schedules (09:23, not 09:00).
- Every send is claimed in a log before it goes (person + kind + reference), so a rerun sends nothing twice.
- Dry run by default; the real run needs a flag I type.
- Fail loud: a locked-out or failed run says so. "Ran, found nothing" is said out loud.
- Lists that page are read to the end ("all"), never the first page.
- Test-only switches (fake dates, test mode) are off in production.
- Data and schema changes go through migration files, local first, then production. No hand edits in production.
- Never delete from a store real customers depend on; add through the app's own API.
- No fast loops against social sites or inboxes. Bulk email through a sending service with a warm-up, never a personal inbox.
- Every job has an owner, an off switch and a monthly review date.
```

---

## 4. Runbook

Under the automation's section in `knowledge/trackers/automations.md`.

```markdown
# Runbook: <automation name>

**What it does:** <one line>
**Where it runs:** <tool + link to the job>
**Schedule:** <when> · **expires / needs renewing:** <date or "no">
**Inputs:** <which accounts or files it reads>
**Outputs:** <where results go>
**Normal run looks like:** <example of a good output, one line>

## If it fails
1. <first check: is the source tool down? did a login expire?>
2. <second check>
3. Still broken -> switch it off (below) and tell <owner>.

## Switch it off
<exact steps: "Zapier -> Zaps -> <name> -> toggle off">

## Undo (risk 2 only)
<how to reverse what it changed: "restore the sheet from version history">

## History
- <date> - created, watch mode
- <date> - turned on (founder's go)
- <date> - changed: <what, why>
```

---

## 5. Automations list (the top of `knowledge/trackers/automations.md`)

```markdown
| Automation | Risk | Runs in | Owner | Last real output seen | Next review |
|---|---|---|---|---|---|
| | | | | <date> | <date> |
```

Monthly: anything with no output read in 30 days -> ask the founder: keep, slow down, or remove.
