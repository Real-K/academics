---
name: comment-dispose
description: 외부 리뷰·코멘트 파일(comment/N.md, 심사의견, 공동저자 메모)을 전수 읽고 항목별로 산출물 대조 → 실재/정의차이/과장/오탐 분류 → 원고·저널셸·표·그림·캡션·부록에 전파 → 잔존 스윕 → 검증기 → 처분 대장(RESPONSE_N.md) → 기록 갱신까지 한 번에 수행한다. "코멘트 문서를 면밀하게 빠짐없이 읽어 반영 여부 검토", "리뷰 반영해", "referee report 대응" 요청 시.
argument-hint: "<comment.md 경로…> [--submission <저널>] [--sync-repo]"
---

# academics:comment-dispose — 외부 코멘트 전수 처분

두 논문에서 56회 반복된 지시("문서를 면밀하게 빠짐없이 읽어. 모든 코멘트에 대해서 우리 paper에 반영 여부를 검토해. 모든 사항을 점검했는지를 Think the answer TWICE")를 절차로 고정한 것이다. 원칙 하나: **리뷰어의 사실 주장도 검증 대상**이다. 리뷰어가 틀린 사례가 라운드마다 있었다(`references/lessons.md`).

## 입력
- 코멘트 파일 경로(여러 개 가능). 어느 제출본 기준인지(`--submission IRFA`) — 셸별 초록·서론이 다르다.
- 프로젝트의 검증기(`academics:manuscript-verify` 설치 전제)와 원장(CLAIMS_LEDGER).

## 절차 (건너뛰지 않는다)
1. **전문 읽기 → 항목 번호화.** 표·번호목록·본문 문장 속 지적까지 전부 나열한다. 요약본을 만들지 말고 원문 항목 단위로.
2. **항목별 사실 확인.** 지적이 수치·표본·설계에 관한 것이면 원장(`claim_id`)과 산출물 JSON 을 직접 열어 확인한다. 분류:
   - **실재** — 고친다.
   - **정의 차이** — 두 값이 다른 정의(창 규칙·표본·설계)면 재계산이 아니라 **정의를 명시**한다.
   - **과장 표현** — 어휘 보정(`academics:narrative-audit` 의 calibration_vocabulary 참조).
   - **오탐** — 리뷰어 오류. 근거를 대장에 남기고 원고는 설명 문장만 보강.
   - **채택 안 함** — 사유 필수(예: 파급 범위 대비 결론 불변; 대안 채택).
3. **백업** `comment/_pre_rN/` 에 편집 대상 파일 복사.
4. **편집**은 `scripts/ed.py`(공백 무시·정확 1회 매치·전체 성공 후 저장)로. 문자열이 줄바꿈으로 갈라져 grep 이 놓치는 경우가 많으니 반드시 이 치환기를 쓴다.
5. **전파 순서**: 핵심 원고 → 저널 셸(빌더 안의 초록·서론·highlights) → 표 빌더(제목·주석) → 그림 빌더(제목·각주) → **캡션 블록(제출 조립 코드 안)** → 온라인 부록 → 전시물 색인. 저널 셸 재생성 후 초록 단어수·highlights 글자수 한도 확인.
6. **잔존 스윕** `scripts/residual_sweep.py --patterns <지적된 문구들> --files <생성 문서 전부>` → 0 이어야 한다. 남은 것은 하나씩 읽고 "같은 표현의 다른 의미"만 허용.
7. **검증기**: 수치(verify_draft) · 앵커(assert_anchors) · 참조+캡션(check_refs) · 원장 lint · docx 재생성.
8. **분석 코드가 바뀌었으면**: 산출물 재실행 → 원장 값·sha 동기화 → 앵커 갱신 → 복제 저장소 동기화(`academics:replication-repo`).
9. **처분 대장** `comment/RESPONSE_N.md` (`references/RESPONSE_TEMPLATE.md`). 불리한 결과 절은 비워두지 않는다.
10. **기록**: RESULTS_LEDGER § 추가(분석 사실만) · PROGRESS · SESSION_HANDOFF · validate.

## 가드레일
- 불리한 결과는 **부록으로 이동**하되 삭제하지 않는다(rules/10). "보고할 필요 없어"는 이동 지시로 이행한다.
- preregistration 어휘("pre-specified", "ex ante", "frozen")를 새로 들이지 않는다. 방향 가설은 "directional hypothesis" 로만.
- "every specification", "specific to", "cannot be affected", "precise zero", "not in X" (X 에 반대 방향 효과가 검출된 경우) 같은 전칭·단정 표현은 항목에 없어도 스윕한다.
- 한 라운드에 신규 회귀를 추가하라는 유혹을 경계한다. 리뷰어가 "production pass 만" 이라고 하면 그대로 따른다.
- 리뷰어가 큰 재계산을 요구하면 **허용된 대안**이 있는지 먼저 찾고, 선택 사유를 대장에 남긴다.

## 산출물
`comment/RESPONSE_N.md` · 갱신된 원고/셸/표/그림/캡션/부록 · 검증 로그(관측된 출력) · 기록 3종.
