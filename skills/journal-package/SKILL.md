---
name: journal-package
description: SSCI 재무 저널 표적 선정과 투고 패키지 조립. 지표(IF·SJR·SNIP) 실측, 최근 계보(같은 주제의 게재 논문과 식별 수준) 스캔, Guide for Authors 추출(단어·초록·highlights 한도·블라인드·선언·제출료), 핵심 §2 이후 공유 + 저널별 초록·서론 셸 빌더, docx(수식·표 렌더)·title page·highlights·부록 조립, 한도 점검, 익명성 점검, 두 논문 동시 진행 시 분산 규칙. "타겟 저널", "게재 가능성 기준 저널", "제출 패키지", "docx 생성", "highlights", "title page" 요청 시.
argument-hint: "target <paper-dir> | shells <core.md> --journals IRFA,PBFJ | package <journal>"
---

# academics:journal-package — 저널 표적과 투고 패키지

## target
1. 후보 저널을 PI 의 기준(게재 가능성 = 적합성 × 계보 × 지표; Q2~Q4 도 배제하지 않음)으로 나열.
2. **지표 실측** — 웹에서 IF/SJR/SNIP 을 조회일과 함께. 지표가 갈리면 갈린다고 쓴다(P-014: IF 는 IRFA, SNIP 은 PBFJ 우세).
3. **계보 스캔** — 저널별 최근 3~5년 같은 주제 논문: 설계·식별·메커니즘 수준, 우리와의 연속성. "우리보다 나았는가"까지.
4. **Guide for Authors 실측** (`references/gfa_checklist.md`) — 기억으로 쓰지 않는다.
5. `references/targeting_template.md` 로 메모 작성 → PI 결정. 두 논문이면 분산 규칙 적용.

## shells (저널별 원고)
- 핵심 원고의 **§2 이후는 공유**, 초록·서론·highlights·키워드만 저널 셸에 둔다(빌더 스크립트 안). 그래서 리뷰 반영 시 **핵심 + 셸 둘 다** 고쳐야 한다(`academics:comment-dispose` 전파 순서).
- 빌더가 단어수·highlights 한도를 출력하게 한다(`scripts/limits_check.py`).
- 지역 정체성이 강한 저널(PBFJ)은 서론을 지역 setting 으로, 일반 저널(IRFA)은 경제적 질문으로 연다.

## package
- 본문 docx(수식·표가 렌더되는 변환기; md 그대로 넣으면 안 보인다), title page(`references/titlepage_template.md`), highlights, 온라인 부록(+부록 표), 그림 파일. 캡션 블록은 조립 코드 안에 있으므로 **`academics:manuscript-verify` 의 캡션 검사**를 통과한 뒤 조립.
- 제출료 문장은 title page 에 넣지 않는다(내부 메모에만).
- **익명성**: 저자명·실명 저장소 URL·감사문이 본문·부록·캡션·그림 메타데이터에 없는지 grep.
- Generative AI 선언은 사실대로 — 이 워크플로 자체가 AI 를 문구 검토·설계 리뷰·코드 작성에 썼다.

## 가드레일
- 지표·한도·정책은 **조회한 원문**만 인용. 기억으로 "PBFJ 는 5,000단어" 같은 말을 쓰지 않는다.
- 초록 한도는 리뷰 반영 때마다 깨진다(단어 추가) — 셸 재생성마다 확인.
- 저널을 바꿔도 결과·주장을 바꾸지 않는다. 바뀌는 것은 프레이밍과 서론뿐.
