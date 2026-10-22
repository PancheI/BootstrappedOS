# Connectors (add only the tools you use)

In Claude Code: `claude mcp add ...` (examples below), then `/mcp` to sign in. CLI rows need no connector: sign in once and Claude runs the command. Check each tool's own docs for its current connector; these are the ones I use.

| Job | Tool | Add it |
|---|---|---|
| Analytics | PostHog | `claude mcp add --transport http posthog https://mcp.posthog.com/mcp` |
| Notes / knowledge | Notion | `claude mcp add --transport http notion https://mcp.notion.com/mcp` |
| Email | Gmail | built into Claude (Settings -> Connectors) |
| Code | GitHub | CLI: `gh auth login` (Claude runs `gh` for issues, PRs, Actions) |
| Hosting | Vercel | `claude mcp add --transport http vercel https://mcp.vercel.com` |
| Database | Supabase | `claude mcp add --transport http supabase https://mcp.supabase.com/mcp` (add `?project_ref=<id>&read_only=true` to limit it) |
| DNS / Workers | Cloudflare | CLI: `npx wrangler login` |
| Voice | ElevenLabs | `claude mcp add elevenlabs -e ELEVENLABS_API_KEY="$ELEVENLABS_API_KEY" -- uvx elevenlabs-mcp` |
| Video help | Remotion docs | `claude mcp add remotion-docs -- npx -y @remotion/mcp@latest` |
| Payments | AgentaOS (my company - disclosure) | `claude mcp add --transport http agentaos https://mcp.agentaos.ai/mcp` |

Using Stripe, Shopify, HubSpot, Google Analytics or others? Search "<tool> MCP" - most major tools publish one. No connector? Export a CSV and give it to Claude.
