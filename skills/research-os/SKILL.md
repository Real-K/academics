---
name: research-os
description: 실증 재무(SSCI) 논문 프로젝트를 위한 연구 운영체제 설치·점검. 새 프로젝트에 CLAUDE.md 연구계약, 규칙 12종(무결성·근거·데이터·계량·이론·영문원고·위키·재현·다중논문·연속성·finance 제시 규범·등가성 게이트), 훅 5종(세션 시작/종료·stop guard·prompt context·경로 보호), 에이전트 13종, 프로젝트 스킬 22종, project-control 골격, 원장 스키마를 설치한다. "새 논문 프로젝트 시작", "연구 하네스 세팅", "research OS 설치", "다른 프로젝트에도 같은 규칙 적용" 요청 시.
argument-hint: "init <target-dir> [--paper <slug>] | check <project-dir>"
---

# academics:research-os — 실증 재무 논문 연구 OS

P-014(PE와 고용)·P-016(제3자배정과 고용) 두 논문을 SSCI 투고까지 끌고 간 하네스를 다른 프로젝트에 그대로 이식한다.
"진행해" 두 글자로 세션이 이어지고, 결과가 원고까지 추적되고, 불리한 결과가 사라지지 않게 하는 **구조**가 이 스킬의 내용이다.

## 언제 쓰나
- 새 논문/새 프로젝트 폴더를 시작할 때 (`init`)
- 기존 프로젝트에 규칙·훅·에이전트가 빠졌는지 점검할 때 (`check`)

## init 절차
1. `python3 ${CLAUDE_PLUGIN_ROOT}/skills/research-os/scripts/init_project.py <target-dir> [--paper <slug>]` — 기존 파일은 덮어쓰지 않는다(`--force` 시 덮어씀).
2. `CLAUDE.md` 의 `## This project` 를 채운다: 논문 slug, 데이터 범위, **정본 표본 파일 경로 + sha256_16**, 현재 단계, 다음 행동. 정본을 명시하는 이유: P-014 에서 처치표본이 283→379 로 확장된 뒤 옛 수치가 산출물 곳곳에 남아 혼선을 일으켰다.
3. `.claude/settings.json` 의 훅 5종이 `${CLAUDE_PROJECT_DIR}` 기준으로 걸렸는지 확인.
4. `python3 scripts/validate_project.py --quick` → `0 errors`.
5. 첫 세션: `/session-start` → `project-control/ACTIVE_PAPER` 지정 → `/create-paper`.

## check 절차
`diff -rq ${CLAUDE_PLUGIN_ROOT}/skills/research-os/templates/.claude <project>/.claude` 로 누락을 보고한다. 규칙 10·11 이 없는 프로젝트는 finance 제시 규범과 등가성 게이트가 없다는 뜻 — 우선 설치.

## 설치되는 것과 그 존재 이유

| 구성 | 내용 | 왜 있어야 하나 (실제 사례) |
|---|---|---|
| `CLAUDE.md` | 세션 시작/종료 의무, 게이트 워크플로, 작성 규범 | 컨텍스트가 여러 번 clear 되어도 `SESSION_HANDOFF` 만 읽으면 재개된다 |
| `rules/00,01` | 무결성·근거 | 날조 금지, 청구→산출물 추적 |
| `rules/09` | 연속성·게이트 | 동결 결과 append-only; 완료 작업 재실행 금지 |
| `rules/10` | **finance 제시 규범** | preregistration 어휘("preregistered", "frozen", "pre-specified")를 원고에 쓰지 않는다. 최종 논리 구조로 제시, 불리한 결과는 부록으로 — **삭제 금지**. 리뷰에서 "pre-specified" 한 단어가 지적된 사례 |
| `rules/11` | **등가성 게이트** | "없음/사전추세 없음/균형" 은 `CI ⊂ ±SESOI` 로만. `p>0.05` 로 "없음"을 주장한 오류가 두 번 반복되어 생긴 규칙 |
| `hooks/stop_guard.py` | 산출물이 바뀌었는데 상태 파일이 안 갱신되면 턴 종료를 막음 | 연속성의 강제 장치 |
| `hooks/protect_paths.py` | 원자료 폴더(`raw/`)와 동결 산출물 보호 | 원자료 무결성. 명령문에 보호 경로 문자열이 들어가면 오탐할 수 있다 — 문서 본문에 그 경로를 쓰지 말 것 |
| `agents/` 13종 | 식별·측정·강건성·문헌·영문·저널·재현성 독립 심판 | 연구감독이 종합, 전문가는 연구질문을 바꾸지 않음 |
| `skills/` 22종 | create-paper · identification-tournament · pre-analysis-freeze · robustness-matrix · internal-review · target-journal · write-section · session-start/close … | 프로젝트 내부 공정 |
| `paper_skeleton/CLAIMS_LEDGER.csv` | `claim_id, exhibit, claim, value, ci95, n, source_json, json_path, code, sha256_16, path_status` | 보고 수치의 출처 고정. **claim_id 유일성**은 `academics:manuscript-verify` 의 `ledger_lint.py` 가 검사(중복이 실제로 발생했던 결함) |

## 가드레일
- 훅·규칙을 "번거로워서" 끄지 않는다. stop_guard 가 막는 것은 기록 누락이고, 그것이 다음 세션의 비용이다.
- 원자료 폴더는 절대 편집하지 않는다. 파생 데이터는 버전 폴더로.
- 한 프로젝트 안에 여러 논문을 두되(`papers/<slug>/`), 결과·표본 규칙을 논문 간에 조용히 옮기지 않는다(rules/08).

## 함께 쓰는 스킬
`academics:idea-harness` → `academics:power-rescue` → `academics:manuscript-verify` → `academics:comment-dispose` → `academics:narrative-audit` → `academics:journal-package` → `academics:replication-repo` · `academics:entity-linkage`
