# Head of Growth (growth module)

**More of your visitors sign up and pay, and AI answers start naming you.** A page critique, a funnel check and an SEO panel. You pick the fixes.

**What the module adds:** two skills (head-of-growth for conversion, head-of-seo for search and AI answers) and the `/critique-page`, `/check-funnel` and `/seo-brief` commands. It needs the core plugin (`bootstrapped-os`); the launch side of Head of Growth is in the core ([06-launch.md](06-launch.md)).

## Set it up (2 minutes, once)
1. Install the core first ([INSTALL.md](../INSTALL.md)), then the module:
   ```
   claude plugin install bootstrapped-os-growth@bootstrapped-os
   ```

   **You should see** `✔ Successfully installed plugin: bootstrapped-os-growth@bootstrapped-os`.

## Every week (20 minutes)
1. Type `/critique-page` and your URL, for example `/critique-page https://yoursite.com`.

   **You should see** a 3-second test of the first screen, a check at 4 screen widths, and the 3 changes that would most raise sign-ups, worst first.
2. Type `/check-funnel`.

   **You should see** counts at each step from visit to payment, the biggest drop, and one fix. Under about 50 visitors a week, the fix is more traffic.
3. Type `/seo-brief`.

   **You should see** "named in N of 15" for 15 questions your buyers ask Google, Bing, Perplexity and ChatGPT, and a brief for the best opening.

Changing a page? Ask for 3 options: bold, middle and safe. Then pick one.

## What a good result looks like
```
Named in 2 of 15 (last week 1 of 15)
Best opening: "how do I take payments from abroad as a freelancer?"
  answered by generic lists, no page owns it
Brief: a page per question. The question as the heading, the answer in the first
  2 lines, a table, a visible date. Then ask to be added to 2 lists that rank for it.
```

## One memory
The SEO panel lives in `knowledge/seo/prompt-panel.md`, so each week is compared with the last. Page checks go to `knowledge/checks/`.

## Avoid
- **Redesigning on 10 visitors a week.** Get traffic first.
- **Adding sections instead of replacing them.** Name what the new block replaces.
- **Hiding the price.** Put it next to the button.

**Files behind this role:** `plugins/bootstrapped-os-growth/` (skills `head-of-growth`, `head-of-seo`; commands)
