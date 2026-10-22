# Outcome copy, line by line

Every word on the page lives in `src/config/product.json` (and prices in `pricing.json`). Write there, not in `page.tsx`, so the page, the meta tags and the social image all say the same thing.

Soft budget: roughly 250-350 visible words for the whole page. It is advice, not a law: a counter that makes the page cryptic is worse than 50 extra words. Clarity leads.

## The first screen (the 3-second test)

| Slot | Field | Rule | Weak | Strong |
|---|---|---|---|---|
| Who-for label | `buyer` | The buyer in their own words. Only if it adds what the headline doesn't. | "For everyone" | "For solo founders with no paying customers yet" |
| Headline | `tagline` | The buyer's result. 2 lines max at 1440 and 390 (about 30-45 characters). | "The pricing platform for modern teams" | "Know what to charge before anyone has paid." |
| Sub-line | `promise` | Who does what, and what they get back. Plain verbs, one or two sentences. | "AI-powered insights to optimise revenue" | "Paste your pricing page. Get two pricing models, what each earns, and how many buyers you need to break even." |
| Button | `cta` | A verb plus the thing they get. | "Get started" / "Learn more" | "Check my price" |
| Price | `pricing.json` | Under or beside the button, in one line. | (hidden behind "See pricing") | "$9/mo · cancel any time" |

The test: show only these lines to someone (or a fresh agent) with no context. They answer five questions: what is it, who is it for, what do I get, what does it cost, what do I click. Write down their answers in `knowledge/pages/home.md`. If one is wrong, fix that line first.

## Below the fold: one level deeper per section

1. **The problem, in their words** (`problem.title`, `problem.quotes`). The title names the moment ("Pricing is a guess until it isn't"). Then the 3 linked quotes, exact, each with its source. No quote without a link.
2. **How it works** (`steps`). 3 steps of what the *buyer* does, a few words each. Not how the product works inside.
3. **Proof** (only if real). The founder's own numbers, a real result, a link to where it's written up. Rounded down, sourced, true today.
4. **Pricing** (`pricing.json`). Every plan, every price, what's included, how to cancel. Visible, not behind a click.
5. **Questions** (`faq`). The 2-4 doubts the quotes raise ("Do you store my data?", "Is this a course?"). Short answers. Kept in the page HTML, so search engines and AI summaries can read them.
6. **The founder** (`founder.line`). One true line about why they built it. A real name and, if they agree, a real photo.
7. **The close.** The same button, same words. Or the waitlist for people not ready yet.

## Rules for every line
- Outcome before mechanism. "Know what to charge", not "pricing analysis engine".
- Name the category plainly ("a payment page", "a checklist"), not the technology.
- One fact once per screen. If a line explains the line above it, cut one.
- Real numbers with a source; round down, never up to a number not reached.
- Write from what the buyer sees on that screen. No internal names, field names or codenames.
- No AI tells: no "X, but Y" contrasts, no "here's the thing", no buzzwords, no em dashes, no tidy three-part slogans.
- No rhetorical questions in the hero. A question works only if it's the buyer's own ("Why isn't anyone paying?") and the page answers it right under.
- Labels above headlines only if they add new information. "How it works" above a section called "How it works" goes.
- No visible SEO subtitles. Use semantic headings, alt text and the FAQ for search and AI readers.

## Proof: what counts

| Counts | Doesn't count |
|---|---|
| A buyer quote, exact, linked to the public post | "What our users say" with first names and no links |
| The founder's real revenue, users or time, with where it's shown | "Join 1,000+ founders" before there are 1,000 |
| A real screenshot of the product | A drawn dashboard with made-up figures |
| A press or community write-up, linked | Logos of companies that never used it |
| A private message, shown only with the person's written OK | A private message, pasted without asking |

## Before showing
Read the whole page as text from top to bottom. Count how many lines a skimmer must read to get the point (aim for 5 or fewer on the first screen). Cut duplicates. Then fact-check every number against its source.
