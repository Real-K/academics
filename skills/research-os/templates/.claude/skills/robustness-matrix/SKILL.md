---
name: robustness-matrix
description: Derive a prioritized robustness and falsification matrix from explicit threats rather than generating decorative alternative specifications.
context: fork
agent: robustness-red-team
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# Robustness matrix

Read the threat, measurement, and identification memos plus the frozen main result. For each material threat create a row with:
- threat ID and logic;
- test and expected pattern under the threat versus focal mechanism;
- required data and estimator;
- decision rule;
- pre-specified/exploratory status;
- result and interpretation;
- effect on claim ceiling.

Prioritize decisive tests: negative controls, placebo timing/outcomes/exposures, alternative measures, bounds/sensitivity, influential observations, sample composition, clustering/randomization inference, multiple testing, and external validation. Reject tests that are not logically connected to a threat. Preserve all failures and nulls in `07_analysis/negative_results` and the matrix.
