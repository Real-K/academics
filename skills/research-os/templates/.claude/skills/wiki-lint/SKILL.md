---
name: wiki-lint
description: Validate Wiki metadata, IDs, links, indexes, and orphan status after knowledge-base changes.
argument-hint: "[--strict]"
disable-model-invocation: true
allowed-tools: Bash, Read, Grep, Glob, Write, Edit
---

# Wiki lint

Run:

```bash
python scripts/wiki_lint.py $ARGUMENTS
```

Fix duplicate IDs, broken internal links, missing required frontmatter, stale indexes, and canonical notes without provenance. Orphan notes may be intentional only when marked `status: inbox` or `status: archived`. Do not make up links merely to satisfy the linter.
