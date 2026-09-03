# -*- coding: utf-8 -*-
"""프로젝트 공용 헬퍼 — validate_project.py, new_paper.py 등이 임포트한다.
인터페이스: ROOT, paper_dirs, paper_id_from_dir, read_csv, active_paper_id.
paper_id 규약 = papers/ 아래 폴더 전체 이름 (예: P001_gender_screening).
"""
from __future__ import annotations

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def paper_dirs():
    """papers/ 아래 논문 폴더 목록 (숨김·비폴더 제외)."""
    base = ROOT / "papers"
    if not base.exists():
        return []
    return sorted(p for p in base.iterdir() if p.is_dir() and not p.name.startswith((".", "_")))


def paper_id_from_dir(p: Path) -> str:
    return Path(p).name


def read_csv(path):
    """(fields, rows) — rows 는 dict 리스트. 파일이 없으면 ([], [])."""
    path = Path(path)
    if not path.exists():
        return [], []
    with open(path, encoding="utf-8-sig", newline="") as fh:
        r = csv.DictReader(fh)
        return list(r.fieldnames or []), list(r)


def active_paper_id() -> str:
    f = ROOT / "project-control" / "ACTIVE_PAPER"
    if not f.exists():
        return "NONE"
    v = f.read_text(encoding="utf-8").strip()
    return v or "NONE"
