---
paths:
  - "shared/data/**"
  - "papers/**/05_data/**"
---
# Data governance

- `shared/data/raw/` is immutable. Add new versioned files; never overwrite.
- Record origin, retrieval date, license/access limits, hash, schema, and transformations.
- Reusable transformations belong in `shared/code`; paper-only transformations belong in the paper.
- Every merge reports keys, cardinality, unmatched rates, duplicates, and temporal alignment.
- Never commit restricted data or secrets. Commit metadata and reproducible acquisition instructions instead.
