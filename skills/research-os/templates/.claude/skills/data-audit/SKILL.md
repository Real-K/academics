---
name: data-audit
description: Audit data provenance, schema, keys, coverage, missingness, merges, event timing, and sample feasibility before building the analytic panel.
context: fork
agent: data-architect
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# Data audit

1. Inventory inputs in `05_data/data_manifest.yaml` and the shared dataset registry.
2. For each source record provenance, version/hash, coverage, access restrictions, unit, frequency, key, and known revisions.
3. Profile duplicates, missingness, impossible values, temporal gaps, and distribution shifts.
4. Audit entity resolution and every merge for cardinality and unmatched observations.
5. Check event dating, reporting lags, left/right censoring, look-ahead leakage, and endogenous record appearance.
6. Build `SAMPLE_FLOW.md` from source population to final candidate sample.
7. Update construct dictionary and provenance artifacts.
8. End with PASS, REPAIR, PIVOT, or KILL and identify the smallest decisive data test.

Do not alter raw data or define undocumented variables by guesswork.
