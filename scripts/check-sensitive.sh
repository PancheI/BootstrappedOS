#!/usr/bin/env bash
# Blocks sensitive info from ever being committed: keys and tokens, private keys, email addresses, phone numbers,
# local paths, and any term in a private denylist (names of customers, merchants, people) kept OUTSIDE the repo.
#   scripts/check-sensitive.sh            check staged files (pre-commit)
#   scripts/check-sensitive.sh --all      check every tracked file (CI)
# Private denylist, one term per line: ~/.config/bootstrapped-os/denylist.txt (or $SENSITIVE_DENYLIST).
set -uo pipefail
cd "$(git rev-parse --show-toplevel)"
if [ "${1:-}" = "--all" ]; then files=$(git ls-files); else files=$(git diff --cached --name-only --diff-filter=ACMR); fi
[ -z "$files" ] && exit 0

patterns=(
  'sk-(ant-)?[A-Za-z0-9_-]{20,}'                 # Anthropic / OpenAI keys
  'eyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}'    # JWTs (Supabase service keys)
  'sb_(secret|publishable)_[A-Za-z0-9_-]{16,}'   # Supabase new keys
  're_[A-Za-z0-9]{20,}'                          # Resend
  'bm_live_[A-Za-z0-9]{12,}'                     # Bootstrapped core keys
  'gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}'
  'AKIA[0-9A-Z]{16}'                             # AWS
  'xox[abpr]-[A-Za-z0-9-]{10,}'                  # Slack
  '[0-9]{8,10}:AA[A-Za-z0-9_-]{30,}'             # Telegram bot tokens
  'phc_[A-Za-z0-9]{30,}'                         # PostHog project keys
  '-----BEGIN [A-Z ]*PRIVATE KEY-----'
  '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}' # email addresses (allowed: example.com/org/net, noreply)
  '\+[0-9][0-9 ]{9,}[0-9]'                       # phone numbers
  '/Users/[a-z][A-Za-z0-9._-]+|/home/[a-z][A-Za-z0-9._-]+|C:\\Users\\[A-Za-z][A-Za-z0-9._-]+'  # local paths
)
allow='@example\.(com|org|net)|@yourdomain\.|@yourcompany\.|noreply|users\.noreply\.github\.com|you@|name@|/Users/<|C:\\Users\\<|/home/<|git@github\.com'
fail=0
for f in $files; do
  [ -f "$f" ] || continue
  case "$f" in *.png|*.jpg|*.jpeg|*.gif|*.webp|*.ico|*.woff|*.woff2|*.mp4|*.zip) continue;; esac
  [ "$f" = "scripts/check-sensitive.sh" ] && continue
  for p in "${patterns[@]}"; do
    hits=$(grep -nE -- "$p" "$f" 2>/dev/null | grep -vE -- "$allow")
    [ -n "$hits" ] && { echo "✗ $f: matches a sensitive pattern"; echo "$hits" | head -3 | cut -c1-160; fail=1; }
  done
done
deny="${SENSITIVE_DENYLIST:-$HOME/.config/bootstrapped-os/denylist.txt}"
if [ -f "$deny" ]; then
  while IFS= read -r term; do
    [ -z "$term" ] || [ "${term:0:1}" = "#" ] && continue
    for f in $files; do [ -f "$f" ] && grep -qiF -- "$term" "$f" && { echo "✗ $f: contains a denylisted term"; fail=1; }; done
  done < "$deny"
fi
if [ $fail -ne 0 ]; then echo; echo "Blocked: sensitive info. Remove it (or, for a false positive, change the wording)."; exit 1; fi
echo "✓ No sensitive info found."
