---
name: run-analysis
description: Execute the versioned empirical pipeline only after design freeze, separate exploratory from confirmatory work, and register immutable runs.
argument-hint: "<paper_id> [--type main|exploratory|robustness|mechanism]"
disable-model-invocation: true
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# Run analysis

1. Confirm the pre-analysis lock and clean validation status.
2. Create a run with `python scripts/create_run.py --paper $ARGUMENTS --type main` (or `exploratory`, `robustness`, `mechanism`).
3. Execute numbered scripts from setup through tables/figures. Never edit generated output manually.
4. Capture code commit, input hashes, environment, package versions, seed, command, row counts, and output hashes.
5. Compare execution to the specification grid and log deviations before interpretation.
6. Lock a completed main run. New work goes to a new run; never replace a frozen result.
7. Update run registry and current state.

Report failures and unexpected nulls directly. Do not shop among run folders for a preferred result.
