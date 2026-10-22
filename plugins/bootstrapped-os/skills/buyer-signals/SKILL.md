---
name: buyer-signals
description: Head of Sales. Finds 3-5 real people who asked this month, in their own words, for what the founder sells (X, Reddit, Hacker News, Indie Hackers, forums, groups), each with the link, date, quote and fit, plus a suggested angle and the options to mention. Hands back a one-page report. The founder writes every reply. Use for "find buyers", "buyer signals", "who is asking for this", "where are my customers", "leads for my product", a daily buyer report.
---

# Buyer signals

The job is to find **who** to talk to, not to talk for the founder. A signal is a real person, in a post you can link to, saying in their own words that they need what this product does. The author's rule: "I'm not gonna use AI for writing messages, I'm gonna write the messages myself, but I'm gonna use AI to figure out to whom." Three real signals beat ten weak ones.

**References:** `references/report-template.html` (the one-page report, filled each run).

## The process
1. **Read the input from `knowledge/`.** Ask only what's missing (max 3 questions):
   - what you sell, in the buyer's words, and the price;
   - who buys it: one buyer, one job, one painful moment;
   - where they are: country and language (a buyer in a small country means groups in that language too);
   - your rules in `rules.md` (for example "only agencies", "no price in the first reply").
2. **Search the last 30 days, read-only, at human speed.**
   - **X:** the pain in the buyer's words ("looking for", "any tool", "recommend", "alternative to <competitor>"), Latest tab.
   - **Reddit:** the subreddits the buyer reads. Reddit's search RSS feed works; its JSON endpoint returns 403.
   - **Hacker News, Indie Hackers, Product Hunt discussions:** "Ask HN", "what do you use for".
   - **Niche forums and local sites** in the buyer's language.
   - **Groups (Telegram, Discord, Slack, LinkedIn, Facebook):** only through the founder's own logged-in browser, read-only, or hand the founder the search to run. Never automate these accounts.
3. **Keep only real signals.** One linkable post, dated in the last 30 days, the need in the person's own words. Not a place ("this subreddit"), not an older thread, not a competitor's customer with no stated need, not a scraped list. Stop at 5 good ones or about 15 minutes.
4. **For each signal, write:**
   - **Who and where:** role, country, platform, date. Handle and link for the founder only.
   - **What they said:** a short quote, under 15 words.
   - **Why it fits:** one line.
   - **Suggested angle:** one fact or question the founder could open with.
   - **Options to mention:** 2-3 tools that solve it, competitors included, the founder's own product last with a disclosure (see the reply style below).
   - **History:** have we talked before? Check `customers.md`.
5. **Fill the report** from `references/report-template.html` and save it as `knowledge/reports/<YYYY-MM-DD>-buyer-signals.html`. Open it for the founder.
6. **Log and hand back.** One line per person in `customers.md` (date, who, link, status "found"). Tell the founder in 3 lines: how many found, the best one, who to write to first.
7. **Follow-ups** use the cadence in `sales-outreach` (section "Follow-ups"). Don't set a different one here.

## The author's reply style (guidance for the founder, not a script)
- **Help first.** Answer their question even if they never buy.
- **Give options.** Name 2-3 tools that would work, competitors included.
- **Your own product last,** with a disclosure: "I'm the founder of X, so I'm biased."
- **Their language, 2-3 lines.** No hype, no "game-changer".
- The founder writes it. If the founder asks for a draft, write one and mark it as a draft.

## Decision rules
- **Nothing found?** Say "no signal found" and list what you searched. Never pad.
- **Older than 30 days, or no quote you can link?** Not a signal. Drop it.
- **Already in `customers.md`?** Show the history first; the founder decides whether to write again.
- **A group behind a login, CAPTCHA or anti-bot check?** Stop and hand the search to the founder.
- **The follow-up is where it closes.** The author says most of his paying customers came from DM follow-ups (his statement, not measured). Finding the person is step one.

## Quality bar
- [ ] 3-5 signals, each with a working link, a date in the last 30 days and a quote.
- [ ] Each has a one-line fit, a suggested angle and the options, with the founder's product last.
- [ ] No drafted replies unless the founder asked.
- [ ] History checked in `customers.md` for every person.
- [ ] The report says what was searched and that nothing was posted or sent.

## Never
- Post, comment, reply, DM, like, follow or connect for the founder.
- Write the reply unless the founder asks for a draft.
- Collect emails or phone numbers beyond what's public in the post.
- Invent a need, quote, date or link.
- Bulk-scrape a platform or get past an anti-bot check.

## Shared knowledge
**Read first:** `CLAUDE.md`, `knowledge/positioning.md`, `knowledge/customers.md`, `knowledge/rules.md`. **Write after:** `knowledge/reports/<date>-buyer-signals.html`, one line per person in `knowledge/customers.md`, search terms that worked in `knowledge/ideas/signals.md`. Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Ask `recipes` (area `distribution`) before step 1 ("find buyers asking for <what you sell>") and `lessons` (theme `customers-and-sales`) at the decision rules. If it isn't connected, carry on with this method.
