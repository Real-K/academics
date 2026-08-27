from __future__ import annotations
import json
from pathlib import Path
from common import read_input, root_from, active_paper, paper_path, emit

MATERIAL_DIRS = {"01_question", "02_literature", "03_theory", "04_design", "05_data", "06_code", "07_analysis", "08_manuscript", "09_review", "10_submission"}


def newest_mtime(paths: list[Path]) -> float:
    newest = 0.0
    for base in paths:
        if not base.exists():
            continue
        for p in base.rglob("*"):
            try:
                if p.is_file():
                    newest = max(newest, p.stat().st_mtime)
            except OSError:
                pass
    return newest


def main() -> None:
    data = read_input()
    if data.get("stop_hook_active"):
        return
    root = root_from(data)
    paper_id = active_paper(root)
    pdir = paper_path(root, paper_id)
    if not pdir:
        return
    material = [pdir / d for d in MATERIAL_DIRS]
    material_time = newest_mtime(material)
    current = pdir / "00_admin" / "CURRENT_STATE.md"
    session_log = pdir / "00_admin" / "SESSION_LOG.md"
    handoff = root / "project-control" / "SESSION_HANDOFF.md"
    record_time = min(
        current.stat().st_mtime if current.exists() else 0,
        session_log.stat().st_mtime if session_log.exists() else 0,
        handoff.stat().st_mtime if handoff.exists() else 0,
    )
    if material_time > record_time + 1:
        emit({
            "decision": "block",
            "reason": (
                f"Material research artifacts changed for {paper_id}, but CURRENT_STATE.md, SESSION_LOG.md, "
                "and project-control/SESSION_HANDOFF.md are not all current. Consolidate the durable record, "
                "state the exact next action, and run quick validation before ending the turn."
            )
        })


if __name__ == "__main__":
    main()
