---
name: idea-finder
description: Niche idea finder - find a startup idea from a real, linked problem and narrow it to a wedge (one buyer, one job, one painful moment), never a "platform for everyone". The idea stage of /start-from-zero. For solo bootstrapped founders, any country. Use for "startup idea", "what should I build", "find a niche", "niche gap", "validate my idea", "is this idea good", "my idea is too broad", "who would pay for this", "I have skills but no idea", "pick between my ideas".
---

# Idea finder

You find one wedge worth a week of selling: **one buyer, one job, one painful moment**. It has to be backed by strangers who said it in their own words at a link, and by somebody already spending money on a bad fix.

This is the author's own method. It comes from the four months he spent at $0 on a broad idea, and the month it then took to find the wedge that paid. Each rule names the run that taught it. The founder picks the wedge; the agent finds, checks and scores.

**No linked signal = no idea.** Interest is not a signal. His broad version got plenty of replies and a popular post, and it made $0.

**References:** `references/signals.md` (grades, the inclusion rule, decay, which channels gave signal vs noise) · `references/wedge.md` (narrowing, the "said vs pitched" count, follow the money) · `references/scoring.md` (scorecard, kill rules, the two kill tests) · `references/output-template.md` (the one-page brief).

## The process (every session)
1. **Intake, once, in one message.** Save it to `knowledge/founder.md` and skip anything already there.
   - What work have you done for years, and what do outsiders get wrong about it?
   - Your rough idea, however vague ("something for X that does Y").
   - Who you can reach this week, and roughly how many (a community, past clients, an audience).
   - What you were turned down for, overcharged for, or did by hand in that work. (His wedge was this answer: the card processors turned him down, then told him to open a company abroad.)
   - What you won't do.
   - If you already have users or sign-ups: where is the data? Sign-ups by country, who paid, what people asked on calls. This decides more than any search.
2. **Read your own data before the web.** The founder's own history decides more than any search.
   - **Where to look:** earlier projects one folder up, their docs (plans, pipelines, pitch notes) and their payments dashboard (read only). Their Claude session logs (`~/.claude/projects/`, `memory/`) can help too, but **ask first**, then grep the founder's own turns only; never load whole files.
   - **What to write:** `knowledge/founder-history.md`: what was tried, what failed and why, who replied, who paid, objections in their words, and the founder's unfair assets.
   - **Where to start the web search:** from the segment that already pays the founder. If anything is live, count who **paid**, not who signed up, and where they are. The segment that pays is area 1, even when the pitch is aimed elsewhere. In the Oct 2026 live run, the web-only pass was called "superficial" because years of the founder's own work sat one folder up.
3. **Name the target before you search.** If the history shows the founder already runs a business in this domain, a wedge may simply restate it. Ask once, as an AskUserQuestion with these three options, and save the answer to `founder.md`:
   - **(a) A new product on the founder's existing assets** (rails, customers, reviews), aimed at a problem of the segment that already pays them. Recommend this one by default.
   - **(b) A new wedge for the existing business,** for example the approved customers who never got a buyer.
   - **(c) A clean start,** as if there were no history.

   In the Oct 2026 live run, the research and positioning agents spent two rounds on a problem the founder's existing business already solved, before anyone read the history.
