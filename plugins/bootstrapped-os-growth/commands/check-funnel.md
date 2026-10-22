---
description: Find where people drop off between visit and payment, from your funnel events and replays, and one fix.
---

Use the `head-of-growth` skill (growth module) with the core `numbers` skill for $ARGUMENTS.

**Read first:** `knowledge/numbers.md`, `knowledge/decisions.md`, `knowledge/pages/home.md`.

1. **Name the source.** Read the events and replays from PostHog through its MCP if it's connected, or from your analytics export. If none is connected, say so in the first line and ask for an export.
2. List the funnel events you find, for example: sign-in, free vs paid choice, price shown, checkout opened, closed or slow, paid, the "why" reason. Name any step with no event; adding it is the first fix.
3. Last 14 days, with your own country, test accounts and agent browser checks excluded. Give counts per step. Show a % only when a step has 20 or more people.
4. For checkout closes: seconds from open to close, and whether anything was typed. Count slow or failed loads apart from closes.
5. Quote every "what stopped you?" answer word for word. Note whether mobile closes ever reach that question.
6. Watch 3 engaged and 2 fastest-leaving replays at the biggest drop, with the skill's five replay questions.
7. Point at the biggest drop and one fix, and what it replaces. Under about 50 real visitors a week, the fix is traffic.

Run it daily for 5 minutes during a launch, weekly after. The author reads his analytics every day and asks what on the page should change.

**Hand back:** the counts per step, the biggest drop, the quoted reasons and one proposed fix. Written to `knowledge/checks/<date>-funnel.md`. Gates: `shared/gates.md`.
