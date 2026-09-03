# -*- coding: utf-8 -*-
"""create-paper 스킬이 호출하는 논문 워크스페이스 생성기.
validate_project.py 의 PAPER_REQUIRED 규격과 1:1 로 골격을 만든다.

사용: python scripts/new_paper.py --title "Working Title" [--slug slug] [--activate]
"""
from __future__ import annotations
import argparse
import csv
import datetime
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from _common import ROOT, paper_dirs, paper_id_from_dir  # noqa: E402

PAPER_REQUIRED = [
    "CLAUDE.md", "00_admin/CURRENT_STATE.md", "00_admin/DECISION_LOG.md", "00_admin/SESSION_LOG.md",
    "01_question/RESEARCH_QUESTION.md", "01_question/ESTIMAND_CARD.md",
    "03_theory/HYPOTHESIS_REGISTRY.csv", "04_design/PRE_ANALYSIS_PLAN.md",
    "04_design/SPECIFICATION_GRID.yaml", "05_data/data_manifest.yaml", "06_code/README.md",
    "07_analysis/run_log.csv", "08_manuscript/manuscript.md", "08_manuscript/CLAIMS_LEDGER.csv",
    "09_review/REVIEW_MATRIX.csv", "10_submission/SUBMISSION_CHECKLIST.md",
]
EXTRA = ["00_admin/PAPER_CHARTER.md", "00_admin/KILL_CRITERIA.md", "00_admin/HYPOTHESIS_BUDGET.md",
         "00_admin/ROADMAP.md", "00_admin/RISK_REGISTER.md", "00_admin/RESULTS_LEDGER.md",
         "02_literature/README.md"]
CSV_HEADERS = {
    "03_theory/HYPOTHESIS_REGISTRY.csv": "hyp_id,statement,type,status,evidence,registered_at\n",
    "07_analysis/run_log.csv": "run_id,date,script,sha256_16,inputs,outputs,verdict,notes\n",
    "09_review/REVIEW_MATRIX.csv": "reviewer,dimension,finding,severity,disposition,date\n",
}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--title", required=True)
    ap.add_argument("--slug")
    ap.add_argument("--activate", action="store_true")
    a = ap.parse_args()
    slug = a.slug or re.sub(r"[^a-z0-9]+", "_", a.title.lower()).strip("_")[:40]
    existing = [paper_id_from_dir(p) for p in paper_dirs()]
    nums = [int(m.group(1)) for pid in existing if (m := re.match(r"P(\d+)", pid or ""))]
    pid = f"P{(max(nums) + 1 if nums else 1):03d}"
    pdir = ROOT / "papers" / f"{pid}_{slug}"
    if pdir.exists():
        sys.exit(f"exists: {pdir}")
    today = datetime.date.today().isoformat()
    for rel in PAPER_REQUIRED + EXTRA:
        f = pdir / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        if rel in CSV_HEADERS:
            f.write_text(CSV_HEADERS[rel], encoding="utf-8")
        elif rel == "08_manuscript/CLAIMS_LEDGER.csv":
            src = ROOT / "paper_skeleton/CLAIMS_LEDGER.csv"
            if src.exists():
                shutil.copy(src, f)
            else:
                f.write_text("claim_id,exhibit,claim,value,ci95,n,source_json,json_path,code,"
                             "sha256_16,path_status\n", encoding="utf-8")
        elif rel == "CLAUDE.md":
            f.write_text(f"# {pid} — {a.title}\n\n(내용은 생성 후 채운다)\n", encoding="utf-8")
        else:
            f.write_text(f"# {rel.split('/')[-1].rsplit('.', 1)[0]} — {pid}\n\n[EVIDENCE REQUIRED]\n",
                         encoding="utf-8")
    # paper_id 규약 = 폴더 전체 이름 (_common.paper_id_from_dir 참조)
    folder_id = pdir.name
    reg = ROOT / "shared/registries/paper_registry.csv"
    with open(reg, "a", encoding="utf-8", newline="") as fh:
        csv.writer(fh).writerow([folder_id, slug, a.title, "active", "question_gate",
                                 str(a.activate), today, today, "finance", "TBD", "PI"])
    if a.activate:
        (ROOT / "project-control/ACTIVE_PAPER").write_text(folder_id + "\n", encoding="utf-8")
    print(f"created {pdir.relative_to(ROOT)} (paper_id={folder_id}, active={a.activate})")


if __name__ == "__main__":
    main()