4. **Write the inclusion rule before you search** (`signals.md`). Say who counts as the buyer, what sentence counts as the need, the date window, and one entry per person. His creator-proof run used: "the poster made the work, and asks how to protect, prove, timestamp or register it before sharing it, or their own work was taken and the problem is showing it is theirs."
5. **Set the pain bar before you hunt.** A problem enters the list only if all four hold: 5+ different buyers state it in their own words inside the window; a measurable loss per incident (money or hours); it recurs (monthly or more); and someone already pays for a bad workaround. In the Oct 2026 live run, the first wide pass let in problems that cleared the evidence bar but not the pain bar, and the founder didn't want any of the three survivors.
6. **Go wide, then narrow.** List 6-10 distinct problems inside the founder's domain (different buyers, different moments), led by what their history shows, before going deep on any. The rough idea is one of them. Test it; don't defend it. In the Oct 2026 live run, going deep on one guess first cost three re-runs.
7. **Hunt by channel, at human speed** (channels from `signals.md` and the core). Search for first-person failure phrases in quotes, the competitor's name plus "rejected / denied / suspended / frozen", and the buyer's own language in their local communities. Read the comments as well as the titles: his count went from 55 to 76 to 396 once comments and two more channels were added.
8. **Log every signal** with its link, date, exact quote, role, today's fix, intent (direct / problem), age (hot / warm / cooling / stale) and grade. Check each quote against the source text before it goes in.
9. **Loop until dry.** Stop a channel when a round adds fewer than 5 qualifying people. A small total means the search was too narrow, not that demand is small.
10. **Count what they said, not what you pitched** (`wedge.md`). If the founder has had calls, sort the reasons into stated (their words), stated weak (a call-note paraphrase) and inferred. A reason you raised on the call doesn't count. Founders are often surprised: the reason they pitch is rarely the reason buyers state.
11. **Cluster and narrow.** A cluster needs 5+ A/B signals from different people hitting the same moment. Write the wedge line: "[who] who [job], at [moment], when [what goes wrong]."
12. **Find who pays today, and whether there's a gap.** Name the current fix and its price, read from a live page and dated. Workarounds count: a company abroad, a relative's account, a freelancer, an hour every Friday. Then check the problem isn't already solved: the incumbent, a free plugin, a recent upstream release (changelogs, closed GitHub issues), a generic AI chat answer, and the cheapest commodity workaround with its cost (a US company plus Stripe, Payoneer, a relative's account). The founder, on why access alone was weak: "I can register a co if I'm big and use stripe; smaller ones dont make money anyway." Verdict per problem: covered, partly covered (name the gap) or open gap. It counts in the score.
13. **Have it attacked, then score, kill, pick one** (`scoring.md`). The `idea-critic` agent attacks every candidate before the founder sees it. **Then a gut check:** show the founder the round-1 survivors in one line each and ask whether they would spend a year on any of them. Only the ones they want get a round-2 fix and a second critic pass. If they want none, hunt again in new segments with the pain bar. Don't polish problems the founder doesn't care about. Take the highest score that passes every kill rule. On a tie, take the one whose buyers the founder can reach soonest.
14. **Set this week's kill test** and write the brief (`output-template.md`). He used two tests. One: 30 one-sentence emails to people already paying for a workaround; 5 replies means the wedge is real, 1 means it isn't. Two: one demand post, read with the table in `scoring.md`.
15. **Hand over.** The first 20 people go to `sales-outreach` as conversations. The first price goes to `pricing-audit` once someone says yes.

## Decision rules (each one from a real run)
- **Sign-ups show interest; payments show the wedge.** Rank areas by who paid. His free pricing review got almost no users, while the access problem brought his first sales, so the review went from the headline to a feature.
- **Money came from a segment you didn't target:** follow it before arguing with it. His pitch was for SaaS, but most of his volume came from a few service businesses. That opened the "service -> package -> tool -> SaaS" path in `wedge.md`.
- **The founder's customer profile lists several buyer types:** it is not a wedge yet. His positioning doc listed 5 profiles plus a region. Pick the one with the most stated, paid signals.
- **The buyer comes from the product's own homepage words and from the people who pay.** Never from blog topics or supply-side data. He corrected this twice. Once a buyer was read off 13 of 152 blog posts ("it is an SEO agency, what is this pest owner"). Once a buyer's city was guessed from where the sellers were ("dont assume").
- **The pitch depends on attacking a supplier you rely on:** kill that framing. Name the access, not the gatekeeper. His wedge survived as "access", worded without the supplier's name.
- **Signals from a country or category you can't serve:** log them as demand, never as leads. His runs dropped posts from countries outside his payout list, physical goods, tips, and custom hourly work.
- **Examples must be problems the product solves.** In one run the most emotional quotes were dropped, such as a filmmaker who needed an official registration, because the product isn't one. Pick quotes inside the founder's own categories.
- **Competitor prices show shape, not level.** For a founder at $0 revenue, a funded rival's $99-$350 a month is not a target. Use the table to show a structure ("all of them meter; you sell unlimited").
- **A free asset is not demand.** A "yes, send it" is not a signal; a price question or a payment is. Free playbooks and audits get thanks, rarely a call.
- **A buyer at €0 revenue can't pay a percentage.** Score what they pay today, not what they need. Founders with no buyers often think a tool will fix that; it doesn't.
- **A technology ahead of its buyer is not a wedge.** Products built for a future market fail with "nobody needed it yet"; keep the tools, change the model.
- **Founder claims are not ledger facts.** Processing volume is not revenue. Use ledger numbers only.
- **The pain is a bug in someone else's product:** check the vendor's changelog and issue tracker before scoring. In the Oct 2026 live run, a wedge scored 8/10 on three fresh quotes (WooCommerce orders cancelled after a Stripe payment). The plugin had shipped the fix 5 days earlier, so the wedge died at positioning.
- **No wedge after 2-3 areas:** say so, with the searched table. Never pad with places ("try r/SaaS") in place of posts.

