#!/usr/bin/env python3
"""Fails the memo unless every gate row has evidence.
Rows 1-5 need a link, or 'not found (searched: <where>)'. Row 6 (red flags) may say 'none' with a reason.
Row 7 (decision) needs a decision word and a 'because'.
Usage: python3 check-memo.py <memo.md>"""
import re, sys
if len(sys.argv) != 2:
    print("Usage: python3 check-memo.py <memo.md>")
    sys.exit(2)
text = open(sys.argv[1]).read()
rows = {int(m.group(1)): m.group(2).strip() for m in re.finditer(r"^\|\s*(\d)\s*\|[^|]*\|(.*)\|\s*$", text, re.M)}
problems = []
for n in range(1, 8):
    v = rows.get(n, "")
    low = v.lower()
    if not v:
        problems.append(f"row {n}: empty")
    elif n <= 5 and not re.search(r"https?://\S+\.\S+", v) and not re.search(r"not found \(searched: [^)]{8,}\)", low):
        problems.append(f"row {n}: needs a link or 'not found (searched: <where you looked>)'")
    elif n == 6 and not (re.search(r"https?://", v) or re.match(r"none\b.{8,}", low)):
        problems.append("row 6: a link per red flag, or 'none - <why you are confident>'")
    elif n == 7 and not (re.search(r"\b(go ahead|walk away|approve|decline|ask for|pause|proceed)\b", low) and "because" in low):
        problems.append("row 7: a decision (go ahead / ask for / walk away) and 'because ...'")
if "FINAL" in text and problems:
    problems.append("marked FINAL while the gate is incomplete")
print("PASS" if not problems else "FAIL\n- " + "\n- ".join(problems))
sys.exit(0 if not problems else 1)
