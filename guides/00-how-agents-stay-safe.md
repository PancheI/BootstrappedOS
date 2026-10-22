# How your AI team stays safe

**Agents read, research and draft. You send, ship, pay and delete.** The full list of what needs your yes: [`shared/gates.md`](../plugins/bootstrapped-os/shared/gates.md).

## See it for yourself (3 minutes, once)
1. In a terminal, copy the repo and run the gate tests:
   ```
   git clone https://github.com/PancheI/BootstrappedOS ~/bootstrapped-os
   bash ~/bootstrapped-os/plugins/bootstrapped-os/hooks/test-hooks.sh
   ```

   **You should see** one line per command, each marked `ASK` (it stops for your yes) or `allow`, for example `ok     ASK   git push origin main`. The last line is `All gate tests pass.`

## The rules
1. **Gates are enforced, not hoped for.** The core plugin's hooks stop pushes to main, merges, migrations, deploys, publishing, money moves and wide deletes until you say yes.
2. **Drafts, never sends.** Email and chat tools that send, reply, forward or post are blocked. Agents write drafts; you press send.
3. **"go" is not "deploy".** `go 1 3` builds and shows those items locally. Only "ship" or "deploy" goes to production. "ok" approves nothing.
4. **Read and write are different agents.** The `watch` agent only reads, so you can schedule it (Claude Code scheduled tasks or cron).
5. **One customer per agent.** Two customers in one context get mixed up, and the customer notices.
6. **Numbered proposals.** `/run-ops` lists actions 1, 2, 3. Nothing runs until you type a number. Silence approves nothing. A list older than 48 hours is checked again before anything runs.
7. **Check it for real.** Website changes are checked in a real, visible browser before "done".
8. **Write it down.** Said twice: a rule in `knowledge/rules.md`. Done every week: a skill.

## Avoid
- **Turning a hook off "just this once".** Approve the one action instead; the hook asks again next time.
- **Tools you added after install.** The hooks can't see every new tool or a browser click. The rule still applies: the agent stops and asks.
- **Automating the last click.** Automate the gathering and the draft. Keep the click that sends, pays or deletes for yourself.

**Files behind this:** `plugins/bootstrapped-os/hooks/`, `plugins/bootstrapped-os/shared/gates.md`
