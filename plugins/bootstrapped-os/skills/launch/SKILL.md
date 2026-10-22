---
name: launch
description: Head of Growth - get a product found by Google, Bing and AI assistants (ChatGPT, Claude, Perplexity, AI Overviews), then run launch week. The setup the author shipped (robots with named AI crawlers, llms.txt with one-sentence answers, .md twins, schema that matches the page, IndexNow), a weekly prompt panel, the dofollow links that move domain rating, the off-site footprint AI answers come from, and launch day. Drafts and fills; the founder submits. Use for launch week, Product Hunt, directories, backlinks, DR, "nobody knows we exist", "ChatGPT doesn't mention us", getting indexed.
---

# Launch

Pages and listings are table stakes. The author shipped every on-site item below on a 10-day-old domain and was named in none of his target AI prompts the next day. AI answers repeat what already ranks, plus Reddit threads and third-party "best X" lists. So do the setup once, in a day, then spend the time off-site. You draft and fill forms; the founder submits, posts and pays.

**References:** `references/listing-kit.md` (the facts block and the two pitches) · `references/launch-week-checklist.md` (day by day, D-7 to D+7).

## The process
1. **Setup: the GEO checklist.** Do all of it in one build. Each line is checkable.

   | # | Item | Exactly how | Check |
   |---|---|---|---|
   | 1 | robots.txt welcomes AI | `User-agent: *` + `Allow: /` + `Content-Signal: search=yes, ai-input=yes, ai-train=yes`. Then a named block: GPTBot, OAI-SearchBot, ChatGPT-User, ClaudeBot, Claude-SearchBot, Claude-User, anthropic-ai, PerplexityBot, Perplexity-User, Google-Extended, Applebot, Applebot-Extended, bingbot, CCBot, all `Allow: /`. Disallow only non-pages (`/api/`, `/cdn-cgi/`, page shells). A `Sitemap:` line. | Fetch the **live** file, not the repo one |
   | 2 | The CDN isn't blocking them | On one of the author's sites, Cloudflare's "Block AI Scrapers" served its own robots.txt and blocked GPTBot and Google-Extended while the repo file allowed them. It's a dashboard switch, not a file edit. | `curl -A GPTBot` returns 200 |
   | 3 | llms.txt built from the same lists as the pages | Generated at build time so it can't drift: a one-paragraph summary, every page with its one-line description, every post with its date and `.md` URL. Plus a **"One-sentence answers"** block: 5 questions buyers ask an assistant, each answered in one true sentence with a number. `<link rel="alternate" type="text/plain" href="/llms.txt">` in every head. | Answers match the pages word for word |
   | 4 | `.md` twins of the pages that should be quoted | Same words, no nav, form or footer. Served with `Content-Type: text/markdown` and `Link: <https://site/page>; rel="canonical"`. `<link rel="alternate" type="text/markdown" href="/page.md">` on the HTML. Tables stay tables; the answer-first lede goes on top. | Open `/page.md`: the answer is in line 1 |
   | 5 | Schema = visible text | JSON-LD only for what a reader sees on that page. Organization with `alternateName` (a short wordmark and a long name read as two entities without it) and `sameAs` profiles. Person with one `@id` reused everywhere. | Every schema string appears on the page |
   | 6 | Links crawlers can see | AI crawlers don't run JavaScript. His JS footer linked the money pages; the raw HTML didn't. A static footer fixed it. Page content inside `<article>`. | View source, not the DOM |
   | 7 | IndexNow on every deploy | A 32-hex key file at the root (`/<key>.txt`, never renamed or deleted), then POST the changed URLs to `api.indexnow.org/indexnow` with host, key, keyLocation and urlList. All sitemap URLs once, then only changed ones. | Response 200, logged |
   | 8 | Google and Bing told directly | Search Console: request indexing per new URL (reload the inspect page before each one). Bing Webmaster: submit the sitemap, run Site Scan; it flags titles over 70 characters. | Logged with the date |
   | 9 | Titles that get clicked | Under 70 characters, a number in the title, the answer in the description. | See step 6 |

2. **Prompt panel (baseline, then weekly).** Write 15 questions a buyer types into an assistant, each mapped to the page that should win. Run them in Google (AI Overview), Bing, Perplexity and ChatGPT. Log per prompt: named yes/no, which brands appear, which URLs are cited. Same questions every week; never change the panel to look better.
   - Look for the uncontested phrase. On his payments product, the clear win was a category phrase only one rival had claimed ("merchant of record for AI agents"). He wrote the definition page and was named first.
   - Openings are prompts where no specialist page ranks. His: "SaaS landing page examples bootstrapped" had no bootstrapped-specific list, and his swipe file was exactly that.
3. **Links that move domain rating.** Only **dofollow** links move DR. Piling up nofollow listings did nothing for his. Get the current list of free dofollow sites from the core's `directories`, and check each link yourself (Inspect, look for `rel="nofollow"`, `ugc` or `sponsored`). Log what you found, not what the site claims. What worked for him, in order:
   - **The product made the links first.** Sellers' buy buttons linked to checkout pages on his domain, so most of his early DR came before any deliberate link work (his reading; not checked domain by domain).
   - **One case study with real numbers** on a big founder community.
   - **Pages that rank:** country and answer pages, a calculator, IndexNow on every deploy.
   - **Then deliberate dofollow work:** free badge directories, data posts on dev.to and Indie Hackers, a GitHub Pages hub, a listing in a library's official docs, an open dataset with a "cite this" box.
