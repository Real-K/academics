# PI 수작업 검토 패키지 형식 (요청 → COMPLETED 반환)

파일: `<task>_REVIEW_PACKAGE.xlsx` → PI 가 `decision` 채워 `<task>_REVIEW_PACKAGE_COMPLETED.xlsx` 로 반환.

| 열 | 내용 |
|---|---|
| candidate_id | 행 id |
| source_name / source_id | 원 소스의 기업명·식별자(영문 포함) |
| candidate_name / candidate_bn | 후보 기업명·사업자번호 |
| evidence | 매칭 근거(정규화 키 일치·주소·업종·대표자·연도) |
| model_confidence | 높음/중간/낮음 + 한 줄 |
| **decision** | PI 기입: accept / reject / alternative(bn) |
| reviewer_note | PI 메모 |

요청서에는 반드시: 목적(어느 논문·어느 표본), 판정 규칙(무엇이면 accept), 예상 소요, 반환 파일명. 반환 후 "참고해서 진행해" 한 줄로 이어질 수 있게 코드는 COMPLETED 파일을 읽어 적용한다.
데이터 요청 대장(`project-control/DATA_REQUESTS.md`)에 요청·반환일 기록.
