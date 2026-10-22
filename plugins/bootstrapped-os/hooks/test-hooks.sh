#!/usr/bin/env bash
# Run this to see exactly what the gates stop and allow:  bash hooks/test-hooks.sh
H="$(cd "$(dirname "$0")" && pwd)"
t() { local exp="$1" cmd="$2"; out="$(printf '{"tool_input":{"command":%s}}' "$(python3 -c 'import json,sys;print(json.dumps(sys.argv[1]))' "$cmd")" | "$H/guard-gates.sh")"
  got=allow; [[ "$out" == *'"ask"'* ]] && got=ASK; [[ "$got" == "$exp" ]] && r=ok || { r=WRONG; WRONG_COUNT=$((WRONG_COUNT+1)); }; printf '%-6s %-5s %s\n' "$r" "$got" "$cmd"; }
cd "$(mktemp -d)" && git init -q -b feature && git commit -q --allow-empty -m x
t allow "git push origin feature"; t ASK "git push origin main"; t ASK "git push origin HEAD:main"; t allow "git push origin domain-fix"
t allow "git push origin feature/maintenance-page"; t ASK "git push --force"; t ASK "git push origin v1.0.0"; t ASK "gh pr merge 12"
t ASK "git checkout main && git merge feature"; t ASK "git reset --hard HEAD~1"; t ASK "supabase db push"; t ASK "supabase db reset"
t ASK "prisma migrate reset --force"; t ASK "npx drizzle-kit push"; t ASK "psql -c 'DROP TABLE users'"; t allow "psql -c 'select * from deleted_users'"
t ASK "vercel --prod"; t ASK "npx wrangler pages deploy dist"; t ASK "fly deploy"; t ASK "railway up"; t ASK "terraform apply"; t ASK "npm publish"; t ASK "pnpm run deploy"
t allow "rm -rf node_modules"; t allow "rm -rf ./dist"; t ASK "rm -rf ~"; t ASK 'rm -rf $HOME'; t allow "npm test"; t allow "git status"
# force pushes and main in disguise
t ASK "git push origin +main"; t ASK "git push origin feature:refs/heads/main"; t ASK "git push origin --mirror"; t ASK "git push --force-with-lease"
t ASK "git branch -D main"; t allow "git branch -D old-feature"; t ASK "git push origin --delete main"
# wide deletes, every spelling
t ASK "rm -rf ~/"; t ASK "rm -r -f ~"; t ASK "rm -fr ~"; t ASK "rm -rf ."; t ASK "rm -rf *"; t ASK "sudo rm -rf /"; t ASK "rm --recursive --force ~"; t allow "rm -rf ./build"; t allow "rm -r tmp/cache"
# SQL in any case, SQL files
t ASK "psql -c 'drop table users'"; t ASK "psql \$DATABASE_URL -f wipe.sql"; t allow "psql -c 'select count(*) from users'"
# money
t ASK "curl -X POST https://api.stripe.com/v1/refunds -d charge=ch_1"; t ASK "curl https://api.stripe.com/v1/payouts -d amount=100"; t allow "curl https://api.stripe.com/v1/balance -u sk_test_x:"
t ASK "stripe refunds create --charge ch_1"; t ASK "stripe subscriptions cancel sub_1"; t allow "stripe listen --forward-to localhost:3000"
t ASK "npm run plans -- --yes --live"; t allow "npm run plans -- --yes"; t allow "npm run golive"
# releases, repos, cloud
t ASK "gh release create v1.0"; t ASK "gh repo delete x --yes"; t ASK "aws s3 rm s3://b --recursive"; t ASK "docker system prune -af"; t allow "docker ps"
# discarding local work
t ASK "git checkout -- ."; t ASK "git restore ."; t ASK "git restore --staged --worktree ."; t allow "git checkout feature"; t allow "git restore src/app.ts"
# email sent through an API from the shell
t ASK "curl -X POST https://api.resend.com/emails -H 'Authorization: Bearer re_x' -d '{}'"; t ASK "curl https://api.sendgrid.com/v3/mail/send --json '{}'"
t ASK "curl -X POST https://api.postmarkapp.com/email -d x"; t ASK "curl -s https://api.mailgun.net/v3/example.com/messages -F to=a@b.c"
t ASK "http POST https://api.resend.com/emails to=a@b.c"; t allow "curl https://api.resend.com/emails/abc -H 'Authorization: Bearer re_x'"
# payment APIs, including the author's own
t ASK "curl -X POST https://api.agentaos.ai/v1/refunds -d x"; t allow "curl https://api.agentaos.ai/v1/balance"
t ASK "curl -X POST https://api.lemonsqueezy.com/v1/refunds -d x"; t ASK "curl -X POST https://api.paddle.com/adjustments --json '{}'"; t ASK "wget --post-data=x https://api.stripe.com/v1/refunds"
git checkout -q -b main; t ASK "git push"; t ASK "git merge feature"

# Connector (MCP) tools: which hook in hooks.json each tool name reaches, and what it decides
tm() { local exp="$1" name="$2"
  got="$(CLAUDE_PLUGIN_ROOT="$(dirname "$H")" python3 - "$H/hooks.json" "$name" <<'PY'
import json, os, re, subprocess, sys
hooks, name = json.load(open(sys.argv[1])), sys.argv[2]
got = "allow"
for entry in hooks["hooks"]["PreToolUse"]:
    if entry["matcher"] == "Bash" or not re.search(entry["matcher"], name):
        continue
    for h in entry["hooks"]:
        cmd = os.path.expandvars(h["command"]).strip('"')
        out = subprocess.run([cmd], input=json.dumps({"tool_name": name, "tool_input": {}}), capture_output=True, text=True).stdout
        if '"deny"' in out: got = "DENY"
        elif '"ask"' in out and got != "DENY": got = "ASK"
print(got)
PY
)"
  [[ "$got" == "$exp" ]] && r=ok || { r=WRONG; WRONG_COUNT=$((WRONG_COUNT+1)); }; printf '%-6s %-5s %s\n' "$r" "$got" "$name"; }
echo
# send tools are blocked, drafts pass
tm DENY mcp__claude_ai_Gmail__send_message; tm DENY mcp__plugin_resend_resend__send-email; tm allow mcp__claude_ai_Gmail__create_draft
# database and deploy
tm ASK mcp__supabase__apply_migration; tm ASK mcp__vercel__deploy_to_production
# money
tm ASK mcp__stripe__create_refund; tm ASK mcp__agentaos__create_payout; tm ASK mcp__stripe__create_transfer; tm ASK mcp__stripe__create_charge
tm ASK mcp__shop__create_payment; tm ASK mcp__stripe__cancel_subscription; tm allow mcp__stripe__list_refunds; tm allow mcp__agentaos__get_payout
# posting in public
tm ASK mcp__linkedin__create_post; tm ASK mcp__x__create_tweet; tm ASK mcp__x__tweet; tm ASK mcp__linkedin__share; tm ASK mcp__plugin_resend_resend__share-email
# deletes
tm ASK mcp__claude_ai_Gmail__trash_thread; tm ASK mcp__hubspot__delete_contact; tm ASK mcp__plugin_resend_resend__remove-contact; tm ASK mcp__notion__remove_page
tm allow mcp__claude_ai_Gmail__untrash_thread; tm allow mcp__claude_ai_Gmail__get_thread; tm allow mcp__claude_ai_Gmail__search_threads
echo; if [ "${WRONG_COUNT:-0}" -gt 0 ]; then echo "$WRONG_COUNT gate test(s) WRONG"; exit 1; fi; echo "All gate tests pass."
