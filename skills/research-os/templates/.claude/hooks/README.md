# Claude Code hooks

These hooks provide lightweight enforcement and context loading:

- `session_start.py`: injects active-paper state and creates session metadata.
- `prompt_context.py`: reminds Claude which research unit and next action are active.
- `protect_paths.py`: blocks raw-data mutation, frozen-design edits, and frozen-main overwrites.
- `stop_guard.py`: prevents a material turn from ending with stale continuity records.
- `session_end.py`: appends a machine-readable session event.

Hooks are deterministic safeguards, not substitutes for methodological judgment. Verify installation with `/hooks` in Claude Code. Use `.claude/settings.local.json` for machine-specific permissions.
