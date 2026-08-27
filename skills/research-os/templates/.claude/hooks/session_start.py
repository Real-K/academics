from __future__ import annotations
import json
from pathlib import Path
from common import read_input, root_from, utc_now, active_paper, paper_path, emit


def first_value(text: str, label: str) -> str:
    for line in text.splitlines():
        if line.strip().startswith(label):
            return line.split(":", 1)[-1].strip().strip("*")
    return "unknown"


def main() -> None:
    data = read_input()
    root = root_from(data)
    paper_id = active_paper(root)
    pdir = paper_path(root, paper_id)
    state = "No active paper. Use /create-paper or scripts/set_active_paper.py."
    if pdir:
        state_file = pdir / "00_admin" / "CURRENT_STATE.md"
        state_text = state_file.read_text(encoding="utf-8") if state_file.exists() else ""
        stage = first_value(state_text, "- **Stage")
        blocker = first_value(state_text, "- **Active blocker")
        next_action = first_value(state_text, "- **Exact next action")
        state = f"Active paper: {paper_id}. Stage: {stage}. Blocker: {blocker}. Next action: {next_action}."

    handoff = root / "project-control" / "SESSION_HANDOFF.md"
    handoff_mtime = handoff.stat().st_mtime if handoff.exists() else 0
    session_state = {
        "session_id": data.get("session_id", "unknown"),
        "source": data.get("source", "unknown"),
        "started_at": utc_now(),
        "active_paper": paper_id,
        "handoff_mtime_at_start": handoff_mtime,
    }
    state_path = root / ".claude" / ".session_state.json"
    state_path.write_text(json.dumps(session_state, indent=2), encoding="utf-8")

    context = (
        "Research repository state: " + state + " "
        "Durable records, not conversation recall, define completed work. "
        "Read project-control/SESSION_HANDOFF.md and the active paper state before changing research artifacts."
    )
    emit({
        "hookSpecificOutput": {
            "hookEventName": "SessionStart",
            "additionalContext": context,
            "sessionTitle": f"Finance SSCI | {paper_id}",
        }
    })


if __name__ == "__main__":
    main()
