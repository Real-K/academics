# 하네스 registry.csv

`id, script, question, prediction, status(GO|PARTIAL|KILL|OK), verdict, n, out_json, sha256_16, date, feeds(원장 id·표·그림)`

- 실행 순서 = id 순. `run_all.sh` 가 순서대로 돌리고 실패는 `fix_failed.sh` 로 재시도.
- VERDICT_AUDIT: KILL 판정문을 사후에 다시 읽어 판정이 맞았는지(판정문 오류로 살아있는 설계를 죽인 사례 방지).
- 배터리가 끝나면 "모든 결과를 모으면 인과 설계와 메커니즘 설명이 가능한가" 를 한 표로 답한다(위협 × 근거 × 판정).
