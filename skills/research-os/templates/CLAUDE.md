# Finance SSCI Research OS

## Mission
Build publishable empirical finance papers in English. Optimize for theoretical contribution, defensible measurement, credible identification, reproducible analysis, and precise journal-quality writing. Never optimize for a significant coefficient at the expense of research integrity.

## Start every session
1. Read `project-control/ACTIVE_PAPER`.
2. Read `project-control/SESSION_HANDOFF.md` and `project-control/PORTFOLIO_STATE.md`.
3. If an active paper exists, read its `00_admin/CURRENT_STATE.md`, `00_admin/DECISION_LOG.md`, `00_admin/ROADMAP.md`, and `00_admin/RISK_REGISTER.md`.
4. State the current stage, unresolved blockers, and a verifiable plan before substantial work.
5. Do not repeat completed work unless a new contradiction, data revision, or explicit re-evaluation requires it.

## Non-negotiable research rules
- Separate facts, estimates, interpretations, hypotheses, and conjectures.
- Never invent citations, data, variable definitions, estimates, institutional details, or robustness results.
- Trace every empirical claim to code, output, table/figure, dataset version, and specification ID.
- Trace every literature claim to a verified source and locator.
- Preserve null, adverse, and contradictory findings. Do not hide specification instability.
- Treat mechanism validity and measurement validity as independent gates from statistical identification.
- Use causal language only when the design and diagnostics justify it.
- Maintain an explicit hypothesis budget. Post-hoc hypotheses are labeled exploratory.
- Never edit `shared/data/raw/`; create versioned derived data instead.
- Never overwrite frozen main results. Create a new run or formally unfreeze with a logged decision.

## Research workflow
Proceed through gates, not by prose completion:
1. Research question and contribution gate.
2. Theory, mechanism, and hypothesis gate.
3. Measurement and data feasibility gate.
4. Estimand and identification gate.
5. Pre-analysis freeze.
6. Main analysis and diagnostics.
7. Robustness, falsification, and sensitivity.
8. Interpretation and claim-language audit.
9. Manuscript drafting in English (finance presentation norms — rule 10; gates and freezes remain internal discipline, not manuscript content).
10. Independent internal review and submission preparation.

A gate may fail. Record the failure and redesign or kill the paper. Do not force continuation.

## Multiple papers
- Each paper lives in `papers/P###_<slug>/` and has its own state, decisions, code, outputs, manuscript, and review history.
- Common data and reusable code live only under `shared/`.
- Cross-paper discoveries go to `Wiki/` and the relevant registry; paper-specific claims stay in the paper folder.
- Do not silently transfer a construct, sample rule, or result across papers. Record provenance and compatibility.

## Agent use
Delegate focused tasks to project subagents in `.claude/agents/`. Give each agent a bounded question, allowed evidence, required artifact, and stopping condition. Use independent reviewers for identification, measurement, robustness, and writing. The research director synthesizes; specialist agents do not silently rewrite the research question.

## Writing standard
- **Finance presentation norm (PI directive 2026-08-15, see `.claude/rules/10-finance-manuscript-norms.md`):** manuscripts present the final specification with its economic/econometric justification, in the field's standard logical structure — not the research chronology. Preregistration vocabulary and confession-style design narratives do not appear in manuscripts; the full design history stays in the internal record and replication package. All findings (including unfavorable ones) are still reported, as robustness or appendix analyses.
- Manuscripts are written in English unless the user explicitly requests otherwise.
- Use finance-journal prose: argument-driven, economical, specific, and evidence-calibrated.
- Each paragraph must have one function. Lead with the claim, then mechanism/evidence, then implication.
- Avoid generic novelty claims, inflated adjectives, unexplained jargon, and results-first theory.
- Tables and figures must be self-contained and reproducible.

## Karpathy-inspired execution discipline
- Surface assumptions and trade-offs before implementation.
- Prefer the smallest design or code change that answers the research question.
- Touch only files required by the task; do not refactor adjacent work without a reason.
- Define success criteria and verify them with tests, diagnostics, or auditable artifacts.

## End every substantive session
Update the active paper's `CURRENT_STATE.md`, append `SESSION_LOG.md`, record material decisions in `DECISION_LOG.md`, update `project-control/SESSION_HANDOFF.md`, and promote durable knowledge to `Wiki/`. Run `python scripts/validate_project.py --quick` before declaring completion.

## This project
<!-- academic-research-os init 가 채우는 자리. 논문 slug, 데이터 범위, 정본 표본 파일 경로 + sha256_16, 현재 단계, 다음 행동. -->

