---
name: manuscript-verify
description: 원고↔산출물 정합성 검증기 세트 설치·실행. verify_draft(수치 전역 대조 + 폐기 산출물 제외 + 원장 SUPERSEDED 행에서 차단수치 자동도출 + 캡션 블록), assert_anchors(헤드라인 청구→출처 고정), check_refs(절·표·그림·부록 참조 + 캡션 제목 삼자 일치), ledger_lint(claim_id 유일성·경로 해석·sha). 음성 대조 프로토콜 포함. "원고 수치 검증", "검증기 돌려", "표 번호 참조 확인", "원장 점검", "제출 전 정합성" 요청 시.
argument-hint: "install <paper-build-dir> | run | negative-control"
---

# academics:manuscript-verify — 원고·산출물 정합성 검증기

원고의 모든 수치·참조·캡션이 산출물과 원장에 닿아 있음을 기계로 확인한다. 두 논문에서 **리뷰어가 잡은 수치 결함 20건 이상**이 전부 같은 원인이었다: 전역 풀 검증기는 폐기된 설계의 값이 산출물 어딘가에 남아 있으면 통과시킨다. 이 스킬의 검증기 3+1종은 그 사각지대를 막도록 만든 것이다.

## install
1. `scripts/*.py` 를 논문의 `build/` 로 복사, `verify_config.example.json` → `verify_config.json` 으로 채운다(경로는 설정 파일 기준 상대).
2. `anchors.json` 을 만든다: 헤드라인 청구마다 `{"claim","values","source"}`. 처음엔 초록·서론의 수치부터.
3. `retired_artifacts` 에 원장에 살아있는 행이 없는 산출물을 적는다. 애매하면 `ledger_lint` 출력의 source 분포로 판단.
4. **음성 대조** (`references/negative_control.md`) 를 실행해 4/4 검출을 확인한 뒤에야 "설치 완료".

## run (제출 전·리뷰 반영 후·표 재편 후 매번)
```
python3 build/verify_draft.py     # 미확인 0 · 폐기 0
python3 build/assert_anchors.py   # 불일치 0
python3 build/check_refs.py       # 미해결 0 · 캡션 0
python3 build/ledger_lint.py      # 중복 0 · 불일치 0
```
넷 다 exit 0 이어야 한다. 하나가 실패하면 원고를 고치기 전에 **어느 검증기가 왜 실패했는지** 기록.

## 사각지대와 그 대책 (실제 사고 → 규칙)
| 사고 | 대책 |
|---|---|
| hazard 1.2512(구설계)가 통과 — 다른 산출물에 값이 남아 있었다 | `retired_artifacts` 제외 + SUPERSEDED 행 자동 차단(`build_stale`, 반올림 충돌 가드) |
| 점추정은 맞고 CI 는 다른 산출물 것인 조합 | `assert_anchors` — 청구별 출처 JSON 안에서만 확인 |
| 표 재번호 후 구 번호 11곳 잔존 | `check_refs` — 수치가 안 바뀌는 변경은 참조 축으로만 잡힌다 |
| 그림 캡션 블록이 코드 안에만 있어 4라운드 생존 | `caption_source` 로 FIGCAP 을 두 검증기 모두의 대상에 포함, 캡션↔그림↔FIGS 제목 삼자 일치 |
| 원장 claim_id 중복 4건 — 표는 맞고 추적 사슬은 끊김 | `ledger_lint` 유일성 assert |
| 귀무 CI 가 추정치 CI 로 기재 | `references/ledger_schema.md` 의 ci95 규칙 |
| 쉼표 없는 4자리 수를 정규식이 통째로 놓침 | `(?:\d{1,3}(?:,\d{3})+|\d+)` |

## 가드레일
- 검증기가 통과했다고 "정합성 확인"이라 쓰지 않는다 — **관측된 출력 줄**을 기록에 붙인다.
- 검증기를 통과시키기 위해 `extra_constants` 에 원고 수치를 추가하는 것은 금지. 상수는 제도·표본 사실(연도·법정 비율)에만.
- 폐기 행은 삭제하지 않는다 — 차단목록의 원천이다.
