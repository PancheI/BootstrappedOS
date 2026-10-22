#!/usr/bin/env bash
# Enforced gates: commands that ship, merge, migrate, publish, send email, move money or delete widely always ask the founder first.
# Reads only the command itself (not descriptions), so a word like "main" elsewhere never triggers it.
input="$(cat)"
# Read the command with python3, else jq. If neither can read it, ask instead of allowing (fail closed).
if command -v python3 >/dev/null 2>&1; then
  cmd="$(printf '%s' "$input" | python3 -c 'import sys,json
try: print(json.load(sys.stdin).get("tool_input",{}).get("command",""))
except Exception: print("@@UNREADABLE@@")' 2>/dev/null)"
elif command -v jq >/dev/null 2>&1; then
  cmd="$(printf '%s' "$input" | jq -r '.tool_input.command // ""' 2>/dev/null || echo "@@UNREADABLE@@")"
else
  cmd="@@UNREADABLE@@"
fi
ask() {
  local shown; shown="$(printf '%s' "$cmd" | tr '\n\t' '  ' | cut -c1-120 | sed 's/\\/\\\\/g; s/"/\\"/g')"
  printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Gate: %s. Command: %s. The founder must say go."}}\n' "$1" "$shown"
  exit 0
}
if [ "$cmd" = "@@UNREADABLE@@" ]; then
  cmd="(unreadable)"; ask "could not read this command (install python3 or jq so the gates can check it)"
fi
[ -z "$cmd" ] && exit 0
branch="$(git rev-parse --abbrev-ref HEAD 2>/dev/null || true)"
# Detached or unknown branch (CI checkouts, rebases): treat it like main, so a bare push or merge asks (fail closed).
unknown=""; [[ -z "$branch" || "$branch" == "HEAD" ]] && unknown=1
c=" $cmd "
m() { printf '%s' "$c" | grep -Eq -- "$1"; }
mi() { printf '%s' "$c" | grep -Eqi -- "$1"; }

# git: pushes to main/master (explicit, +refspec, refs/heads, HEAD, bare push while on main), force, mirror, tags,
# merges into main, deleting main, hard resets
m 'git +push[^;&|]*(--force|-f( |$)|--tags|--follow-tags|--mirror)' && ask "force, mirror or tag push"
m 'git +push[^;&|]*[ :+](refs/heads/)?(main|master)( |$)' && ask "push to main"
if m 'git +push( |$)' && [[ "$branch" == "main" || "$branch" == "master" ]]; then ask "push while on $branch"; fi
# Unknown branch: a bare push (no branch named) could go anywhere, so it asks; naming a branch is fine.
if [[ -n "$unknown" ]] && m 'git +push( +[A-Za-z0-9._-]+)? *($|[;&|])'; then ask "push with no branch named, on an unknown branch"; fi
m 'git +push[^;&|]* v?[0-9]+\.[0-9]+' && ask "tag push"
m 'gh +pr +merge' && ask "merging a pull request"
if m 'git +merge( |$)' && { [[ "$branch" == "main" || "$branch" == "master" || -n "$unknown" ]] || m 'checkout +(main|master)|switch +(main|master)'; }; then ask "merge into main"; fi
m 'git +reset +--hard|git +clean +-[a-z]*f' && ask "discarding work"
m 'git +(checkout|restore)( +--[a-z-]+)*( +--)? +\.( |$)' && ask "discarding work"
m 'git +branch +(-D|--delete +--force|-d +-f)[^;&|]* (main|master)( |$)' && ask "deleting the main branch"

# databases
mi 'supabase +(db +(push|reset)|migration +up)|prisma +(migrate +(deploy|reset)|db +push)|drizzle-kit +(push|migrate)|knex +migrate|rails +db:(migrate|drop|reset)|dropdb ' && ask "database migration or reset"
mi '(psql|mysql|sqlite3|mongosh)[^;&|]*\b(drop|truncate|delete +from|alter +table|dropDatabase)\b' && ask "destructive SQL"
mi '(psql|mysql)[^;&|]* (-f|--file)[ =]' && ask "running a SQL file"

# deploys, publishing and releases
mi '(vercel|netlify)[^;&|]*--prod|wrangler +(pages +)?deploy|fly +deploy|railway +up|terraform +(apply|destroy)|serverless +deploy|firebase +deploy|(npm|pnpm|yarn|bun) +publish|(npm|pnpm|yarn|bun) +(run +)?deploy|heroku[^;&|]*(releases|deploy)' && ask "deploy or publish"
m 'gh +release +create' && ask "publishing a release"
m 'gh +repo +(delete|archive)' && ask "deleting or archiving a repository"

# A request that writes: POST/PUT/PATCH/DELETE, or a body (curl -d/-F/--json, wget --post-data, httpie POST)
writes='(-X *(POST|PUT|PATCH|DELETE)|--request *(POST|PUT|PATCH|DELETE)| (-d|--data[a-z-]*|-F|--form|--json|--post-data|--post-file)[ =]|--method *(POST|PUT|PATCH|DELETE)| (POST|PUT|PATCH|DELETE) )'

# email: sending through an email API from the shell (agents draft; the founder sends)
if mi '(^|[ ;&|(])(curl|wget|http|https|xh) [^;&|]*(api\.resend\.com|api\.sendgrid\.com|api\.postmarkapp\.com|api\.(eu\.)?mailgun\.net)' && mi "$writes"; then
  ask "sending email through an API"
fi

# money: payment APIs and CLIs that charge, refund, pay out or change billing
if mi '(^|[ ;&|(])(curl|wget|http|https|xh) [^;&|]*(api\.agentaos\.ai|api\.stripe\.com|api\.paddle\.com|sandbox-api\.paddle\.com|api\.lemonsqueezy\.com|api(-m)?\.paypal\.com|connect\.squareup\.com|api\.gumroad\.com|api\.mollie\.com|api\.wise\.com|b2b\.revolut\.com)' \
  && mi "$writes"; then
  ask "a payment API call that can move money"
fi
mi 'stripe +([a-z_]+ +)?(create|update|delete|cancel|refund|capture|pay|void|close)( |$)|stripe +(refunds|payouts|transfers|charges)( |$)|stripe +post ' && ask "a payment command that can move money"

mi '(npm +run +plans|create-plans\.mjs)[^;&|]*--live' && ask "creating live payment plans"

# cloud and container wipes
mi 'aws +s3 +(rm[^;&|]*--recursive|rb )|gsutil[^;&|]* rm[^;&|]* -r|docker +(system|volume|image) +prune|kubectl +delete +(namespace|ns|pv|pvc|deployment)' && ask "deleting cloud or container data"

# wide deletes: rm (with or without sudo) with a recursive flag aimed at /, ~, $HOME, ., .., * (optional trailing slash)
m '(^|[ ;&|(])(sudo +)?rm +(-[a-zA-Z-]+ +)*-[a-zA-Z]*[rR][a-zA-Z]*( +-[a-zA-Z-]+)* +(/|/\*|~/?|~/\*|\$HOME/?|\$\{HOME\}/?|\./?|\.\./?|\./\*|\*)( |$)' && ask "deleting a whole folder tree"
m '(^|[ ;&|(])(sudo +)?rm +(-[a-zA-Z-]+ +)*--recursive( +-[a-zA-Z-]+)* +(/|~/?|\$HOME/?|\./?|\.\./?|\*)( |$)' && ask "deleting a whole folder tree"
exit 0
