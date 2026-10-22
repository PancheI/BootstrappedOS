#!/usr/bin/env python3
# Live view of a background run (claude -p ... --output-format stream-json --verbose > run.jsonl):
#   python3 watch-run.py run.jsonl
# Interactive runs don't need this: you see every stage in the Claude Code window, and knowledge/progress.md.
import json, os, sys, time

# Stage names as in plugins/bootstrapped-os/shared/stages.md (names only, so they never drift)
STAGES = {"head-of-research": "Idea", "idea-critic": "Idea (critic)", "head-of-positioning": "Positioning",
          "brand-designer": "Brand", "cfo": "Pricing / payments", "head-of-design": "Landing page",
          "head-of-infrastructure": "Deploy", "architect": "Product", "implementer": "Product",
          "reviewer": "Product", "verifier": "Product", "creative-director": "Launch video",
          "head-of-growth": "Launch", "head-of-sales": "First customers", "head-of-content": "Launch (content)"}

TOTALS = {}   # stage -> [calls, input+cache tokens, output tokens, models]
current = ["Chief of Staff"]

def tally(d):
    m = d.get("message")
    if not isinstance(m, dict) or d.get("type") != "assistant":
        return
    u = m.get("usage") or {}
    t = TOTALS.setdefault(current[0], [0, 0, 0, set()])
    t[0] += 1
    t[1] += (u.get("input_tokens") or 0) + (u.get("cache_read_input_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0)
    t[2] += u.get("output_tokens") or 0
    if m.get("model"):
        t[3].add(str(m["model"]).replace("claude-", ""))

def summary():
    print("\n\033[1m LLM calls by stage\033[0m")
    for stage, (calls, tin, tout, models) in TOTALS.items():
        print(f"   {stage:<20} {calls:>4} calls  {tin/1000:>8.0f}k in  {tout/1000:>6.1f}k out  {', '.join(sorted(models))}")

def show(d):
    stamp = time.strftime("%H:%M")
    tally(d)
    if d.get("type") == "result":
        summary()
        print(f"\n✅ DONE · total cost ${d.get('total_cost_usd', 0):.2f} (as reported by Claude Code)\n")
        return
    m = d.get("message")
    content = m.get("content") if isinstance(m, dict) else None
    if not isinstance(content, list):
        return
    inner = "   ↳ " if d.get("parent_tool_use_id") else ""
    for c in content:
        if not isinstance(c, dict):
            continue
        if c.get("type") == "tool_use":
            name, i = c.get("name"), c.get("input") or {}
            if name in ("Agent", "Task"):
                a = str(i.get("subagent_type", "")).split(":")[-1]
                if TOTALS:
                    summary()
                current[0] = STAGES.get(a, a)
                print(f"\n\033[1;35m[{stamp}] ▶ STAGE {current[0]}  ({a})\033[0m")
            elif name == "Skill":
                print(f"[{stamp}] {inner}\033[36m📘 skill {i.get('skill')}\033[0m")
            elif name == "WebSearch":
                print(f"[{stamp}] {inner}🔎 {str(i.get('query', ''))[:100]}")
            elif name == "WebFetch":
                print(f"[{stamp}] {inner}🌐 {str(i.get('url', ''))[:100]}")
            elif name in ("Write", "Edit"):
                print(f"[{stamp}] {inner}📝 {os.path.basename(str(i.get('file_path', '')))}")
            elif name == "Bash":
                cmd = str(i.get("command", "")).strip().splitlines()
                print(f"[{stamp}] {inner}⚙️  {(cmd[0] if cmd else '')[:100]}")
        elif c.get("type") == "text" and not inner:
            print(f"[{stamp}] 💬 {str(c.get('text', ''))[:400]}")

f = open(sys.argv[1])
while True:
    line = f.readline()
    if not line:
        time.sleep(0.5)
        continue
    try:
        d = json.loads(line)
        if isinstance(d, dict):
            show(d)
    except Exception as e:
        print(f"   (skipped a line: {e})")
    sys.stdout.flush()
