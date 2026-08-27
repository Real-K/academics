---
name: entity-linkage
description: 한국 기업 식별자(사업자번호 bn10/bn6·DART corp_code·ticker·기업명 국/영문)를 여러 소스(PitchBook·국민연금·DART·NICE·IROS·KRX) 사이에서 연결하고, 결측 식별자를 기업명 정규화→영→한 변환→LLM 유사매칭→외부 조회→PI 수작업 adjudication 패키지의 사다리로 회수한다. 회수 후 대조풀 오염 방지·정본 표본 고정·기각 설계 재점검 규칙 포함. "사업자번호 매칭 안 되는 기업 회수", "bn6+기업명 매칭", "처치표본 늘리기", "작업 패키지 제공" 요청 시.
argument-hint: "link <source.csv> --to <panel> [--id-cols ...] | recover <unmatched.csv> --package"
---

# academics:entity-linkage — 기업 식별자 연결·표본 회수

PitchBook(영문)→국민연금(사업자번호)→DART→NICE 를 잇는 과정에서 P-014 처치표본이 283→379 로 늘었고, 그 확장이 논문의 설계를 바꿨다. 이 스킬은 그 사다리와 규칙을 담는다. 데이터 소스별 수집은 `nicebizline-shareholders`·`nicebizline-representatives`·`iros`·`krx-data` 가 맡고, 이 스킬은 **연결 프로토콜**이다.

## 절차
1. 소스별 식별자 열을 목록화하고 `references/linkage_ladder.md` 의 1단계부터 적용. 단계마다 매칭 수·잔여 수를 기록.
2. 3~5단계는 후보를 여러 개 두고 근거를 남긴다(`scripts/name_normalize.py`). LLM 판정은 확신도+근거 문장 필수.
3. 남은 것은 **PI 패키지**(`references/pi_package_template.md`)로. "내가 진행해야 할 부분이 있으면 패키지 제공해" 가 PI 의 표준 요청이다.
4. 반환된 `_COMPLETED` 를 코드가 읽어 적용 → **정본 표본 파일 + sha** 갱신 → CLAUDE.md 에 명시.
5. 회수 기업을 대조 풀 제외집합에 넣는다. 오염 검사: 대조 풀 ∩ 처치 = ∅.
6. 표본이 늘었으면 `academics:idea-harness` 의 KILL 재점검 → `academics:power-rescue`.
7. provenance 표(기업별 매칭 단계)는 내부 `work/` 에만. 공개 저장소 금지.

## 가드레일
- bn6 는 유일하지 않고, bn10 은 사업장 번호일 수 있다 — 둘 중 하나로 "매칭됐다"고 끝내지 않는다.
- 유사매칭의 accept 는 PI 가 한다. 모델은 후보와 근거를 낸다.
- 자격증명(NICE·KRX·DART 키)은 `~/.claude/.env` 에만. 채팅·코드·문서에 쓰지 않는다.
- 회수분의 반응이 원표본과 다를 수 있다(P-014 F.1: 회수 사건 반응이 더 작음) — 그 사실을 보고한다.