4. **Off-site footprint (where AI answers come from).**
   - **One facts block, byte-identical everywhere** (`references/listing-kit.md`). Add each profile URL to `sameAs`. His order: LinkedIn company page, Product Hunt, Crunchbase, Indie Hackers product, X bio link, Wikidata only once 2+ independent sources exist.
   - **Reddit threads already on Google page 1.** Question title, 20-100 replies, under a year old, not locked. The founder replies from his own account: answers the question in full, mentions his product once at the end, says he built it. One such comment of his brought a wave of sign-ups (his estimate, about 50).
   - **The "best X" lists that rank** for your prompts: send the roundup note (`listing-kit.md`) to their authors, or leave a useful comment with a disclosure ("I run it, so take that into account").
   - **One case study beats every directory.** An Indie Hackers interview with his real numbers did more than any listing.
5. **Launch day.** Run `references/launch-week-checklist.md`. His Product Hunt plan (planned, not yet run): scheduled for 00:01 Pacific; a pre-launch forum thread a few days before, written as a question in the buyer's words; free launch, no promoted slot; reply to every comment within 15 minutes; never ask for upvotes; share in waves across time zones; badge on the homepage. One big event per day.
6. **Measure clicks, not rankings.** His bottleneck was **clicks**: most Google clicks were searches for his brand name, and comparison pages on page one got almost no clicks because the snippets talked about his product. He rewrote titles and descriptions to lead with the reader's answer, then waited a week before touching more pages.
   - Weekly: Search Console queries at positions 5-20 with impressions -> fix that page (answer first, the missing fact, the title).
   - Tag every link `?utm_source=<site>&utm_medium=directory|launch|community`. Count AI referrals (chatgpt.com, perplexity.ai) as their own source.
   - **Monthly: where did sign-ups actually come from?** Check before building more pages. For him, the homepage and brand searches brought most new users; all SEO pages together brought few.
   - **One lead box per content page, tagged `?src=seo-<page>`,** so you see which page brings leads, not just visits.

## Decision rules
- **Free listings only.** He turned down every paid one. Badge-gated dofollow is fine if the founder says yes: badges in static HTML, one "Listed on" row above the footer.
- **dev.to: one data post a day at most,** with `canonical_url` set to the original so Google credits the site.
- **The biggest lever is links the product makes.** A public page per customer and a badge that links back. Get listed inside the stack buyers start on: starter kits, auth plugins, framework templates. Founders pick a provider once, at setup.
- **Tag the product's own link** (`?ref=powered-by`). A share of the people who saw his checkout later visited his site, while directories sent about zero visitors.
- **Find where to list by scanning a top rival's customers' homepages** for launch badges and links, not from "dofollow directory" blog lists.
- **Original data gets cited.** He published a dataset (payment providers across 85 countries, CC BY, on Hugging Face and Kaggle) and a post on its headline number ("isn't available in 37 of 85 countries"). No listicle can copy it.
- **Curated "awesome" lists want outside proof first** (stars, reviews, press). Pitch them later.
- **Skip a directory owner's "sister" directories that each want a homepage badge.** That's a reciprocal-link pattern.
- **Most ranking "best X" lists are paid or guest posts.** Pitch the few independent ones with real numbers.
- **After the setup, every work block ships one off-site or reach item before another SEO page.** The author was told he "kept failing into the same loop" of pages and indexing requests.

## Quality bar
- [ ] Every GEO line checked on the **live** site, with the date.
- [ ] Prompt panel baseline logged before any change.
- [ ] Every listing's link type checked in-page, not taken from the site's claim.
- [ ] The facts block is the same on every listing; every number in it is in `knowledge/numbers.md`.
- [ ] Every link carries its UTM.
- [ ] The name field holds the name, read before the founder submits.

## Never
- Pay for a directory, upvotes, vote groups or new accounts voting.
- Submit forms, solve captchas or anti-bot checks, create accounts, sign in, pay or post. You fill and prepare; the founder submits.
- Trust a prefilled form. On one directory the tagline landed in the name box and the listing went live under the wrong name.
- Put anything in schema, llms.txt or a listing that the page doesn't say. No invented numbers, quotes or reviews.

## Shared knowledge
**Read first:** `CLAUDE.md`, `knowledge/decisions.md` (offer, price, who it is for), `knowledge/numbers.md` (every number in the facts block). **Write after:** every listing in `knowledge/trackers/launch.md` (site, link type as checked, cost, status, date, UTM); the facts block in `knowledge/how-to/listing-kit.md`; prompt panel results in `knowledge/seo/prompt-panel.md`. One line, dated. Never passwords or card numbers. Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Ask `recipes` (area `seo`) before step 1, `directories` (your product type, free only) at step 3, and `lessons` (theme `customers-and-sales`) at the decision rules. If it isn't connected, carry on with this method.
