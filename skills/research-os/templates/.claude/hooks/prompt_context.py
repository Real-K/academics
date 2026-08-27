from __future__ import annotations
from common import read_input, root_from, active_paper, paper_path, emit


def main() -> None:
    data = read_input()
    root = root_from(data)
    paper_id = active_paper(root)
    if paper_id == "NONE":
        return
    pdir = paper_path(root, paper_id)
    if not pdir:
        return
    state = pdir / "00_admin" / "CURRENT_STATE.md"
    next_action = ""
    if state.exists():
        for line in state.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("- **Exact next action"):
                next_action = line.split(":", 1)[-1].strip().strip("*")
                break
    msg = f"Active research unit is {paper_id}."
    if next_action:
        msg += f" Recorded next action: {next_action}."
    msg += " Check durable state before reopening completed work; update records after material progress."
    emit({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": msg}})


if __name__ == "__main__":
    main()
