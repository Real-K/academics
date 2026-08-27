# academics — Claude Code plugin for empirical finance papers

Nine skills distilled from taking two empirical-finance papers (private-equity and employment; third-party placements and employment) from idea battery to SSCI submission. Skills load as `academics:<name>`.

| skill | what it does |
|---|---|
| `academics:research-os` | install the research operating system into a new project: CLAUDE.md contract, 12 rules (integrity, evidence, finance presentation norms, equivalence gates…), 5 hooks, 13 referee agents, 22 project skills, ledgers |
| `academics:idea-harness` | generate N idea cards (identification, mechanism, moderator/mediator, kill criteria) → numbered elimination harness |
| `academics:power-rescue` | 23 design levers to rule out false negatives when a result weakens — with guardrails against significance search |
| `academics:manuscript-verify` | numbers / claim-anchors / cross-references+captions / ledger lint, plus a negative-control protocol |
| `academics:comment-dispose` | dispose every reviewer comment: verify the reviewer's facts, classify, propagate, sweep, verify, log |
| `academics:narrative-audit` | three-sentence core, so-what test, claim-calibration vocabulary, main/appendix split |
| `academics:journal-package` | metrics/lineage/Guide-for-Authors, per-journal shells, docx/title page/highlights, anonymity |
| `academics:replication-repo` | stored-output notebooks cut verbatim from build scripts, identifier scan, manifest, push, resync |
| `academics:entity-linkage` | Korean firm identifier linkage ladder and PI adjudication package format |

## Install

**This machine (skills-dir auto-load):**
```bash
git clone https://github.com/Real-K/academics ~/.claude/skills/academics   # loads next session as academics@skills-dir
```
**Via marketplace:**
```bash
claude plugin marketplace add Real-K/academics
claude plugin install academics@academics
```
Update: `git pull` in the clone, or `claude plugin update academics`.

## Requirements
Python 3.11+, numpy, matplotlib (figures/notebooks), python-docx (submission package), gh CLI (replication repo). Credentials live only in `~/.claude/.env`; none are shipped here.

## Note
`skills/research-os/templates/` is a copy of the originating project's `.claude/`; refresh it when the source changes.
