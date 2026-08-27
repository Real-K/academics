---
paths:
  - "scripts/**"
  - "shared/code/**"
  - "papers/**/06_code/**"
---
# Reproducible code

- Use numbered, idempotent scripts with explicit inputs and outputs.
- No manual edits to generated tables, figures, or analytic datasets.
- Set seeds where randomness exists and record environment/package versions.
- Fail loudly on schema violations, duplicate keys, unexpected row loss, and missing required columns.
- Keep functions simple and test transformations that affect reported results.
