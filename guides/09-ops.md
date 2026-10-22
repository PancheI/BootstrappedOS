# Chief of Staff: repeat work and due diligence

**The repeat tasks of your week, found and scored, and the safe ones automated.** Each automation gets a brief, a runbook and an off switch. Before you trust a big client or supplier, you get a one-page check. You decide.

Starts once you have customers. At $0, `/day0` leaves it out of your rhythm.

## Set it up (20 minutes, once)
1. Type: "Use ops: here is what I do every week: <your list>. What should I automate first?"

   **You should see** each task scored: times a month × minutes = minutes a month, and a risk from 1 (only reads) to 3 (sends, pays or deletes). The top 1-3 come with a short brief.
2. Turn on the built-in settings of tools you already pay for first. Then pick one read-only automation.

## Every month (15 minutes)
1. A new automation runs in watch mode for one week: it reports what it would do and does nothing.
2. Say `go` to turn it on. Run it with Claude Code scheduled tasks or cron.
3. Once a month, ask: "Did anyone read each automation's output?" Turn off what nobody reads.

## Before a big deal (30 minutes)
Type: "Use ops: check <company>."

**You should see** a one-page memo: the decision first (yes, yes with one condition, or no), then each check with a link, or what was searched and not found.

## What a good result looks like
```
Weekly sales count:        4 × 20 min = 80 min/month, risk 1 → automate
Wholesale orders to sheet: 120 min/month, risk 2 → the shop's own integration, one watch week first
Download-link replies:     risk 3 → turn on the shop's built-in resend; replies stay drafts
```
Due diligence: "Yes, with a condition. Real company, pays on day 60, but 60-day terms on half our revenue needs a deposit. One ask: a 3-month pilot with 30% upfront."

## One memory
Automations are listed in `knowledge/trackers/automations.md`, checks in `knowledge/checks/`. Nothing runs that nobody knows about.

## Avoid
- **Automating anything that sends, pays or deletes.** Automate the gathering and the draft; keep the last click.
- **The same job running in two places.** One owner, one schedule.
- **Deciding on a feeling.** Every check needs a link or says where it searched.

**Files behind this role:** `plugins/bootstrapped-os/skills/ops/` (scoring, runbook and due-diligence templates in `references/`)
