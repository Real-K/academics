from __future__ import annotations
import argparse, csv, json, re, subprocess, sys
from pathlib import Path
from _common import ROOT, paper_dirs, paper_id_from_dir, read_csv, active_paper_id

REQUIRED_ROOT=["CLAUDE.md",".claude/settings.json","project-control/ACTIVE_PAPER","shared/registries/paper_registry.csv","Wiki/index.md","shared/templates/paper-skeleton/CLAUDE.md"]
PAPER_REQUIRED=["CLAUDE.md","00_admin/CURRENT_STATE.md","00_admin/DECISION_LOG.md","00_admin/SESSION_LOG.md","01_question/RESEARCH_QUESTION.md","01_question/ESTIMAND_CARD.md","03_theory/HYPOTHESIS_REGISTRY.csv","04_design/PRE_ANALYSIS_PLAN.md","04_design/SPECIFICATION_GRID.yaml","05_data/data_manifest.yaml","06_code/README.md","07_analysis/run_log.csv","08_manuscript/manuscript.md","08_manuscript/CLAIMS_LEDGER.csv","09_review/REVIEW_MATRIX.csv","10_submission/SUBMISSION_CHECKLIST.md"]
NAME=re.compile(r"^name:\s*([a-z0-9-]+)\s*$",re.M)
DESC=re.compile(r"^description:\s*(.+)$",re.M)


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--quick',action='store_true');args=ap.parse_args()
    errors=[];warnings=[]
    for rel in REQUIRED_ROOT:
        if not (ROOT/rel).exists(): errors.append(f"Missing required root path: {rel}")
    try: json.loads((ROOT/'.claude/settings.json').read_text(encoding='utf-8'))
    except Exception as exc: errors.append(f"Invalid settings.json: {exc}")
    if len((ROOT/'CLAUDE.md').read_text(encoding='utf-8').splitlines())>200: warnings.append('Root CLAUDE.md exceeds 200 lines')

    names={}
    for kind in ['agents','skills']:
        paths=(ROOT/'.claude'/kind).glob('*.md') if kind=='agents' else (ROOT/'.claude'/kind).glob('*/SKILL.md')
        for path in paths:
            text=path.read_text(encoding='utf-8')
            if not text.startswith('---'): errors.append(f"Missing frontmatter: {path.relative_to(ROOT)}")
            nm=NAME.search(text); desc=DESC.search(text)
            if not nm: errors.append(f"Missing/invalid name: {path.relative_to(ROOT)}"); continue
            if not desc: errors.append(f"Missing description: {path.relative_to(ROOT)}")
            key=(kind,nm.group(1))
            if key in names: errors.append(f"Duplicate {kind} name {nm.group(1)}")
            names[key]=path
            if kind=='skills' and path.parent.name!=nm.group(1): errors.append(f"Skill folder/name mismatch: {path.relative_to(ROOT)}")

    fields,rows=read_csv(ROOT/'shared/registries/paper_registry.csv')
    registered={r.get('paper_id'):r for r in rows}
    folders={paper_id_from_dir(p):p for p in paper_dirs()}
    for pid,paper in folders.items():
        if pid not in registered: errors.append(f"Unregistered paper folder: {paper.name}")
        for rel in PAPER_REQUIRED:
            if not (paper/rel).exists(): errors.append(f"{pid} missing {rel}")
    for pid,row in registered.items():
        if pid and pid not in folders: errors.append(f"Registry points to absent paper: {pid}")
    active=active_paper_id()
    if active!='NONE' and active not in folders: errors.append(f"ACTIVE_PAPER {active} has no unique folder")
    if sum(1 for r in rows if r.get('active','').lower()=='true')>1: errors.append('More than one registry row is active')
    if active!='NONE' and not any(r.get('paper_id')==active and r.get('active','').lower()=='true' for r in rows): warnings.append('ACTIVE_PAPER and registry active flag differ')

    # 혼합 날짜형식 게이트 (D-2026-08-23-datefix): pd.to_datetime(errors="coerce")의 무성 탈락 방지
    DATECOL=re.compile(r"date|_dt$|일자",re.I)
    PATS=[("YYYYMMDD",re.compile(r"\d{8}")),("YYYY-MM-DD",re.compile(r"\d{4}-\d{2}-\d{2}")),
          ("YYYY/M/D",re.compile(r"\d{4}/\d{1,2}/\d{1,2}"))]
    for path in list((ROOT/'shared/outputs').rglob('*.csv'))+list((ROOT/'shared/data/processed').glob('*.csv')):
        if 'ORIGINAL' in path.name or path.stat().st_size>50_000_000: continue
        try: cols,recs=read_csv(path)
        except Exception: continue
        for col in [c for c in (cols or []) if DATECOL.search(str(c))]:
            seen=set()
            for r in recs[:5000]:
                v=str(r.get(col,'') or '').strip()
                if not v: continue
                for nm,p in PATS:
                    if p.fullmatch(v): seen.add(nm); break
            if len(seen)>1:
                errors.append(f"Mixed date formats in {path.relative_to(ROOT)} [{col}]: {sorted(seen)} — normalise or use shared/lib/safe_dates.py")

    if not args.quick:
        result=subprocess.run([sys.executable,str(ROOT/'scripts/wiki_lint.py')],cwd=ROOT,capture_output=True,text=True)
        print(result.stdout,end='')
        if result.returncode: errors.append('Wiki lint failed')
        result=subprocess.run([sys.executable,'-m','unittest','discover','-s','tests'],cwd=ROOT,capture_output=True,text=True)
        print(result.stdout,end='');print(result.stderr,end='')
        if result.returncode: errors.append('Unit tests failed')
    report=ROOT/'logs/validations/latest_validation.txt';report.parent.mkdir(parents=True,exist_ok=True)
    lines=[f"errors={len(errors)} warnings={len(warnings)}"]+[f"ERROR {e}" for e in errors]+[f"WARN {w}" for w in warnings]
    report.write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(f"Validation: {len(errors)} errors, {len(warnings)} warnings")
    for e in errors: print('ERROR:',e)
    for w in warnings: print('WARN:',w)
    if errors: sys.exit(1)


if __name__=='__main__': main()
