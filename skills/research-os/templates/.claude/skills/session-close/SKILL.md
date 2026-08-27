---
name: session-close
description: Consolidate a completed turn into durable paper and portfolio records so the next session resumes without reconstruction.
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# Close a research session

For material work only:

1. Summarize what was attempted, evidence examined, files changed, decisions made, failed paths, and unresolved uncertainty.
2. Update the active paper's `00_admin/CURRENT_STATE.md`, append `DECISION_LOG.md` when a decision changed, append `SESSION_LOG.md`, and set one exact next action in `ROADMAP.md`.
3. Update `project-control/SESSION_HANDOFF.md`; update portfolio registries only when their state changed.
4. Promote reusable knowledge to the Wiki through `/promote-insight`; do not dump transient conversation text.
5. Run `python scripts/validate_project.py --quick` and `python scripts/wiki_lint.py`.
6. Report validation failures explicitly. Do not claim completion while the durable state is stale.
