# Knowledge templates

Copy, fill, adapt.

---

## 1. Decision log entry

One file (`decisions.md`) or one Notion database. Newest at the top.

```markdown
## <YYYY-MM-DD> - <decision in under 10 words>
**Decided:** <what, in one or two lines>
**Why:** <the reason, ideally a real number or a customer's words>
**What would change it:** <a specific signal: "if 3+ customers ask for X", "if refunds go over 5 a month">
**Replaces:** <date + title of the older decision, or "nothing">
**Files updated:** <CLAUDE.md line / skill / `knowledge/rules.md`, or "none">
```

When a later decision replaces it, add one line under the old entry:
`**Replaced by:** <date> - <title>`

---

## 2. Rule-writing pattern (CLAUDE.md or `knowledge/rules.md`)

Every rule has three parts. The "why" lets Claude judge edge cases instead of following blindly.

```markdown
**Rule:** <one line, an instruction: "Never ...", "Always ...", "Before X, do Y">
**Why:** <what went wrong, or what the founder said, with the date>
**How to apply:** <when it applies, the exact steps, the edge cases>
```

Example:

```markdown
**Rule:** Before any reminder email, check the inbox and the payment tool for that customer.
**Why:** 3 Oct - a customer who had already replied by email got a "we're still waiting" reminder.
**How to apply:** for every failed-payment or unpaid-invoice reminder, search the inbox for the customer's address and check the payment status first. Replied or paid -> no reminder; tell the founder instead.
```

In CLAUDE.md, keep only the **Rule** line (one screen total). Put the why and how in `knowledge/rules.md` and link it.

---

## 3. The shared knowledge base (one per business)

Every role reads and writes the same folder in your project. `/day0` creates it. The tree, and the only paths any role uses, are in [`shared/knowledge-tree.md`](../../../shared/knowledge-tree.md).

Index line format (`knowledge/INDEX.md`):

```markdown
- [Pricing rules](rules.md#pricing) - one main offer, yearly = 10x monthly, existing customers keep their price (updated 12 Oct)
```

Using Notion or Google Docs instead? Same shape: one page per file in the tree, one index page.

---

## 4. Customer / lead note

```markdown
# <Name> - <company or what they do>

| Date | What they said (their words) | Next step | Owner |
|---|---|---|---|
| | | | |

**What they bought / are considering:** <plan, package, product>
**Watch for:** <e.g. "asked about refunds twice">
```

---

## 5. "How we do things" page

```markdown
# How we <do the task>

**When:** <trigger: "every Monday", "when a refund request arrives">
**Done means:** <the result someone can check>
**Steps:**
1. <verb + object>
2. ...
**Never:** <the one or two mistakes that happened before>
**Owner:** <founder / which AI role>
```

---

## 6. Weekly cleanup routine (Friday, 10 minutes)

- [ ] **New corrections this week** -> each written as rule + why + how, in the right file.
- [ ] **Duplicates:** two files on one topic -> merge into one, update the index.
- [ ] **Clashes:** two rules that disagree -> the newer wins; mark the older "Replaced by <date>".
- [ ] **Dead rules:** about a tool, offer or process you no longer use -> delete or mark replaced.
- [ ] **CLAUDE.md length:** over one screen -> move topic rules to `knowledge/rules.md`, leave a pointer.
- [ ] **Index check:** every line in `knowledge/INDEX.md` points at a real file; every file has a line.
- [ ] **Decisions:** this week's decisions logged, with why and what would change it.
- [ ] **Scratch check:** anything worth keeping in a temp or scratch folder -> move it into the project.
- [ ] **Backup:** commit to the private repo (or export the notes tool).
