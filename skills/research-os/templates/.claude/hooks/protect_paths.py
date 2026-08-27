from __future__ import annotations
import re
from pathlib import Path
from common import read_input, root_from, active_paper, paper_path, emit, safe_rel

PROTECTED_AFTER_FREEZE = {
    "01_question/ESTIMAND_CARD.md",
    "03_theory/HYPOTHESIS_REGISTRY.csv",
    "04_design/IDENTIFICATION_STRATEGY.md",
    "04_design/MEASUREMENT_VALIDITY.md",
    "04_design/PRE_ANALYSIS_PLAN.md",
    "04_design/SPECIFICATION_GRID.yaml",
    "04_design/POWER_AND_PRECISION.md",
    "05_data/data_manifest.yaml",
    "05_data/CONSTRUCT_DICTIONARY.csv",
}
WRITE_TOOLS = {"Write", "Edit", "MultiEdit", "NotebookEdit"}
MUTATING_BASH = re.compile(
    r"(?:^|[;&|]\s*|\s)(?:rm|mv|cp|install|truncate|touch|sed\s+-i|perl\s+-pi|python\b|Rscript\b|tee\b|cat\s+[^|]*>)"
)


def deny(reason: str) -> None:
    emit({"hookSpecificOutput": {
        "hookEventName": "PreToolUse",
        "permissionDecision": "deny",
        "permissionDecisionReason": reason,
    }})


def normalize_target(value: str, root: Path) -> Path:
    path = Path(value)
    return (path if path.is_absolute() else root / path).resolve()


def extract_write_paths(tool: str, tool_input: dict, root: Path) -> list[Path]:
    if tool not in WRITE_TOOLS:
        return []
    keys = ["file_path", "path", "notebook_path"]
    values = [tool_input.get(key) for key in keys if tool_input.get(key)]
    edits = tool_input.get("edits", [])
    if isinstance(edits, list):
        for item in edits:
            if isinstance(item, dict) and item.get("file_path"):
                values.append(item["file_path"])
    return [normalize_target(str(value), root) for value in values]


def command_mentions(command: str, token: str) -> bool:
    return token in command.replace("\\", "/")


def main() -> None:
    data = read_input()
    root = root_from(data)
    tool = data.get("tool_name", "")
    tool_input = data.get("tool_input") or {}
    targets = extract_write_paths(tool, tool_input, root)

    for target in targets:
        rel = safe_rel(target, root)
        if rel == "shared/data/raw" or rel.startswith("shared/data/raw/"):
            deny(f"Raw data are immutable. Add a new versioned source file through an explicit ingestion step instead of editing {rel}.")
            return
        if "/07_analysis/frozen_main/" in f"/{rel}/" and target.name != "README.md":
            deny(f"Frozen main-analysis artifacts are append-only. Create a new registered run instead of modifying {rel}.")
            return

    paper_id = active_paper(root)
    pdir = paper_path(root, paper_id)
    frozen = bool(pdir and (pdir / "04_design" / "PRE_ANALYSIS_FROZEN.lock").exists())
    if frozen and pdir:
        for target in targets:
            try:
                relpaper = target.resolve().relative_to(pdir.resolve()).as_posix()
            except Exception:
                continue
            if relpaper in PROTECTED_AFTER_FREEZE:
                deny(
                    f"{relpaper} is protected by the pre-analysis freeze. "
                    f"Run scripts/unfreeze_paper.py --paper {paper_id} --reason \"...\" first; the deviation will be logged."
                )
                return

    if tool != "Bash":
        return
    command = str(tool_input.get("command", ""))
    if not MUTATING_BASH.search(command):
        return
    if command_mentions(command, "shared/data/raw"):
        deny("Bash command appears to mutate shared/data/raw. Raw data are immutable.")
        return
    if command_mentions(command, "07_analysis/frozen_main"):
        deny("Bash command appears to mutate frozen main-analysis artifacts. Create a new run instead.")
        return
    if frozen and pdir:
        for relpaper in PROTECTED_AFTER_FREEZE:
            if command_mentions(command, relpaper):
                deny(
                    f"Bash command appears to mutate frozen design file {relpaper}. "
                    f"Use scripts/unfreeze_paper.py with a reason before changing the plan."
                )
                return


if __name__ == "__main__":
    main()
