# Due diligence: check them before you sign

Use this before you sign with a big client, a partner or reseller, a supplier, or a tool you'll give data to or depend on. One short memo, so the founder can say yes, yes with one condition, or no, with the evidence in front of them.

Most checks end in a yes. The aim is to find the one thing that would change the answer, not to pile up worries.

Templates: `due-diligence-templates.md` (checks by type, red flags, memo) · Gate: `due-diligence-gate.md` · Worked example: `due-diligence-example.md`

## Step by step
1. **Name the type:** tool or vendor, partner or reseller, supplier, or big client. Open the matching checks list in the templates.
2. **Look for an earlier check.** Past memos live in `knowledge/checks/`. A similar case decided before? Start from that.
3. **Read your own history with them first.** Your inbox, invoices and payment tool: past emails, payments, disputes. Search the inbox for anything they already sent.
4. **Walk their live website in a real browser.** Quote prices, claims and terms word for word, with the URL. If a page blocks automated fetching, open it in the browser before you call it missing.
5. **Check the company and the people:** the legal entity and country in a public company register, the founders and their public footprint.
6. **Look for independent reviews and complaints.** Not their own testimonials.
7. **Fill the gate** (`due-diligence-gate.md`): every row a link, or `not found (searched: <where>)`.
8. **Sort the red flags** with the red-flag list: stop, ask about it, or note only.
9. **Write the memo** from the template. The suggested decision first, then the evidence.
10. **Run the checker.** It must print PASS before the memo says FINAL.
11. **Save it** as `knowledge/checks/<date>-<name>.md`. Anything you caught late becomes a rule in `knowledge/rules.md`.

## Decision rules
- **Judge what they say and sell today.** A months-old blog post is history, not evidence.
- **Ask only what would change the decision.** One question is normal. A second only if it could turn yes into no.
- **Stop** (identity can't be confirmed, what they do is illegal, a lawsuit or regulator action about the same thing you'd do with them) -> suggest walking away. Keep the memo short and say which gate row fired.
- **Can't check it, but the stakes are low** -> go ahead with a limit (a smaller first order, a deposit, a short contract, payment upfront).
- **Normal business choices are not red flags:** working with other suppliers or your competitors, being new, selling services.
- **A flag means look, not reject.** Check each flag against a source before it counts.

## Quality bar
- [ ] One company or person per memo, named in the title.
- [ ] Every gate row: a link, or "not found (searched: ...)" with where you looked.
- [ ] Prices and claims quoted word for word, with URL and date.
- [ ] Your own history read from the inbox and payment tool, not from memory.
- [ ] The decision row has a decision word and "because".
- [ ] The checker printed PASS.

## Never
- Never decide on a feeling or on one review site.
- Never check two companies in one agent or one memo.
- Never say "doesn't exist" without checking the real thing (their site, the register).
- Never pad a section without evidence. Shorter, not vaguer.
- Never contact them, sign or pay. The memo is a suggestion for the founder.
- Never paste private personal data (home address, ID numbers) into the memo. Link to the source.

## Finish
Run `python3 "${CLAUDE_PLUGIN_ROOT}/skills/ops/scripts/check-memo.py" <memo.md>`. It must print PASS before the memo is marked FINAL.
