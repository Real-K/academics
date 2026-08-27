---
name: idea-harness
description: 연구 아이디어 N개(30/100/300)를 인과식별·메커니즘·moderator/mediator·counter-intuitive 각도·데이터·Gate/Kill/Pivot·점수가 채워진 카드로 생성하고, 번호 하네스(iNN 스크립트 + emit 계약 + registry)로 순차 실행해 기각을 소거하며 수렴한다. 새 논문 착수, 막힌 논문의 재발명(reinvite), 표본·데이터가 확장된 뒤 기각 설계 전면 재점검 때. "아이디어 100개 생성해서 하나씩 점검", "다중 경로 하네스", "harness 구성해서 하나씩" 요청 시.
argument-hint: "generate <N> --context <문서…> | scaffold <harness-dir> | run <harness-dir> [--from iNN]"
---

# academics:idea-harness — 아이디어 배터리 → 소거형 하네스

RE014(300 가설)·P-014 업그레이드(30/100 아이디어)·P-016(100 아이디어) 에서 쓴 방식. 하나의 설계에 매달리지 않고 **후보를 넓게 생성 → 카드로 규격화 → 하나씩 실행 → 기각 소거 → 살아남은 것으로 논문**.

## generate
- 입력: 보유 데이터 목록(+입수 가능 공공·API 데이터), 기존 결과·실패 이력, PI 선호(인과설계·메커니즘 identification·moderator 와 mediator·부호 반전/counter-intuitive·finance SSCI).
- 출력: `references/idea_card_template.md` 규격의 카드 N개 + JSON 인덱스. **빈 필드 금지** — 특히 Kill 조건과 필요 데이터. 실패·보류·재탐색 금지 경계(이전 KILL)는 유지한 채 새 처치·새 시계·새 estimand 를 요구한다.
- 카드에 반드시 "이 결과가 나오면 독자가 왜 놀라는가" 한 문장.

## scaffold
- `iNN_<slug>.py` 스텁(`scripts/new_harness_script.py` — 번호 충돌 방지), `emit_contract.py`, `registry.csv`(`references/registry_schema.md`), `run_all.sh`.
- 스크립트 머리에 **사전 예측**을 쓴다. 결과 뒤에 쓰면 사후 합리화다.

## run
- 순서대로 하나씩. 각 결과는 GO/PARTIAL/KILL + verdict 한 줄. 등가성은 CI 로(rules/11).
- KILL 은 되살리지 않는다. 약해진 GO 는 `academics:power-rescue` 로 넘긴다(레버는 그 스킬에).
- 배터리 종료 시 종합표: 위협 × 근거 × 판정 → "인과 설계 + 메커니즘 근거 k개" 가 논문의 뼈대.
- **표본·데이터가 확장되면 KILL 을 전부 재점검**한다(P-014: 처치 283→379 뒤 재점검).

## 가드레일
- 카드 수를 채우기 위한 변형 카드(창만 바꾼 것)를 만들지 않는다 — 처치·시계·estimand 중 하나는 달라야 한다.
- 30개를 다 돌려도 메커니즘이 안 나오면 그렇게 쓴다("observe where the response lives, not what produces it"). 있는 척하지 않는다.
- 판정문이 틀렸다는 의심이 들면(PI 가 두 번 제기) VERDICT_AUDIT 로 KILL 을 재독한다 — 코드가 구버전이어서 KILL 난 사례가 있었다.
