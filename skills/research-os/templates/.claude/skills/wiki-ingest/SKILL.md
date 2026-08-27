---
name: wiki-ingest
description: Ingest a raw source or research artifact into the Obsidian Wiki while preserving immutable source files and provenance.
argument-hint: "<path-to-source>"
disable-model-invocation: true
allowed-tools: Bash, Read, Grep, Glob, Write, Edit
---

# Wiki ingest

Run:

```bash
python scripts/wiki_ingest.py --source "$ARGUMENTS"
```

Then review the generated intake note. Assign a stable ID and type, distinguish direct evidence from interpretation, add source locators, link existing concepts/methods/papers, and record contradictions rather than resolving them prematurely. Search for an existing note before promotion. Update `Wiki/index.md`, `Wiki/log.md`, and source registry. Run the Wiki linter.
