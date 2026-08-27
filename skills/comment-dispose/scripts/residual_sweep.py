# -*- coding: utf-8 -*-
"""잔존 문구 스윕 — 리뷰에서 지적된 표현이 모든 생성 문서(핵심 원고·저널 셸·부록·표·캡션 코드)에 남아 있는지 센다.
사용: python3 residual_sweep.py --files f1 f2 ... --patterns "p1" "p2" ...   (grep -c 와 동일 의미, 대소문자 구분)
exit 1 = 잔존 있음. 정당한 잔존(같은 표현의 다른 의미)은 결과를 읽고 판단한다 — 자동 통과시키지 않는다.
"""
import argparse, re, sys
ap = argparse.ArgumentParser(); ap.add_argument("--files", nargs="+", required=True); ap.add_argument("--patterns", nargs="+", required=True)
a = ap.parse_args(); total = 0
for p in a.patterns:
    n = 0; where = []
    for f in a.files:
        try: c = sum(1 for ln in open(f, encoding="utf-8") if p in ln)
        except FileNotFoundError: continue
        if c: where.append(f"{f.split('/')[-1]}:{c}")
        n += c
    total += n; print(f"  {p[:46]:<48} {n}  {' '.join(where)}")
print(f"\n잔존 합계 {total}"); sys.exit(1 if total else 0)
