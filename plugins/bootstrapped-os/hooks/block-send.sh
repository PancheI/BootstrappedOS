#!/usr/bin/env bash
# Agents draft, the founder sends. Any "send" tool on email or chat is blocked.
cat >/dev/null
printf '%s\n' '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"deny","permissionDecisionReason":"Drafts only: create a draft and let the founder send it."}}'
exit 0
