# Due diligence templates

The gate itself lives in `due-diligence-gate.md`. This file holds the checks per type, the red-flag list and the memo.

Note for the checker: in the memo, only the gate table may have rows numbered 1-7. Use bullets everywhere else, or the checker will read the wrong rows.

---

## 1. Checks list, by type

Do the **common checks** for everyone, then the checks for the type.

**Common (feeds gate rows 1-6)**
- Legal entity name, registration number and country, from a public company register.
- Website live today: what they sell, prices word for word, terms, privacy policy, contact details.
- Founders or owners: names, public profiles, how long they've done this.
- Independent reviews and complaints (review sites, forums, news). Not their own testimonials.
- Our own history with them: inbox search, past payments, disputes, support tickets.
- Domain age and whether the site, company name and email domain match.

**Tool or vendor (you'll give it data or depend on it)**
- Where data is stored, and who can see it. Is there a data-processing agreement?
- Can you export everything and leave? In what format?
- Price today, word for word. What happened to prices in the past (changelog, announcements)?
- Uptime or status page. Recent outages.
- Who owns it. Recently acquired? Still being updated?
- What breaks for your customers if this tool disappears tomorrow?

**Partner or reseller (they sell for you, or you for them)**
- What exactly do they get: discount, commission, exclusivity? Written down?
- Do they already sell to your kind of customer? Show one real example.
- How will they describe you? Ask for the page or the pitch.
- Who owns the customer relationship and support?
- How either side ends it.

**Supplier (you buy goods or work from them)**
- Sample or small first order before a big one.
- Lead times and what happens when they're late.
- Payment terms: deposit, balance, currency.
- Returns and defects: who pays.
- Any certifications they claim: check the issuer's own register.

**Big client (they'll owe you money or a lot of your time)**
- Are they who they say? Company register, website, the person's role.
- Can they pay? Payment terms they ask for vs what you offer. Deposit?
- How do they talk about past suppliers (reviews, public posts)?
- Scope written down with a fixed price or clear rate.
- What share of your revenue would they be? Over a third means a dependency.

---

## 2. Red flags

Sort each flag into one of three bins. A flag only counts once you've checked it against a source.

**Stop -> suggest walking away**
- Identity can't be confirmed: no company, no person, mismatched names everywhere.
- What they do is illegal where they or you operate, or banned by your payment provider.
- Public court or regulator action about the same activity you'd do with them.
- Asks for payment or bank-detail changes through an unusual channel.
- Copied or fake content: stolen photos, invented reviews, fake team pages.

**Ask about it -> one question, decision waits for the answer**
- Company registered very recently for a large deal.
- Prices or terms on the site contradict what they told you.
- A pattern of the same complaint in independent reviews (3 or more).
- Pressure to decide fast or skip your normal steps.
- Wants exclusivity or long lock-in before any results.

**Note only -> doesn't change the decision**
- New business with a small footprint.
- Also works with your competitors or other suppliers.
- One bad review among many good ones.
- Sells services as well as products.
- Old blog posts that no longer match today's site.

---

## 3. Memo template

Save as `knowledge/checks/YYYY-MM-DD-<name>.md`. A later re-check adds to the same file.

```markdown
# <Name> - due diligence (DRAFT)

**Type:** tool / partner / supplier / big client
**Asked by:** <founder>, <date> - <what we're deciding: "sign a 12-month reseller deal">
**Suggested decision:** go ahead / go ahead with a condition / ask for <one thing> / walk away - because <one line>

## Gate
| # | Check | Evidence (link) or "not found (searched: ...)" |
|---|---|---|
| 1 | Legal entity and country | |
| 2 | Website live, what they sell, prices (verbatim) | |
| 3 | Founder(s) and public footprint | |
| 4 | Reviews / complaints (independent sources) | |
| 5 | Our own history with them: emails, payments, disputes | |
| 6 | Red flags | |
| 7 | Decision proposed + why | |

## Type checks
- <check from the list>: <finding> (<link>)
- ...

## Red flags, sorted
- Stop: <none, or flag + link>
- Ask about it: <flag + link>
- Note only: <flag + link>

## Earlier checks
- <a similar memo in `knowledge/checks/` and what was decided, or "none">

## The one ask (if any)
<the exact question, one line, in plain words>

## Not checked
- <what you couldn't check and why>
```

Change `DRAFT` to `FINAL` only after the checker prints PASS and the founder has read it.

---

## 4. A lesson from a late catch

Add it to `knowledge/rules.md`:

```markdown
**Rule:** <what to check from now on>
**Why:** <date> - missed <what> in the check on <name>.
**How to apply:** <add it to the checks list for this type>.
```
