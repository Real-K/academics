from __future__ import annotations
import json
from common import read_input, root_from, utc_now, active_paper, append_jsonl


def main() -> None:
    data = read_input()
    root = root_from(data)
    record = {
        "ended_at": utc_now(),
        "session_id": data.get("session_id", "unknown"),
        "reason": data.get("reason", "unknown"),
        "active_paper": active_paper(root),
        "cwd": data.get("cwd", str(root)),
    }
    append_jsonl(root / "logs" / "sessions" / "session_events.jsonl", record)


if __name__ == "__main__":
    main()
