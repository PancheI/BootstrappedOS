# Choosing the model for each job (the Chief of Staff decides, per dispatch)

Every agent has a default model in its file. When you dispatch it, set the model for THIS job by how hard it is. Say the choice in one line ("cfo on opus: three models and a roast").

| Job | Model | Why |
|---|---|---|
| Judgement with money or direction at stake: idea research and the idea critic (the idea stage), positioning and the roast, choosing a pricing model, an architecture design, a kill or pivot call, the final review before the founder sees a page | **opus** | One wrong call here costs more than every token in the run |
| Normal work: follow-up research on a chosen wedge (first 20 people, a price check), drafting copy, building a page or a feature, writing posts and emails, deploy steps | **sonnet** | Good enough, a fraction of the cost |
| Mechanical: browser checks and screenshots, one short draft from a template, reformatting, counting, moving files, the daily watch | **haiku** | Fast and cheap; the output is checked anyway |

## Escalate and step down
- **Escalate to opus** when a sonnet result fails its gate, the founder rejects it as generic, a reviewer finds a real error in it, or two sources disagree and someone has to judge.
- **Step down** for retries of the same mechanical step, and for anything you're only re-checking.
- **Never** run a whole stage on opus because one part was hard: split it, and send only the hard part to opus.

## Budget
Every agent's completion report includes its tokens, tool calls and duration: log them per stage in `knowledge/progress.md`, never estimate them. If one stage uses more than about half of the run's tokens, say so at its gate and offer a cheaper way (a smaller model, a tighter time box, fewer sources).
At the start of a run, say the plan in one line ("opus for positioning and pricing, sonnet for the rest, haiku for checks"). In `knowledge/progress.md`, note the model each stage used, so the founder sees where the money went.
