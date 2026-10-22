#!/usr/bin/env bash
# The author's own Claude Code setup, for Bootstrapped OS. Safe to re-run: installed items are skipped.
# Installs plugins and connectors into YOUR Claude Code (user scope). Nothing is bought; sign-ins open in your browser.
set -u
ok() { printf '  \033[32m✓\033[0m %s\n' "$1"; }
no() { printf '  \033[31m✗\033[0m %s\n' "$1"; }
have() { claude plugin list 2>/dev/null | grep -q "$1"; }

echo "1/4 Official plugins (the same ones the author runs)"
claude plugin marketplace add anthropics/claude-plugins-official >/dev/null 2>&1 || true
for p in superpowers frontend-design code-review feature-dev code-simplifier github supabase posthog chrome-devtools-mcp resend typescript-lsp claude-md-management claude-code-setup; do
  if have "$p@claude-plugins-official"; then ok "$p (already)"; elif claude plugin install "$p@claude-plugins-official" >/dev/null 2>&1; then ok "$p"; else no "$p (install it later with: claude plugin install $p@claude-plugins-official)"; fi
done

echo "2/4 Payments: AgentaOS plugin (the author's company)"
claude plugin marketplace add AgentaOS/agentaos >/dev/null 2>&1 || true
if have "agentaos@agentaos"; then ok "agentaos (already)"; elif claude plugin install agentaos@agentaos >/dev/null 2>&1; then ok "agentaos"; else no "agentaos"; fi

echo "3/4 Connectors"
if claude mcp list 2>/dev/null | grep -q "^vercel:"; then ok "vercel (already)"; else claude mcp add --scope user --transport http vercel https://mcp.vercel.com >/dev/null 2>&1 && ok "vercel" || no "vercel"; fi
if claude mcp list 2>/dev/null | grep -q "^notion:"; then ok "notion (already, optional)"; else claude mcp add --scope user --transport http notion https://mcp.notion.com/mcp >/dev/null 2>&1 && ok "notion (optional)" || no "notion"; fi

echo "Bootstrapped core (members): your key from the app, Account -> Your Bootstrapped key"
if [ -n "${BOOTSTRAPPED_KEY:-}" ]; then ok "key already set"; else
  printf "  Paste your Bootstrapped key (Enter to skip): "; read -r BMK
  if [ -n "$BMK" ]; then
    case "$SHELL" in *zsh*) RC="$HOME/.zshrc";; *) RC="$HOME/.bashrc";; esac
    grep -q "BOOTSTRAPPED_KEY" "$RC" 2>/dev/null || echo "export BOOTSTRAPPED_KEY=\"$BMK\"" >> "$RC"
    ok "saved to $RC (open a new terminal, then start Claude Code)"
  else no "skipped: the method works without it; add it any time"; fi
fi

echo "4/4 Command-line tools"
command -v node >/dev/null && ok "node $(node -v)" || no "node: install Node.js 20+ from nodejs.org"
command -v gh >/dev/null && ok "gh" || no "gh: install GitHub CLI from cli.github.com, then gh auth login"

cat <<'TXT'

Then, once, inside Claude Code:
  /mcp      sign in to supabase, posthog, vercel, agentaos, resend (each opens your browser)
  /chrome   install the Claude in Chrome extension and choose "Enabled by default"
            (your agents check pages in this visible Chrome; Chrome DevTools is the second browser)
Gmail: Claude settings -> Connectors -> Gmail (drafts only; you send).
Design kit (optional): see INSTALL.md.
TXT
