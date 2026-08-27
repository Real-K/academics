# -*- coding: utf-8 -*-
"""저널 한도 점검 — 초록 단어수·본문 단어수·highlights 글자수. 사용:
python3 limits_check.py <manuscript.md> [--abstract-max 250] [--body-max 10000] [--highlights <file.md> --hl-max-chars 85 --hl-count 5]"""
import re, sys, argparse
ap = argparse.ArgumentParser(); ap.add_argument("md"); ap.add_argument("--abstract-max", type=int, default=250); ap.add_argument("--body-max", type=int, default=None)
ap.add_argument("--highlights"); ap.add_argument("--hl-max-chars", type=int, default=85); ap.add_argument("--hl-count", type=int, default=5)
a = ap.parse_args(); t = open(a.md, encoding="utf-8").read(); bad = 0
m = re.search(r"^## Abstract\s*\n(.*?)(?=^## |\Z)", t, re.S | re.M); ab = m.group(1) if m else ""
ab_words = len(re.findall(r"\b[\w'’-]+\b", re.sub(r"^\*\*[^*\n]+\*\*.*$", "", ab, flags=re.M)))
body = t.split("## References")[0]; body = re.sub(r"\|.*\|", "", body); bw = len(re.findall(r"\b[\w'’-]+\b", body))
flag = lambda ok: "✓" if ok else "🔴"
print(f"초록 {ab_words} 단어 / 한도 {a.abstract_max} {flag(ab_words <= a.abstract_max)}"); bad += ab_words > a.abstract_max
if a.body_max: print(f"본문(표 제외) {bw:,} 단어 / 한도 {a.body_max:,} {flag(bw <= a.body_max)}"); bad += bw > a.body_max
else: print(f"본문(표 제외) {bw:,} 단어")
if a.highlights:
    hl = [l[2:].strip() for l in open(a.highlights, encoding="utf-8") if l.startswith("- ")]
    print(f"highlights {len(hl)}개 / {a.hl_count} · 최장 {max(map(len, hl)) if hl else 0}자 / {a.hl_max_chars} {flag(len(hl) == a.hl_count and all(len(h) <= a.hl_max_chars for h in hl))}")
    bad += not (len(hl) == a.hl_count and all(len(h) <= a.hl_max_chars for h in hl))
sys.exit(1 if bad else 0)
