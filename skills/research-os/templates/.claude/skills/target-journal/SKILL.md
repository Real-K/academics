---
name: target-journal
description: Select and rank SSCI finance journal targets using current scope, recent conversations, contribution type, methodological bar, and desk-rejection risks.
argument-hint: "[paper_id]"
context: fork
agent: journal-editor
allowed-tools: Read, Grep, Glob, Write, Edit
---

# Target journal

1. Verify current journal scope, status, article types, policies, and recent relevant articles.
2. Compare paper contribution, method, audience, length, and framing with recent publications—not only stated scope.
3. Build stretch/core/safety candidates with explicit fit evidence.
4. For each target list likely desk-rejection trigger, required reframing or evidence, and submission cost.
5. Check exclusivity, data/code disclosure, AI-use, preprint, and formatting policies before submission.
6. Write `10_submission/TARGET_JOURNALS.md` and a stop rule for sequential targeting.

Never guarantee acceptance or treat impact metrics as quality proof.
