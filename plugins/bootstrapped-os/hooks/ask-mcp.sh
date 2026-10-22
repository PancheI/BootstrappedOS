#!/usr/bin/env bash
# Connector (MCP) tools that change the database, deploy, move money, post in public or delete ask the founder first.
# hooks.json decides which tools reach this script; it always asks. The tool name only picks the reason shown.
input="$(cat)"
name=""
if command -v python3 >/dev/null 2>&1; then
  name="$(printf '%s' "$input" | python3 -c 'import sys,json
try: print(json.load(sys.stdin).get("tool_name",""))
except Exception: print("")' 2>/dev/null)"
elif command -v jq >/dev/null 2>&1; then
  name="$(printf '%s' "$input" | jq -r '.tool_name // ""' 2>/dev/null)"
fi
action="${name##*__}"
shopt -s nocasematch
case "$action" in
  *refund*|*payout*|*transfer*|*charge*|*payment*|*subscription*) why="a connector wants to move money or change billing" ;;
  *post*|*tweet*|*share*) why="a connector wants to post or share in public" ;;
  *migration*|*sql*|*drop*|*reset*|*deploy*) why="a connector wants to change the database or deploy" ;;
  *delete*|*trash*|*remove*) why="a connector wants to delete something" ;;
  *) why="a connector wants to change data, move money or deploy" ;;
esac
printf '{"hookSpecificOutput":{"hookEventName":"PreToolUse","permissionDecision":"ask","permissionDecisionReason":"Gate: %s. The founder must say go."}}\n' "$why"
exit 0
