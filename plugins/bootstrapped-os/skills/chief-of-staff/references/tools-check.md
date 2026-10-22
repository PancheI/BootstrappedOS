# Tools check (run before /day0 and /start-from-zero, and whenever a stage needs a tool)

Check each one; show a table with ✅ / ❌ and, for every ❌, the exact line to fix it. Never fall back silently: say what's missing and what that stage will do without it.

| Tool | Needed for | Check | Fix |
|---|---|---|---|
| Visible Chrome (Claude in Chrome) | research reading, landing-page and live checks, buying as a buyer in pricing audits | Claude in Chrome tools are available (`/chrome` shows "Status: Enabled") | Install the Claude in Chrome extension, then run `/chrome` and pick "Enabled by default" (or start with `claude --chrome`). Needs a direct Claude plan. Docs: code.claude.com/docs/en/chrome |
| Chrome DevTools (second browser option) | the same checks, plus console, network and Lighthouse | chrome-devtools tools are available | `claude mcp add chrome-devtools --scope user npx chrome-devtools-mcp@latest` |
| Node.js 20+ | the launch starter | `node -v` | nodejs.org |
| GitHub CLI | code, pull requests | `gh auth status` | `gh auth login` |
| Vercel CLI | deploy | `npx vercel whoami` | `npx vercel login` |
| Supabase CLI | database, login | `npx supabase --version` and a project | `npx supabase login` |
| AgentaOS key | payments | `AGENTAOS_API_KEY` set in `.env.local` (never print it) | AgentaOS dashboard → Developers → test key (sk_test_) |
| PostHog | analytics | `NEXT_PUBLIC_POSTHOG_KEY` set | PostHog project settings |
| ElevenLabs | launch-video voice | ElevenLabs tools or `ELEVENLABS_API_KEY` set | `connectors.md` |

**Browser rule:** checks of pages run in a **visible** browser (Claude in Chrome first, Chrome DevTools second) so the founder can watch. A headless browser is a last resort, and you say so in the hand-back.
