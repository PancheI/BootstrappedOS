# Weekly numbers templates

Copy, fill, adapt. Every query below is a starting point: event names and column names differ per business, so check yours first.

---

## 1. The Monday note

Add it at the top of `knowledge/numbers.md`, above last week's.

```markdown
# Week <nn> (<Mon date> - <Sun date>)

Excluded: <my IP / my country / @mydomain emails / test orders / test-mode payments>

| # | Number | This week | Last week | Source | Tag |
|---|---|---|---|---|---|
| 1 | Visitors (top 3 sources) | | | | verified |
| 2 | Leads (sign-ups / trials / bookings) | | | | verified |
| 3 | Buyers / revenue | | | | verified |
| 4 | Why they didn't buy | <n answers> | <n answers> | | quotes below |
| 5 | What broke (errors / complaints / refunds / failed payments) | | | | verified |

**Funnel:** see table below. Biggest drop: <step> -> <step>.

**Why they didn't buy (their words):**
- "<quote>" - <where: checkout question / email / cancel reason>
- "<quote>"

**Last week's change:** <what> -> <worked / didn't / too early> because <number>.

**ONE change this week:** <what> at the <step> step.
**Expect:** <which number moves, which way>.
**Check next Monday:** <the exact query or page to look at>.

**Not tracked / not checked:** <list, or "nothing">
```

Tags: **verified** = from a query you ran today. **arithmetic** = worked out from verified numbers. **projection** = a guess about the future. Never lead with a projection.

---

## 2. Funnel table

```markdown
| Step | This week | Last week | % of previous step |
|---|---|---|---|
| Visitors | | | - |
| Lead (sign-up / booking / add-to-cart) | | | |
| Started checkout / call booked | | | |
| Bought / signed | | | |
```

Fewer than 10 people at a step? Leave the % empty and write the counts only. Comparing two weeks or two versions needs 5+ people on each side and 3+ events.

Pick your steps by business:
- **SaaS:** visit -> sign-up -> first key action -> started checkout -> paid
- **Shop:** visit -> product view -> add to cart -> checkout started -> order
- **Coach / service:** visit -> enquiry or booking -> call held -> proposal sent -> signed
- **Creator:** visit -> email sign-up -> opened 2+ emails -> bought

---

## 3. "Why didn't they buy?" question bank

Ask ONE question, in ONE place. Short answer box. Optional.

**At checkout exit or cancel screen:**
- "What stopped you today?"
- "What almost stopped you from buying?" (ask buyers, on the thank-you page)
- "What would you use instead?"

