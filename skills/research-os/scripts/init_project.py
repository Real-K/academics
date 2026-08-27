# -*- coding: utf-8 -*-
"""academic-research-os — 새 프로젝트에 연구 OS 를 설치한다.
사용:  python3 init_project.py <target-dir> [--paper <slug>] [--force]
동작:  templates/ 를 target 에 복사. 기존 파일은 보존(--force 시 덮어씀). --paper 시 papers/<slug>/ 골격 + ACTIVE_PAPER.
"""
import os, sys, shutil, argparse
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(os.path.dirname(HERE), "templates")
ap = argparse.ArgumentParser(); ap.add_argument("target"); ap.add_argument("--paper"); ap.add_argument("--force", action="store_true")
a = ap.parse_args(); tgt = os.path.abspath(a.target); os.makedirs(tgt, exist_ok=True)
copied = skipped = 0
for dp, _, fs in os.walk(T):
    for f in fs:
        src = os.path.join(dp, f); rel = os.path.relpath(src, T); dst = os.path.join(tgt, rel)
        if rel.startswith("paper_skeleton"): continue
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if os.path.exists(dst) and not a.force: skipped += 1; continue
        shutil.copy(src, dst); copied += 1
if a.paper:
    pdir = os.path.join(tgt, "papers", a.paper)
    for sub in ["00_admin", "03_identification", "06_code", "08_manuscript", "09_review", "10_submission", "11_replication"]:
        os.makedirs(os.path.join(pdir, sub), exist_ok=True)
    for f in ["CLAIMS_LEDGER.csv", "RESULTS_LEDGER.md"]:
        d = os.path.join(pdir, "08_manuscript", f)
        if not os.path.exists(d): shutil.copy(os.path.join(T, "paper_skeleton", f), d)
    for f, txt in [("CURRENT_STATE.md", f"# {a.paper} — current state\n\n- stage:\n- blocker:\n- next action:\n"),
                   ("SESSION_LOG.md", f"# {a.paper} — session log\n"), ("DECISION_LOG.md", f"# {a.paper} — decision log\n"),
                   ("ROADMAP.md", f"# {a.paper} — roadmap\n"), ("RISK_REGISTER.md", f"# {a.paper} — risk register\n")]:
        d = os.path.join(pdir, "00_admin", f)
        if not os.path.exists(d): open(d, "w", encoding="utf-8").write(txt)
    open(os.path.join(tgt, "project-control", "ACTIVE_PAPER"), "w").write(a.paper + "\n")
print(f"installed → {tgt}: copied {copied}, kept existing {skipped}" + (f", paper {a.paper}" if a.paper else ""))
print("next: 1) CLAUDE.md '## This project' 채우기  2) .claude/settings.json 훅 확인  3) python3 scripts/validate_project.py --quick")
