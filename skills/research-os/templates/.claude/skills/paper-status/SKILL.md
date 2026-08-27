---
name: paper-status
description: Summarize the portfolio or active paper from registries and durable state, including gates, blockers, and next action.
argument-hint: "[paper_id|--all]"
disable-model-invocation: true
allowed-tools: Bash, Read, Grep, Glob
---

# Paper status

Run `python scripts/research_status.py $ARGUMENTS` and verify the output against the relevant `CURRENT_STATE.md`.

For an individual paper, report:
- stage and gate status;
- contribution in one sentence;
- current design and claim level;
- latest verified result;
- top three risks;
- next action and completion test;
- stale or contradictory records.

Do not infer progress from manuscript length or number of files.
