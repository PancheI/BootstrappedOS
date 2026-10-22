---
name: brand-brief
description: Brand brief - turn the idea-finder's top wedges into one chosen wedge and a one-page brand brief (name with domain check, one-line outcome, voice, palette with contrast, two fonts, a text wordmark, the real buyer quotes), then fill the launch starter's product.json. The brand stage of /start-from-zero. Use for "name my startup", "pick between my ideas", "brand brief", "what should it be called", "colours and fonts", "tagline", "one-liner", "which wedge".
---

# Brand brief

You turn a researched wedge into something a buyer recognises in 3 seconds: one wedge, a promise line in the buyer's words, a name the founder can own, the words to use and ban, and a look the landing page can use tomorrow. One page. No logo, no mood boards.

The founder makes two calls: **which wedge** and **which name**. You decide everything visual and show one finished choice with a one-line reason. His words when shown four options: "why on me I'm not design expert."

**No linked quotes = no brief.** If the idea brief has fewer than 3 linked quotes, stop and send the founder back to `idea-finder`. **Needs the positioning card** (`knowledge/positioning.md`) first: the promise line comes from it.

**References:** `references/lines-and-names.md` (the author's line, name and word rounds with his verdicts, the messaging layers, the 7 line tests, and the story behind each step below) · `references/brief-template.md` (the page to fill, the domain and contrast checks, the product.json mapping).

## The process
1. **Read what exists:** the latest idea brief (quotes, stated reasons, who paid), the positioning card, decisions, customers, and the brand brief if there is one. A live brand's palette and fonts are never reopened.
2. **Show the top 3 wedges side by side** (`brief-template.md` part 1) and recommend one in a sentence.
3. **One moment.** Allow a mix of wedges only if it still has one moment. On a first product, pick one (`lines-and-names.md` §7).
4. **Write the promise line first:** 10 words or fewer, from the strongest stated reason and the buyers' own phrase. Run the 7 tests (`lines-and-names.md` §6) and write each result down.
5. **A playful line gets a plain sentence directly under it.**
6. **Fill the five layers** (`lines-and-names.md` §5). Never let a hook become a product name.
7. **Name: 5 options from 5 angles** (the outcome, the moment, a word from a quote, a plain compound, a short coined word). Apply the naming rules in `lines-and-names.md` §3 and §7. Run the domain check on `.com`, `.co` and `.app`. **Never buy, reserve or add to a cart.**
8. **Words to use and ban:** start from `lines-and-names.md` §4 and add the founder's own.
9. **Voice:** 3 words plus 2 example lines built from the buyers' quotes. No em dashes, no tagline tails.
10. **Palette:** ink, paper and **one** accent, with hex. A colour that fails contrast as text is a fill only. No glow or gradient wash on white. Run the contrast check and write the ratios down.
11. **Fonts:** two Google Fonts, display and body, each with a reason. The display font is never a default (Inter, Roboto, Arial, system) and goes on H1/H2 only. Both fonts cover the founder's languages.
12. **Wordmark:** the name in the display font, one weight, one colour. Text only.
13. **Second language, if any:** the native word, not a transliteration, checked against official terms.
14. **Quotes:** copy 3 linked quotes exactly from the idea brief. Re-open each link today; drop dead ones.
15. **Show the whole brief once.** **Gate:** wait for the founder's OK. Change only what they name; never re-touch an approved line later.
16. **After approval, save** the brief and fill the launch starter's `src/config/product.json`. Then ask: "go to the landing page?"

### Filling product.json
Read the file's current shape first and keep its keys. Never add new ones: palette and fonts go into `globals.css` and `layout.tsx` at the landing-page stage. The field-by-field mapping is in `brief-template.md`. `legal` is always asked, never guessed. Delete `_note` only once every field is real.

## Decision rules (each from a real run)
- **The founder wants a name before a wedge:** do the wedge first. A name for no one is a guess with a domain.
- **The line names the founder's feature, not the buyer's outcome:** rewrite it. "Our pricing agent builds..." was rejected as feature-speak; the hero names the pain, then removes it in words a cold reader knows.
- **The line attacks a gatekeeper or supplier:** drop the name, keep the access. A line aimed at a supplier you depend on is a risk.
- **Two products, one founder:** one sentence joins them ("I help founders get their first paying customer. One is how you find them, the other is how you take the money"), and each post or page carries one ask, never two.
- **The founder loves a taken name:** say so. Use a prefix (get-, try-) only if it still reads naturally. Prefer a plain word on `.co` or `.app` over a misspelled `.com`.
- **The founder has an existing brand:** keep the palette and fonts. When a designer pass replaced his community's look with a dark palette, gold leaf and three new fonts, his answer was "I liked the story but not the style... the colors not good".
- **The founder can't judge a line on paper:** show it on the built hero. He reacts to the built thing, not to sketches.
- **No "why now":** write "none found" and lower the recommendation. Never invent urgency.

## Quality bar (every brief)
- [ ] One wedge line: one buyer, one job, one moment.
- [ ] A promise line of 10 words or fewer, with all 7 tests written down, including at least one phrase from a linked quote.
- [ ] A playful line has a plain sentence directly under it.
- [ ] The five layers filled; the category never used as a hook; one launch hook, marked disposable.
- [ ] 5 names with `.com` / `.co` / `.app` status and the date checked; every analogy is one the founder recognises.
- [ ] A use / ban word list of at least 5 rows, including the founder's own.
- [ ] Voice: 3 words plus 2 lines that sound like the buyers' quotes.
- [ ] Ink, paper and one accent with hex and contrast ratios written down; any failing colour marked "fill only".
- [ ] Two Google Fonts, the display one not a default, each with a reason.
- [ ] A text wordmark; 3 exact quotes, each link re-opened today.
- [ ] Fits on one screen. The founder said OK before anything was saved.

## Never
- Buy, reserve or hold a domain, or create registrar or social accounts.
- Invent, polish or merge quotes.
- Generate or draw a logo, icon or mascot.
- Use "free money", "revolutionary", "all-in-one", "AI-powered", "cheapest" as your own claim, or a supplier's or rival's name in the promise, voice lines or hero.
- Name a free tool with an invented term, or turn a hook into a product name.
- Use an em dash in any line.
- Ask the founder to choose between palettes, font pairs or layouts.
- Save to `decisions.md` or `product.json` before the founder approves, or rewrite an approved line without being asked.
- Assume a country, currency or legal entity. Ask.

## Shared knowledge
**Read first:** `CLAUDE.md`, `knowledge/decisions.md`, the latest `knowledge/ideas/<date>-<slug>.md`, `knowledge/positioning.md`, `knowledge/customers.md`, `knowledge/rules.md`, and `knowledge/brand/brief.md` if it exists. **Write after (only once approved):** `knowledge/brand/brief.md` (the brief, with the promise line marked **locked**); `knowledge/decisions.md` (dated lines for the wedge and the two not chosen, the name and its domain status, the palette, the fonts; a liked but unavailable name marked "parked"); the use / ban word list in `knowledge/rules.md`; `product.json` filled. Never passwords or card numbers. Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Ask `recipes` (area `seo`) before step 1 and `lessons` (theme `writing-and-copy`, then `design-and-pages`) at the decision rules. If it isn't connected, carry on with this method.
