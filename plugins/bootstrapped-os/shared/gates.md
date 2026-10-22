# Gates: what needs the founder's yes

Agents read, research and draft. Anything that leaves the computer, costs money or can't be undone waits for the founder.

| Action | What happens | Enforced by |
|---|---|---|
| Send an email, DM, reply or post | Connector send tools are blocked; email and social APIs called from the shell ask. The agent writes a draft. The founder sends it. | `hooks/block-send.sh`, `hooks/guard-gates.sh` |
| Push or merge to main, force push, tag, release | Asks | `hooks/guard-gates.sh` |
| Deploy to production, publish a package | Asks | `hooks/guard-gates.sh`, `hooks/ask-mcp.sh` |
| Database migration, reset or destructive SQL | Asks | `hooks/guard-gates.sh`, `hooks/ask-mcp.sh` |
| Anything that can move money (charge, refund, payout, live plans) | Asks | `hooks/guard-gates.sh`, `hooks/ask-mcp.sh` |
| Delete data (contacts, threads, folders, cloud storage) | Asks | `hooks/guard-gates.sh`, `hooks/ask-mcp.sh` |
| Clicks in the browser | Not hooked. The agent stops before any click that submits, buys, sends or deletes. | this rule |

## The approval words
- **"go"** or **"go 1 3"**: do those items, locally. Show the result.
- **"ship"** or **"deploy"**: production. Only these words, only for what was shown.
- **"ok"**, "looks good" or "nice" are not approvals. Ask again with the numbers.

An approval covers one action, one time. A new action needs a new yes.

The hooks can't see everything (a browser click, a tool the founder added after install). Where a hook can't stop it, this rule still applies. Run `bash hooks/test-hooks.sh` to see what is enforced.
