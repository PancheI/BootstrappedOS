# Verification: be ready, then draft the answers

The founder submits verification in the AgentaOS dashboard. A merchant of record sells your product in its own name, so before it does, it checks that the product is real, the prices are clear and a buyer gets something. This page is a checklist from the public AgentaOS docs and Terms, plus a draft the founder copies from. Policies move: read the live docs and Terms before relying on a line.

## Be ready before you submit

| The check | What "ready" looks like |
|---|---|
| A live product | The site is public, the buy button opens a working checkout, and the test checkout passed through to access (SKILL.md step 4) |
| What the buyer gets | Something the buyer has the minute the card succeeds: a login, a file, a course, a report. "We start work after a call" is not it |
| A way to see the paid part | A demo login, a 100% discount code, test mode or a recorded walkthrough, so the reviewer can see behind the paywall |
| Prices in public | The same prices and what's included, visible before checkout. Refund and cancel terms one click from the buy button |
| Terms and privacy | `/terms` and `/privacy` live, with the real seller's name and details |
| Who sells | The legal seller named where a buyer looks (footer or legal page) |
| Support that matches | One support email on the site, the same one in the dashboard, and someone reads it |
| Fixed prices | Packages with one price for every buyer. Quoted or "starting at" work is billed outside the checkout |
| A durable deliverable | Recordings, templates, software or a login. Time sold by the hour (mostly live calls) is not a product |
| Claims you can back | Every count, quote and testimonial true today, or removed |
| Money between your users | Say plainly whether your users pay each other through you. Bookkeeping (a "paid / not paid" field) is different from moving other people's money |
| You can be paid out | Your country and bank are on the supported list in the docs |

## The draft
Put it in `knowledge/drafts/agentaos-verification.md`, headed: **Draft. Check every line before you paste it. Nothing here was submitted.** Fill each line only from `knowledge/` or the live site, source beside it. Unknown: leave blank, "you fill this". Never guess a legal fact.

| Field in the dashboard | Draft | Source |
|---|---|---|
| Selling as | individual / business | `knowledge/decisions.md` |
| Legal name (company, or your full legal name) | | you fill this |
| Registration number (business only) | | you fill this |
| Tax country | | `product.json` -> `legal.country` |
| Address | | you fill this |
| Product URL | | the live site |
| Product description: what it does, who buys it, **what the buyer gets the minute they pay** | | `product.json` -> `promise`, `buyer` |
| Name on the buyer's statement | | `product.json` -> `name` |
| Category and delivery | e.g. SaaS, subscription access by login | the product |

## The checklist questions
Answer each from what is true on the live site today:
- Privacy and terms live, with the real company details?
- Prices and what's included clear before checkout? Refund and cancel terms one click from the buy button?
- Any usage or result claims? Each one backed by something real, or removed.
- Any customers yet? The true number; zero is fine. Your own test purchase is not one.
- A way for the reviewer to see the paid product?
- The name or logo is yours to use?

## Open questions
`npm run golive` lists them. For each: a short, true reply, plus what changed on the site if a change was asked. The founder posts it in the dashboard, not by email. After approval, take the first test payment and the first real one soon.