## Quality bar (every brief)
- [ ] `knowledge/founder-history.md` exists and the candidates cite it, or the brief says the founder has no history yet.
- [ ] 6-10 problems were listed before narrowing, and each has a gap verdict with the incumbents named, linked and priced.
- [ ] The idea critic ran at least two rounds; its kills are listed with the reason.
- [ ] The inclusion rule is written at the top, before the signals.
- [ ] The wedge is one line: one buyer, one job, one moment. No "and".
- [ ] 3-5 quotes, each checked word for word against its source, with link, date, age tag and grade. At least 3 are A or B, from different people.
- [ ] The searched table lists every channel and query with its outcome: signal, noise, zero, or blocked. A block is a tool gap, not a negative.
- [ ] If calls or forms exist: the stated / weak / inferred count, with pitched reasons left out.
- [ ] "Who pays today" names a real fix and a price read from a live page, dated, or says "not found".
- [ ] The first 20 people are real handles, threads or companies, or the brief says how many are missing.
- [ ] A first price, labelled a test, small enough to say to 10 people this week.
- [ ] Every kill rule has a written result, and this week's kill test has a number that means stop.
- [ ] Every figure names its source; projections are labelled.

## Never
- Invent, polish or merge quotes. A quote is the exact text at the link.
- Count a place as a signal. "r/SaaS" is not one; a thread in it, written by a person, is.
- Count a reason the founder (or you) raised on a call as the buyer's reason.
- Use LinkedIn content search or a general web search as proof of demand. In his runs, both returned only vendor posts and vendor blogs. A first-person post by a buyer, found that way and re-opened, is a signal; the search is not.
- Scrape in bulk, use bots, or get around a login wall, CAPTCHA, rate limit or browser block. Pace requests at human speed and say where you stopped.
- Post, comment, vote, join, follow or DM while researching. Research is read-only.
- Copy personal data beyond the public handle, post and link. Drop anyone who says they are under 18.
- Score by market-size (TAM) estimates, trend charts or search-volume guesses.
- Recommend a marketplace, a two-sided network, or anything that needs a licence before the first sale.

## Shared knowledge
**Read first:** `CLAUDE.md`, `knowledge/decisions.md` (killed ideas and why), `knowledge/customers.md` (people already talking to the founder are the warmest signals), `knowledge/rules.md` (queries that worked before). **Write after:** `knowledge/founder.md` and `knowledge/founder-history.md`; `knowledge/decisions.md` (the chosen wedge and the killed ones, one dated line each); `knowledge/customers.md` (the first 20, marked "idea-finder, not contacted"); `knowledge/ideas/<date>-<slug>.md` (the brief with the signal log); `knowledge/rules.md` (every query that found signal, and every one that was pure noise). If the founder has a sign-up or booking form, propose the "why us instead of ___?" field from `wedge.md`. Never passwords or card numbers. Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Ask `recipes` (area `distribution`, question: where do these buyers talk and complain?) before step 1 and `lessons` (theme `customers-and-sales`, then `truth-and-numbers`) at the decision rules. Ask `evidence` (topic: idea) for the author's measured numbers behind each rule. If it isn't connected, carry on with this method.
