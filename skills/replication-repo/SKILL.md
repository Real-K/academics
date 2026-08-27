---
name: replication-repo
description: 논문의 표·그림을 집계 산출물만으로 재생성하는 출력 저장 노트북(ipynb)과 파이프라인 코드·원장·매니페스트를 GitHub 공개 저장소로 조립·검증·푸시한다. 라이선스 원자료 없이 방문자가 결과와 코드를 함께 보게 하고, 노트북 마지막 셀이 논문 전시물과 바이트/해시 동일함을 assert 한다. 식별자·절대경로·자격증명 스캔, 익명심사 경고 포함. "github에 ipynb로 결과 확인", "복제 저장소", "replication package", "Zenodo" 요청 시.
argument-hint: "<paper-dir> --repo <owner/name> [--exclude <artifact…>] [--sync]"
---

# academics:replication-repo — 출력 저장 노트북 복제 저장소

P-016 `paper_PIPE`·P-014 `paper_Private-Equity-and-Employment` 에서 확립한 방식. 원자료가 라이선스라 방문자는 `.py` 를 못 돌리므로, **집계 산출물(JSON)만으로 표·그림을 재생성하는 노트북에 출력을 저장**해 GitHub 에서 결과·코드를 함께 보게 한다. 저널 정책상 "encouraged"(가점·의무 아님)지만 리뷰어 신뢰도와 재현성의 실질적 증거다.

## 구조
```
notebooks/   01_main_tables · 02_figures · 03_traceability (출력 저장)
artifacts/   집계 JSON + CLAIMS_LEDGER.csv          paper_exhibits/  원고 첨부 표(md)·그림(png/pdf) = 대조 기준
code/pipeline/ 전 분석 스크립트(경로 env 화)          code/build/  표·그림 빌더 + 노트북 빌더     code/verification/
figures/     노트북이 재생성한 그림                    README · DATA_ACCESS · ARTIFACT_MANIFEST · LICENSE(MIT) · .gitignore
```

## 절차
1. **인벤토리**: 표 빌더·그림 빌더·산출물 폴더·원장·전시물 위치. 산출물마다 원장 인용 수(retired 표시).
2. **안전 스캔** `scripts/safety_scan.py <후보 트리> --names <처치기업명…>` — 사업자번호 10자리·회사명 접미사·절대경로·자격증명. 식별자가 든 산출물은 **제외**(P-014: `I05.json` 에 사업자번호 13개 → 제외, 매니페스트에 사유). 파이프라인 주석 속 실제 회사명 → 익명화(조립 스크립트에 내장).
3. **조립**(`references/assemble_example_p014.py` 참고): 산출물 복사(제외 목록 적용) · 파이프라인 복사 + `BASE = os.environ.get("<PROJ>_BASE", "/path/to/project-root")` 치환 · 빌더 복사 + 경로 매개화 · 전시물 참조본 복사 · 매니페스트(sha256₁₆·크기·생성 스크립트·제목·status·원장 인용 수).
4. **노트북 빌드**(`scripts/build_notebooks.py` + `references/make_nb_example_p014.py`): 빌더 스크립트를 마커(`# ───────── Table`, `# ════ Figure`)로 잘라 셀로; 표는 `_md`(text/markdown), 그림은 `_figs`(PNG) 로 출력 저장. **정합성 셀**: 표 = 바이트 비교, 그림 = SHA-256, 원장 = 전 행 경로 해석(bracket-aware), 매니페스트 = 해시. 어긋나면 `assert` → 빌드 실패.
5. 문서: README(노트북 표, 추적 사슬 설명, 검증기 3종 설명, 라이선스), DATA_ACCESS(출처별 재배포 불가 사유·입수 경로·대신 있는 것), MANIFEST, LICENSE. 원고 본문은 넣지 않는다.
6. 재스캔 → `git init -b main` → 로컬 `user.name/email` → 커밋(검사 결과를 메시지에) → `git push -u origin main` → `gh api …/contents` 로 확인.
7. 이후 변경은 `references/resync_protocol.md`.

## 가드레일
- 기업단위 파생 파일(사업자번호·티커·헤드카운트·매칭쌍)은 절대 올리지 않는다.
- 노트북 코드를 손으로 다시 쓰지 않는다 — 빌더 블록을 잘라 넣는다. 그래야 "노트북이 논문과 다를" 여지가 없다.
- 정합성 셀의 통과를 **저장된 출력에서 읽어** 확인한다(빌더 rc=0 만으로 주장하지 않는다).
- 실명 저장소는 익명심사 중 투고본에 링크하지 않는다.
- 저장소 조립용 원장↔산출물 전수 검사가 **원장 중복 claim_id 를 적발**했던 사례 — 조립 자체가 검증이다. 발견하면 원고 쪽 원장을 고치고 다시 조립.
