# The brand brief (one page)

Two parts: the choice screen (before the founder picks), then the brief (after). Fill every line. If something has no evidence, write "not found". Save the approved brief as `knowledge/brand/brief.md`.

---

## Part 1: the choice screen

| | Option A | Option B | Option C |
|---|---|---|---|
| **Wedge** (one line) | [who] who [job], at [moment], when [what goes wrong] | | |
| **Buyer** | | | |
| **First price to test** | $__ per __ (test, from the idea brief) | | |
| **Why now** | dated, linked reason, or "none found" | | |
| **Kill risk** | the one thing that ends it | | |
| Score (idea-finder) | __/18 | | |

**My pick:** <A/B/C or a mix>, because <one sentence>. You can take one as it is, or mix (for example A's buyer with C's moment). Which one?

---

## Part 2: the brief

# Brand brief: <name>
**Date:** YYYY-MM-DD · **Status:** draft / approved by <founder> on <date>

## The wedge
<One line. One buyer, one job, one moment.> Chosen over: <B> (<why not>), <C> (<why not>).

## Promise line (10 words or fewer)
**<What the buyer gets.>**
<If playful: the plain sentence that sits directly under it.>

| Test (`lines-and-names.md` §6) | Result |
|---|---|
| 1. 3 seconds: a stranger says what, for whom, what they get | "<what a cold reader said>" |
| 2. Could it sit unchanged on a rival's page? | no / yes (rewrite) |
| 3. Category in the first words, or right under it | |
| 4. A phrase from a linked quote | "<phrase>" (quote #_) |
| 5. X to Y, or a verified digit | |
| 6. Can you picture who does what? | |
| 7. True today, every number sourced | |

## The layers
| Layer | Ours | Where it goes |
|---|---|---|
| 1 Brand | <name> | everywhere |
| 2 Promise | <the line above> | H1, link preview, bios |
| 3 Category | <search words> | titles, meta, comparison pages; never a hook |
| 4 Products | <plain names: "[what] + noun"> | nav, features, pricing |
| 5 Launch hook | <"X for Y", disposable> | one post or video only |

## Words: use / ban
| Don't write | Write | Why |
|---|---|---|
| free (paid brand) | $0 / "for an email" | cheapens it |
| free money | grants and AI credits, no equity | "looks scammy" |
| <jargon from the category> | <the plain word a cold reader knows> | |
| <a word that cheapens the product> | <the exact word> | |
| <the founder's own> | | |

## Name
| # | Name | Angle | .com | .co | .app | Note |
|---|---|---|---|---|---|---|
| 1 | | outcome | looks free / taken / unclear | | | |
| 2 | | moment | | | | |
| 3 | | buyer's own word (quote #_) | | | | |
| 4 | | plain compound | | | | |
| 5 | | short coined word | | | | |

Checked on YYYY-MM-DD with RDAP, DNS and whois. "Looks free" means no record found today; it is not a reservation. **Pick:** #_ on <ending>, because <one line>. Nothing was bought or held.

## Voice
**<word>, <word>, <word>.**
- Hero line: "<...>"
- Button or email line: "<...>"
Never sounds like: <one line, e.g. a bank, a hype thread>.

## Palette
| Role | Hex | Use |
|---|---|---|
| Ink | #______ | text, borders |
| Paper | #______ | ground |
| Accent | #______ | the one button, links, one highlighted word |
| Highlight (optional) | #______ | one named job only (a marker, a live dot); "fill only" if it fails as text |

Contrast: ink on paper __:1 (need 7) · accent with its label __:1 (need 4.5) · accent as large text on paper __:1 (need 3). <If the accent fails as text: "fill only, ink text on it".>

## Fonts (Google Fonts)
- Display: **<font>**, weight __, on H1/H2 only. Why: <tied to the buyer>.
- Body: **<font>**, weights __/__. Why: <reading context>.
Languages covered: <list>.

## Wordmark
<The name, as text, in the display font: weight, case, colour, the one accented character if any.> No drawn mark.

## What buyers say (exact, linked, re-opened today)
1. "<text>", <source>, <url>
2. "<text>", <source>, <url>
3. "<text>", <source>, <url>

## Goes into product.json (after approval)
| Field | From |
|---|---|
| `name` | the chosen name |
| `domain` | the chosen domain; keep the `.example` placeholder with a note if none is free yet |
| `tagline` | the one-liner |
| `promise` | one or two plain sentences: what the buyer does, what they get back |
| `buyer` | the wedge's buyer, in their words |
| `cta` | a verb plus what they get ("Check my price"); never "Get started" or "Learn more" |
| `problem.title` | the moment, in the buyer's terms |
| `problem.quotes` | the 3 quotes above as `{text, source, url}`, exact |
| `steps` | 3 steps of what the buyer does, a few words each |
| `faq` | the 2-4 doubts the quotes raise, short answers |
| `founder` | name and one true line |
| `legal` | asked from the founder: company or name, email, country. Never guessed |

---

## The domain check (read-only, never a registrar search box)

Registrar search boxes can log what you look up. Use public lookups, and treat a "free" result as a hint until the founder checks at their registrar.

```bash
for d in NAME.com NAME.co NAME.app; do
  code=$(curl -sL -m 15 -o /dev/null -w "%{http_code}" "https://rdap.org/domain/$d")
  ns=$(dig +short NS "$d" | head -1)
  who=$(whois "$d" 2>/dev/null | grep -i -m1 -E "no match|not found|does not exist|domain name:")
  echo "$d rdap=$code ns=${ns:-none} whois=${who:-none}"
done
```

Read it like this:
- **Taken:** RDAP 200, or any NS record, or whois shows a "Domain Name:" line. Any one is enough.
- **Looks free:** RDAP 404, no NS, and whois says "not found" / "no match" / "does not exist". All three.
- **Unclear:** anything else (timeouts, rate limits, mixed answers). Say "unclear", don't guess.
- RDAP alone is not enough for `.co` (it can answer 404 for registered names); whois decides there.
- A taken domain with no site may be for sale. Note it; never contact the owner or make an offer.

## The contrast check

```bash
node -e 'const L=h=>{const c=[1,3,5].map(i=>parseInt(h.slice(i,i+2),16)/255).map(v=>v<=.03928?v/12.92:((v+.055)/1.055)**2.4);return .2126*c[0]+.7152*c[1]+.0722*c[2]};const r=(a,b)=>{const x=L(a),y=L(b);return((Math.max(x,y)+.05)/(Math.min(x,y)+.05)).toFixed(1)};const p=process.argv.slice(1);for(let i=0;i<p.length;i+=2)console.log(p[i],"on",p[i+1],r(p[i],p[i+1])+":1")' '#INK' '#PAPER' '#ACCENT' '#PAPER' '#LABEL' '#ACCENT'
```

Replace INK, PAPER, ACCENT and LABEL with hex values and **keep the quotes**: an unquoted `#0B1533` starts a shell comment. With `node -e`, the arguments start at `process.argv[1]`. Checked on his community palette: `'#0B1533' '#FFFFFF'` gives 18.0:1, `'#FFFFFF' '#4F46E5'` 6.3:1, `'#E4FF3C' '#FFFFFF'` 1.1:1. Pass marks (WCAG AA/AAA): body text 4.5:1, large text (24px+, or 19px bold) 3:1; aim for 7:1 ink on paper.

## Fonts: quick guide
- Pick from Google Fonts so the launch starter loads them with `next/font/google`, no files to host.
- Display: something with a point of view that fits the buyer (a sturdy grotesk for trades, a softer humanist for care work, a sharp serif for money and law). Body: a calm, readable sans or serif with real italics and tabular figures if prices show.
- Not the display choice: Inter, Roboto, Arial, Helvetica, system-ui, Open Sans. Inter is fine as the body when the display font carries the brand (his payments site: Bricolage Grotesque 500 for headings, Inter for body, Space Grotesk for figures).
- His two real pairs: Unbounded 700/900 + Onest 400-700 (community: loud, reads on a phone); Bricolage Grotesque 500 + Inter (payments: editorial, calm).
- Two families, at most three weights in total on the page. A third family only for figures.
- On a live brand, never swap the heading font in one place; he flagged a one-page swap as "inconsistency" with the live site.
