---
name: session-start
description: Load the durable research state, active paper, open decisions, and next action before beginning work. Use at the start of a research session or after compaction.
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Bash
---

# Start a research session

1. Read `project-control/ACTIVE_PAPER`, `PORTFOLIO_STATE.md`, and `SESSION_HANDOFF.md`.
2. When a paper is active, read its `00_admin/CURRENT_STATE.md`, `ROADMAP.md`, `DECISION_LOG.md`, `RISK_REGISTER.md`, and latest session entry.
3. Inspect `git status` and report any uncommitted research artifacts that could change the working state.
4. State in no more than eight lines:
   - active paper and stage;
   - last verified result or decision;
   - unresolved blocker;
   - exact next deliverable;
   - completion test;
   - files expected to change.
5. Do not redo completed work unless a logged reason reopens it.
