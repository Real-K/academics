from __future__ import annotations
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def read_input() -> dict[str, Any]:
    try:
        text = sys.stdin.read()
        return json.loads(text) if text.strip() else {}
    except Exception:
        return {}


def root_from(data: dict[str, Any]) -> Path:
    root = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
    return Path(root).resolve()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def active_paper(root: Path) -> str:
    path = root / "project-control" / "ACTIVE_PAPER"
    if not path.exists():
        return "NONE"
    value = path.read_text(encoding="utf-8").strip()
    return value or "NONE"


def paper_path(root: Path, paper_id: str) -> Path | None:
    if paper_id == "NONE":
        return None
    matches = sorted((root / "papers").glob(f"{paper_id}_*"))
    return matches[0] if len(matches) == 1 else None


def emit(obj: dict[str, Any]) -> None:
    sys.stdout.write(json.dumps(obj, ensure_ascii=False))


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def safe_rel(path: Path, root: Path) -> str:
    try:
        return path.resolve().relative_to(root.resolve()).as_posix()
    except Exception:
        return str(path)
