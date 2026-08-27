---
name: archive-paper
description: Archive a killed, superseded, rejected, or completed paper while preserving reusable assets, reasons, and cross-paper lessons.
argument-hint: "<paper_id> --reason "...""
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# Archive a paper

1. Confirm paper ID and archive reason: completed, killed, superseded, withdrawn, or indefinitely paused.
2. Write a terminal decision in `DECISION_LOG.md` with evidence and conditions for reopening.
3. Update `CURRENT_STATE.md`, paper registry, portfolio state, and active-paper pointer.
4. Preserve all data provenance, code, frozen runs, null results, and review records.
5. Promote reusable constructs, datasets, methods, contradictions, and lessons to the shared registries/Wiki.
6. Move only disposable scratch files; never erase the evidentiary trail.
7. Run full validation.
