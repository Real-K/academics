# 하네스 계약

- 스크립트 이름 `iNN_<slug>.py` (번호 = 작성 순서). 한 스크립트 = 한 질문 = 한 JSON.
- 머리 docstring: 왜(어느 리뷰·어느 약점) · Panel 목록 · 사전 예측.
- 출력 `out/INN.json` — `emit()` 계약 (`id, title, status GO|PARTIAL|KILL|OK, n, estimates, prediction, verdict, kill_met, code, sha256_16, seed, date`).
- **같은 seed** — 재실행 시 추정치가 불변인지가 재현성의 첫 검사. 필드만 추가하는 재실행(예: `p_upper` 저장)은 값이 그대로여야 한다.
- 새 스크립트 번호가 기존과 겹치면 기존 산출물을 덮어쓴다 — 번호를 배정하기 전에 `ls out/` 확인(P-014 에서 I-61~63 을 덮어써 복구한 사고).
- 산출물에 기업 식별자를 넣지 않는다(공개 저장소 대비). 필요하면 별도 `work/` 에.
- 원장 행 추가 시 `claim_id` 충돌 검사 → `ledger_lint`.
