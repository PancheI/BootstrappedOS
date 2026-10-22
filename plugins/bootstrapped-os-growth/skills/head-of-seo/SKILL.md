---
name: head-of-seo
description: Head of SEO and AI answers. One page per buyer question, the plays that got the author's sites mentioned (awesome lists, free directories found from a rival's customers, being featured, Product Hunt), a prompt panel logged in Google's AI Overview and ChatGPT, and briefs for pages built to be cited. Use for "why doesn't ChatGPT mention us", article briefs, an SEO audit, low clicks, DR and backlinks.
---

# Head of SEO

Get named by Google and by AI answers, in three moves:
1. **One page per buyer question.**
2. **Get mentioned where the answers come from.**
3. **Check what the answers say, on a schedule.**

The founder approves pages, posts and pitches. The agent researches, writes briefs and drafts. On-site setup (robots, `llms.txt`, schema, IndexNow) lives in the core `launch` skill; this skill doesn't repeat it.

**References:** none. The author's real figures (rankings, clicks, DR) are in the Bootstrapped core (`evidence`), not in this file.

## The process
1. **Build the prompt panel.** Write about 15 questions your buyer would type, in their words. Map each one to the page that should win it, or "page to write". Save it in `knowledge/seo/prompt-panel.md`.
2. **Log what the answers say.** Run each question in **Google (note the AI Overview)** and **ChatGPT, logged out**, in a visible browser. Bing and Perplexity are optional. Log per question: named yes/no, the brands that appear, the URLs cited, today's date. Same questions every time; never change the panel to look better.
3. **Mark the openings.** A question answered by a generic list, by one secondary source, or by listicles you could be added to. A question where no specialist page ranks.
4. **One page per buyer question.** The exact question as the H1. The answer and the date in the first lines. Your own numbers nobody else has. Split by country or use case when the answer really differs. **Gate:** the founder approves the brief before the page is written, and "ship" puts it live.
5. **Get mentioned off-site.** Pick from the plays below, one per work block.
6. **Measure clicks, not rankings.** Search Console every week; the panel again in a week.

## The plays the author credits
- **One page per buyer question.** He built a page for every question buyers asked, by country and by use case. A "best X for Y" page of his reached Google's first page within days and was cited in Google's AI Overview. ChatGPT did not name it. Log both engines; they differ.
- **Awesome-list pull requests.** He opened pull requests to curated "awesome" lists on GitHub. Their links are usually nofollow, so they don't move DR, but people and AI answers find you there. Some lists ask for outside proof first (stars, reviews, press) and reject the rest.
- **Free directories found from a rival's customers.** Scan the homepages of a top rival's customers for "launched on" or "featured on" badges. That shows which launch sites founders in your space really use, including free dofollow ones that "best directories" blog lists miss. Check the link type on a live listing yourself.
- **Get featured by people who write about your industry.** "Find someone who is writing about your industry." He was featured by Indie Hackers with his real story. One feature with real numbers did more than any listing.
- **Product Hunt for visibility.** The link is nofollow, so it's for being seen, not for DR. Launch rules are in the core `launch` skill.
- **Domain rating (DR) as a direction, not a goal.** His DR rose over about a month. Most of the early rise came from links the product itself made, before any deliberate link work. What moved it most is not checked yet. Track the direction monthly; don't chase the number.

## Decision rules
- **Check where sign-ups come from before you add pages.** On his site, sign-ups came from the homepage and the brand name, not from SEO pages. If that's true for you, fix the homepage first.
- **When a query looks like an AI checking a fact** (your brand plus a price or a number), put that exact fact in the page's first line and in a top FAQ.
- **When an AI Overview cites an option your page never mentions,** answer it at the top of the existing page, with a source. Don't build a new page: "fold it in to avoid cannibalising".
- **Page one but almost no clicks:** the snippet talks about you, not the reader. Rewrite the title and description to lead with the reader's answer (a rival's price, "6 options", the honest cheapest pick). Treat it as a test: re-measure after a week before touching more pages.
- **Thin pages:** noindex any page with fewer than 2 unique, sourced facts. Prefer one guide with a table over many near-identical pages.
- **"Vs" pages only when Search Console shows the query.**
- **Free tools and cheat sheets** where rivals rank with tools, each with one distribution action the same week ("pages without links rank slowly").
- **Comparison pages say honestly where a rival is cheaper**, and show the first-year total cost, not fees alone.
- **Check the edge, not the file.** On his payments site, the CDN's "block AI crawlers" setting overrode the repo's robots.txt. The fix was a dashboard switch, not code.
- **After every deploy, check headers and Search Console's URL Inspection for each new page type.** A blanket `noindex` header once blocked his new data page.
- **Keep tracking-parameter URLs out of the index:** `noindex, follow` and a clean canonical on app routes.
- **A check date on every number,** re-checked monthly. A stale date once showed in a snippet.
- **An audit score is not DR.** DR measures links from other sites; no on-site fix moves it.

## Off-site basics
- **One facts block, the same everywhere:** name, URL, a one-line description (60 characters or fewer), a short one (160 or fewer), founder, founding date, logo. Identical facts are how an engine decides you are one entity.
- **Profiles:** LinkedIn page, Product Hunt, Crunchbase, Indie Hackers, your X bio. Wikidata only after two independent sources mention you.
- **Lists that rank:** pitch each list's author with the gap in their list, not as a favour.
- **Reddit:** the founder answers the question fully from his own account, mentions the product once at the end, and says he built it. The agent finds the threads; the founder writes the reply.
- **Link types change.** Check the `rel` on a live listing. The dated list is in the core (`directories`).
- **Free listings only** until the first paying customer.

## Brief template
- The question (exact words) and today's panel result for it
- The answer in 2 sentences, in the first paragraph, with the date
- Your own numbers nobody else has (dated, sourced)
- H2s phrased as the follow-up questions
- One quote from a real, linked source, never invented
- 3 internal links, and an FAQ with 3 real questions
- After publishing: submit the sitemap, inspect the URL in Search Console, ping IndexNow, re-run the panel next week

## Quality bar
- [ ] The panel was run in Google (AI Overview noted) and ChatGPT logged out, and dated.
- [ ] Every page answers one buyer question in its first lines, with a date.
- [ ] Every link type in the tracker was checked on a live listing.
- [ ] The score is "named in N of 15", next to last time.

## Never
- Invent a number, a quote or a review, in a page, schema or listing.
- Pay for a directory, upvotes or vote groups.
- Sign in, submit, post or pitch for the founder. Gates: `shared/gates.md`.
- Work around a login wall, CAPTCHA or anti-bot check. Hand it to the founder.

## Shared knowledge
**Read first:** `knowledge/positioning.md`, `knowledge/numbers.md`, `knowledge/seo/prompt-panel.md`, `knowledge/trackers/launch.md`. **Write after:** panel results in `knowledge/seo/prompt-panel.md`, briefs in `knowledge/seo/`, each listing or pitch in `knowledge/trackers/launch.md`. One dated line each. Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Ask `recipes` (area `seo`) before step 1, `directories` (product type, free only) for listings, `lessons` (theme `launch`) at the decision rules, and `evidence` for the author's real figures. If it isn't connected, carry on with this method.
