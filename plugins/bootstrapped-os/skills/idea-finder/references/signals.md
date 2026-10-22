# Signals: what counts, how to grade it, and where the author found it

A **signal** is one linkable thing one person wrote, in their own words, showing they have the problem. A place ("this subreddit", "freelancer groups") is never a signal; a specific post or comment in it is.

His rule, after an assistant sent him lists of places: "not vague and high level like 'write and ask 10 people'; this is BS. We need something concrete: we've noticed this post on X or Reddit or LinkedIn or the web, or a person in my network." And: "a proper reddit comment or FB post or a post in my LinkedIn; a proper signal!"

## 1. Write the inclusion rule first
Write it before the first query, and put it at the top of the log. A rule written after the search bends to fit what you found.

| Part | His creator-proof run (one product) | His payments run (another) |
|---|---|---|
| Who | The poster made the work themselves | A seller with a product or a fixed-price service |
| Need | Asks how to protect, prove, timestamp or register it before sharing, or their work was taken and they must show it is theirs | Can't take card payments where they live, or was rejected by a payment provider |
| Window | 12 months for demand evidence; under 60 days for leads | 60 days for leads |
| Dedup | One entry per person, by handle, across all channels | Same |
| Out | Vendors and founders running "surveys"; self-identified minors; work not their own (fan edits, quoting a famous song); AI-accusation posts; contract disputes with a distributor | Countries outside the payout list; physical goods; tips and donations; custom hourly client work; marketplaces paying third parties; already-solved threads; country not stated |

The snippet must appear word for word in the source. In his runs a script checked every snippet against the archived or API text before it was recorded.

## 2. Grade (quality) and intent (what they want)
| Grade | What it is | Shape from his runs |
|---|---|---|
| **A** | Recent, linkable, own words, and money or a workaround already spent | Both seen in his files: a services seller whose US-dollar receipts "incur high fees of 8% to 9%"; a founder who opened a US company just to get a card processor |
| **B** | Recent, linkable, own words, clear pain, no spend yet | "I tried, it rejects me. It's a SaaS on a subscription model." / "What practical steps do you take to protect your unreleased music?" |
| **C** | Old, vague, second-hand, or a builder's wish | "Someone should build X"; a 9-month-old thread with no reply |
| **Out** | No link, invented, vendor marketing, a trend article, a minor | |

| Intent | Meaning | Use |
|---|---|---|
| **direct** | Asks for a way to do the job ("is there a place to timestamp my hypothesis?") | Highest. Outreach and quotes |
| **problem** | Hit the problem and is dealing with the fallout ("they keep asking me to prove the films are mine") | High. Buys after the fact, or for the next piece |

## 3. Age (signal decay)
| Tag | Age | Counts as |
|---|---|---|
| hot | 0-7 days | Lead. Reply this week |
| warm | 8-30 days | Lead |
| cooling | 31-60 days | Lead, lower odds |
| stale | over 60 days | Demand evidence only, never an outreach target |

A thread can be stale while its pattern is live. In April, about 10 people in one thread of a regional developer subreddit asked a stranger to DM them a guide to opening a US company so they could charge for software. Too old to answer, but the same question kept coming back, so the cluster counted.

## 4. Which channels gave signal and which gave noise (his runs, Oct 2026)
| Channel | Payments run (sellers who can't take cards) | Creator-proof run (people protecting their work) | Verdict |
|---|---|---|---|
| X, logged in, **Latest** tab, quoted phrases | 5 of the first 6 signals, including all 3 strong ones | 7 | Best live channel for first-person complaints |
| X, local-language queries | Noise: news and crypto promos | n/a | Don't bother; use local Reddit and forums instead |
| Reddit, national and regional subs, native-language terms | The warmest leads; one regional developer sub was "the best sub for this" | n/a | Best for a home-market wedge |
| Reddit, big English subs (r/SaaS, r/indiehackers) | r/SaaS "merchant of record": 25 entries, a few real; r/indiehackers: 3, all a year old | 48 from creator subs | Good if the buyer is a maker |
| Reddit, r/freelance, r/forhire | 0 results on 8 queries | n/a | Freelancers don't describe payment problems there |
| Reddit comments (archive) | Not run | Round 1 added 19 people | Always run; titles miss them |
| Bluesky public search | Not run | **177 of 396**, the biggest channel | Run it for creators and writers |
| GitHub issues and discussions | n/a | 16 | Developers asking how to protect code |
| Hacker News (Algolia) | 1 signal; the rest were launches and noise | 5 | Low yield for non-developer buyers |
| Stack Exchange (Academia, Law) | n/a | 6, plus the research cluster | Good for researchers |
| LinkedIn content search, by date | Vendor posts only, 0 signals | n/a | Not a demand channel. Use it for the founder's own network |
| General web search aimed at Reddit | Vendor blogs only | n/a | Not a demand channel |
| Facebook groups, Instagram | Login wall, not searched | 0 | Do them in the logged-in browser, read-only, or mark "not searched" |

## 5. Queries: what worked and what was noise
| Worked (first person, quoted, a failure verb) | Noise |
|---|---|
| `"not available in my country"` + the tool | `stripe alternative country` unquoted: 25 entries, all noise (music subs) |
| `<competitor> rejected` / `denied` / `suspended` / `frozen`, and `@<competitor's handle>` + the same verbs | `"eu vat" "digital products"`: guides and vendor posts |
| `"prove I made"`, `"someone stole my design"`, `"how do i protect my"`, `"poor man's copyright"` | Local-language payment words on X |
| The native words for "charge", "payment from abroad" and "freelancer" in the buyer's national subs | `"accept card payments"` in freelance subs: 0 |
| `"need a merchant of record"`, `"alternative to <competitor>"` | The product's own name: in one run every hit was the same word in another language |

Run each query on the Latest tab with a `since:` date. Then re-open every candidate on its own page before it goes in the log.

## 6. How much is enough
- **Loop until dry:** run rounds (comments, more communities, other channels, other languages, new phrase families) until a round adds fewer than 5 people. His creator run: 76 after the first pass, 396 after 15 rounds. The owner's rule: "a small count like 76 means coverage was too narrow, not that demand is small."
- **Short brief or teaser:** 2-3 strong signals, about 15 minutes per product, then stop.
- **Cluster:** 5+ A/B signals from different people. Count people, not upvotes.

## 7. The signal log (one row each)
| # | Link | Date | Age | Quote (exact) | Who (role) | Today's fix | Money? | Intent | Grade |
|---|---|---|---|---|---|---|---|---|---|

Below it, the **searched table**: channel, query or method, number of entries, outcome (signal / noise / 0 / blocked). Keep the log even for killed ideas.

## 8. Red flags
- All signals from one thread, one community or one person.
- The quote reads smoother than a person writes: re-open it and copy it again.
- Builders talking about builders' problems, or "would you use this?" surveys (vendors in disguise).
- The only pain is price ("X is too expensive"). That's a discount, not a gap.
- You picked the most emotional posts over the ones the product actually solves.
