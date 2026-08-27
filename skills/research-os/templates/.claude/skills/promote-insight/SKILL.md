---
name: promote-insight
description: Promote a durable, reusable research insight or decision from a paper/session into the typed Obsidian Wiki without duplicating existing knowledge.
argument-hint: "<insight, decision, or source>"
context: fork
agent: wiki-curator
allowed-tools: Read, Grep, Glob, Bash, Write, Edit
---

# Promote an insight

1. Search Wiki and registries for an existing canonical note.
2. Classify the item as source, concept, theory, method, dataset, construct, paper, contradiction, decision, or synthesis.
3. Promote only knowledge with durable value beyond the immediate turn.
4. Include stable ID, status, evidence level, provenance, supporting and contradicting links, papers affected, and date.
5. Keep the source statement separate from interpretation and implications.
6. Update existing notes when possible; create a new note only for a distinct entity or proposition.
7. Update index/log and run the linter.