**In a follow-up email (to someone who started but didn't finish):**
- "Quick one: what made you stop at checkout? One line is plenty."
- "Was it the price, the timing, or something missing?"

**On a cancel screen:**
- "What's the main reason you're leaving?" (choices: too expensive / didn't use it / missing a feature / switched to another tool / other + text box)

**On a sales call that didn't close:**
- "What would have to be true for this to be a yes?"

Sort answers into: price, trust, missing feature, timing, confusion, other. Count each. Quote the clearest one.

---

## 4. PostHog (HogQL) - five numbers and step counts, this week vs last

Run in PostHog -> SQL. Change the event names and the domain to yours.

```sql
-- Step counts per week (people, not a strict ordered funnel)
SELECT
  if(timestamp >= now() - INTERVAL 7 DAY, 'this_week', 'last_week') AS week,
  count(DISTINCT if(event = '$pageview', person_id, NULL))            AS visitors,
  count(DISTINCT if(event = 'signed_up', person_id, NULL))           AS leads,
  count(DISTINCT if(event = 'checkout_started', person_id, NULL))    AS started_checkout,
  count(DISTINCT if(event = 'purchase_completed', person_id, NULL))  AS buyers
FROM events
WHERE timestamp >= now() - INTERVAL 14 DAY
  AND properties.$host = 'www.yourdomain.com'
  AND NOT (coalesce(person.properties.email, '') ILIKE '%@yourdomain.com')
  -- AND properties.$ip != '<your IP>'
GROUP BY week
ORDER BY week DESC
```

```sql
-- Top 3 sources this week
SELECT coalesce(properties.$referring_domain, '$direct') AS source,
       count(DISTINCT person_id) AS visitors
FROM events
WHERE event = '$pageview'
  AND timestamp >= now() - INTERVAL 7 DAY
  AND properties.$host = 'www.yourdomain.com'
GROUP BY source
ORDER BY visitors DESC
LIMIT 3
```

For a strict ordered funnel (step 2 only counts people who did step 1 first), use PostHog's Funnel insight with the same events and filters.

---

**Google Analytics 4 instead:** Explore -> Funnel exploration, `page_view` -> `sign_up` -> `begin_checkout` -> `purchase`, last 7 days vs the previous 7, with Admin -> Data filters -> Internal traffic set first.

---

## 5. Closed checkouts: the author's replay review

The leak he found most often sat between "opened the checkout" and "paid", and it was the words around the price, not the price.

1. **Track the close.** Fire `checkout_closed` when someone closes the checkout without paying, with the seconds it was open and the plan shown.
2. **Ask once.** On close, one optional box: "What stopped you?" Save the answer on your own server with the plan and the price line they saw (an analytics property gets lost).
3. **Watch the fast ones first.** Filter recordings to `checkout_closed` with under ~5 seconds open. A close that fast means they read something and left; read what was on screen.
4. **Write one line per recording:** the price line visible, the amount the checkout showed, the seconds open.

What his replays showed, and what he changed:

| What visitors did | What was on screen | The change |
|---|---|---|
| Closed a yearly checkout they didn't expect | The price framed as a monthly figure "billed annually", opening a yearly charge | The exact amount sits next to every Join button; a closed checkout asks "What stopped you?" |
| Closed the checkout in about 3 seconds | A line that read as both "pay today for the year" and "first month free" | One price line everywhere, monthly and yearly with the real amounts, nothing that reads as "free" |

Two of five recordings doing the same thing is a pattern worth a change; one is a story.

---

## 6. Stripe or Shopify CSV export

Export the last 14 days of payments (Stripe: Payments -> Export) or orders (Shopify: Orders -> Export). Then ask Claude to run this, or run it yourself. Change the four column names to match your file's header row.

```python
# weekly_from_csv.py  -  usage: python3 weekly_from_csv.py export.csv
import csv, sys
from datetime import date, timedelta

# Stripe payments export (check your header row):
DATE_COL, AMOUNT_COL, STATUS_COL, EMAIL_COL = "Created date (UTC)", "Amount", "Status", "Customer Email"
PAID = {"paid", "succeeded"}
# Shopify orders export instead:
# DATE_COL, AMOUNT_COL, STATUS_COL, EMAIL_COL = "Created at", "Total", "Financial Status", "Email"
# PAID = {"paid"}

EXCLUDE = ("@yourdomain.com", "test")          # your own and test orders
today = date.today()
weeks = {"this_week": [today - timedelta(7), today - timedelta(1)],
         "last_week": [today - timedelta(14), today - timedelta(8)]}
out = {w: {"buyers": set(), "revenue": 0.0, "failed": 0} for w in weeks}

for row in csv.DictReader(open(sys.argv[1], newline="", encoding="utf-8-sig")):
    if not row.get(DATE_COL):
        continue                                       # Shopify repeats rows per line item
    email = (row.get(EMAIL_COL) or "").lower()
    if any(x in email for x in EXCLUDE):
        continue
    day = date.fromisoformat(row[DATE_COL][:10])
    for w, (start, end) in weeks.items():
        if start <= day <= end:
            if (row.get(STATUS_COL) or "").lower() in PAID:
                out[w]["buyers"].add(email)
                out[w]["revenue"] += float(row[AMOUNT_COL].replace(",", ""))  # "1,234.56" format; for "1.234,56" swap the separators first
            else:
                out[w]["failed"] += 1

for w, v in out.items():
    print(f"{w}: buyers={len(v['buyers'])} revenue={v['revenue']:.2f} not_paid={v['failed']}")
```

Revenue here is gross (before fees and refunds). Say so in the note. Payment tools win over analytics for money numbers.

---

## 7. Recordings at any other leaking step

5 recordings: the 3 most engaged and the 2 fastest-leaving, never random. One line each: what was on screen when they stopped, any click on something that isn't a link, any error, and any surprise (a cost, a step, a field, tax added at checkout). Then: **the pattern across 5:** what at least 2 did.
