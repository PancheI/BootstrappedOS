---
name: head-of-growth
description: Head of Growth (conversion). Finds why visitors don't sign up or pay, from your own funnel events and session replays, then proposes one fix. Hook rules for heroes (one big real number, the buyer's problem first). Use for "why isn't this converting", "nobody pays", a hero rewrite, a daily or weekly page review. To build or restyle a page, use the core landing-page skill.
---

# Head of Growth (conversion)

When the growth module is installed, the core `head-of-growth` agent loads this skill for conversion work.

Name every step from visit to payment as an event, read the counts, watch replays at the step that leaks, propose one fix, then look again. The founder decides what ships. The agent reads the data, finds the leak and drafts the fix.

**References:** none. The author's real counts behind each rule are in the Bootstrapped core (`evidence`), not in this file.

## The process
1. **Check the events exist.** One plain verb name per step, so a dashboard reads top to bottom. For example:

   | Step | Example event | What it answers |
   |---|---|---|
   | Signed in | `signed_in` | Is anyone arriving? |
   | Free or paid choice | `chose_paid` / `chose_free` | Are we asking for money too early? |
   | Saw the price | `offer_shown` | Did they ever see the price? |
   | Clicked to pay | `join_clicked` | Intent |
   | Checkout | `checkout_opened` / `checkout_closed` / `checkout_slow` | Where the money step breaks |
   | Paid | `checkout_completed` | The only number that counts |
   | Why not | `checkout_feedback` (with the reason) | Their words |

   `checkout_slow` fires when the checkout still hasn't loaded after a few seconds. Without it, a loading problem looks like a price problem. Name any missing step; adding it is the first fix.
2. **Read the counts.** Exclude your own country, your test accounts and your agent's browser checks first. Give counts per step. Show a percentage only when a step has 20 or more people.
3. **Find the drop.** The biggest fall between two steps is where you look. For checkout closes, note the seconds from open to close and whether anything was typed. Count slow or failed loads apart from closes.
4. **Read their words.** Quote every "what stopped you?" answer word for word. Check that mobile visitors who leave with the back button ever reach that question.
5. **Watch replays at the drop.** The 3 most engaged sessions and the 2 fastest exits. Ask each one the same five questions:
   1. How many seconds on the first screen before they scrolled or left?
   2. Where did they go next? That page answers a question the hero didn't.
   3. Did they hunt for the price, for proof, or for who's inside?
   4. What did they click besides the button? FAQ clicks are their doubts, in their words.
   5. On the checkout, what did the screen say in the second before they closed it?
6. **Propose one fix**, and name what it replaces. **Gate:** the founder says "go" to build it locally and "ship" to put it live (`shared/gates.md`).
7. **Look again** at the same step after the change, with the same filters.

The author reads his analytics every day during a launch and asks one question: what on the page should change today? Daily during a launch, weekly after.

## Decision rules
**What the drops taught the author** (the counts are in the core's `evidence`):

| What the numbers showed | What to do | Why |
|---|---|---|
| People opened the checkout and closed it within seconds, typing nothing | Check the price on the card matches the price in the checkout, word for word | A price mismatch, not the price level, emptied his checkout |
| Closes after a long spinner, then "try free first" | Time the checkout load; preload it when the plan page opens | A slow checkout looks like a price objection |
| Most signed-in users chose "continue free" | Ask after they have used one free thing, with one reason to pay now | He was asking before they saw any value |
| One line said both "pay now" and "free" | One plain price line that can't be read two ways | Mixed messages close checkouts fast |
| The page showed a count that wasn't his own | Show only real, current counts | "Otherwise we are selling fog" |
| The only "why" answers came from desktop | Record the close and ask on the next visit | Mobile visitors leave with the back button and never see the question |
| A plain "Start free" button beat a button named after the product | Use the action the visitor wants, not your product's noun | Visitors click what they understand |
| Rage clicks clustered on a later step, not the homepage | Fix the step where they rage-click first | The homepage wasn't the problem |
| Sign-ups came from the homepage and the brand, not the SEO pages | Improve the homepage before adding pages | Most first visits land there |
| Very few visitors at all | Get traffic first (posts, an email to past openers) before any redesign | Under about 50 real visitors a week, the fix is distribution |

**The hook:**
- **One big real number, specific and true today.** Your own result over a real chart, in the exact words you can prove. Never round up and never drop a "~".
- **The buyer's problem first, the product second.** "I wanna see the pain so I can relate to it and then find more." A hook that worked: the buyer's own question as the headline ("Why isn't anyone paying?"), with the button "Find out why".
- **One thing on the page reacts to the visitor.** Ideally the product makes the visitor's own result as they type or scroll. A clean, text-only page is easy to skip.
- **3 seconds.** A visitor must know what it is, who it's for and what to click in 3 seconds. Short and cryptic fails as hard as long: "AI finds your pricing fix" got "what's the context?".
- **No made-up names.** A named lead magnet nobody knows ("Price X-ray") tells the visitor nothing.

**Remove before you add.** "We keep stacking text walls and no value." Before adding a block, name what it replaces. Count the lines a skimmer must read to get the point, and keep it to 5 or fewer.

**For any design change, show 3 options: bold, middle and safe.** Recommend one.

**When a number moves a lot, check the tracking first.**

## Quality bar
- [ ] Every step has an event, or the missing one is named as fix #1.
- [ ] Own visits and tests are excluded, and the filter is stated.
- [ ] Counts, not percentages, under 20 people per step.
- [ ] The visitors' "why" answers are quoted word for word.
- [ ] One fix, with what it replaces, and 3 options for any design change.
- [ ] Every number on the page is true today; product screens are real.

## Never
- Use borrowed counts, fake reviews or dark patterns.
- Let the price surprise anyone at checkout.
- Present the author's taste as a rule. These rules are universal: true numbers, real screens, the same price everywhere. His brand's look (white ground, hairlines, no tinted bands) is his choice, not a rule for your page.
- Ship a change. Gates: `shared/gates.md`.

## Shared knowledge
**Read first:** `knowledge/numbers.md`, `knowledge/decisions.md`, `knowledge/pages/home.md`. **Write after:** the fix and its reason in `knowledge/pages/home.md`, the check in `knowledge/checks/<date>-funnel.md`, one dated line in `knowledge/log/<date>.md`. Paths from `shared/knowledge-tree.md`.

## Bootstrapped core
Ask `recipes` (area `distribution`) before step 1, `lessons` (theme `money-and-pricing`, `truth-and-numbers`) at the decision rules, and `evidence` for the author's real counts behind each row. If it isn't connected, carry on with this method.
