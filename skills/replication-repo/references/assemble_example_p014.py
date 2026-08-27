import os, re, shutil, json, csv, hashlib, glob, subprocess, sys
ROOT="<PROJECT_ROOT>"
V=f"{ROOT}/P014_upgrade_package/paper_v4"; H30=f"{ROOT}/P014_upgrade_package/harness30"
R=f"{V}/replication"
KEEP={".git","README.md","DATA_ACCESS.md","LICENSE",".gitignore"}          # hand-written / history: never regenerated here
if os.path.exists(R):
    for e in os.listdir(R):
        if e in KEEP: continue
        q=f"{R}/{e}"; shutil.rmtree(q) if os.path.isdir(q) else os.remove(q)
for d in ["notebooks","artifacts","code/pipeline","code/build","code/verification","paper_exhibits/figures","figures"]:
    os.makedirs(f"{R}/{d}",exist_ok=True)

# ── 1. artifacts (aggregate JSON only; I05 excluded — contains business-registration numbers) ──
EXCLUDE={"I05.json"}
arts=[]
for p in sorted(glob.glob(f"{H30}/out/I*.json")):
    if os.path.basename(p) in EXCLUDE: continue
    shutil.copy(p,f"{R}/artifacts/"); arts.append(os.path.basename(p))
shutil.copy(f"{ROOT}/shared/outputs/idea014_h41_2026-08-24/h41_causal_gap.json",f"{R}/artifacts/h41_causal_gap.json"); arts.append("h41_causal_gap.json")
shutil.copy(f"{V}/CLAIMS_LEDGER_v4.csv",f"{R}/artifacts/CLAIMS_LEDGER_v4.csv")

# ── 2. pipeline code (paths → env var) ──
def strip_base(s):
    s=s.replace('BASE = "<PROJECT_ROOT>"',
                'BASE = os.environ.get("P014_BASE", "/path/to/project-root")   # project root holding shared/data (licensed; see DATA_ACCESS.md)')
    s=s.replace('BASE="<PROJECT_ROOT>"',
                'BASE=os.environ.get("P014_BASE","/path/to/project-root")   # project root holding shared/data (licensed; see DATA_ACCESS.md)')
    s=s.replace('sys.path.insert(0, f"{BASE}/Wiki/20-papers/P-014-pe-employment/code")',
                'sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))   # h39_common.py sits alongside in this repository')
    return s
for p in sorted(glob.glob(f"{H30}/*.py")):
    s=open(p,encoding="utf-8").read(); open(f"{R}/code/pipeline/{os.path.basename(p)}","w",encoding="utf-8").write(strip_base(s))
s=open(f"{ROOT}/Wiki/20-papers/P-014-pe-employment/code/h39_common.py",encoding="utf-8").read()
if "import os" not in s.split("\n",15)[0:15].__str__(): s=s.replace("import numpy as np, pandas as pd","import os\nimport numpy as np, pandas as pd",1)
open(f"{R}/code/pipeline/h39_common.py","w",encoding="utf-8").write(strip_base(s))
# anonymise the one comment in the pipeline that names exit-sample firms (public repository)
_q=f"{R}/code/pipeline/i05a_exit_refine.py"; _L=open(_q,encoding="utf-8").read().split("\n")
assert _L[57].startswith("# 실측 오탐") and _L[58].startswith("#")
_L[57]="# 실측 오탐 예시(회사명은 공개 저장소에서 제거): 영문 등기명 vs 한글 등기명, 법인격 표기 위치 차이((주) 접두/접미),"
_L[58]="#           홀딩스/홀딩즈 표기 차이 등 — 이런 쌍이 원시 문자열 비교에서 불일치로 잡히므로 아래 정규화를 거친다."
open(_q,"w",encoding="utf-8").write("\n".join(_L))
for f in ["run_harness30.sh","CODE_INDEX.md","HARNESS30.md","registry.csv"]:
    if os.path.exists(f"{H30}/{f}"):
        t=open(f"{H30}/{f}",encoding="utf-8").read()
        if re.search(r"(?<!\d)\d{10}(?!\d)",t): print("  (skip, 10-digit ids)",f); continue
        open(f"{R}/code/pipeline/{f}","w",encoding="utf-8").write(t.replace(ROOT,"$P014_BASE"))

# ── 3. build code (repo-path parameterized copies) ──
mt=open(f"{V}/build/make_tables.py",encoding="utf-8").read()
mt=mt.replace('''D = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(D)
H = os.path.join(os.path.dirname(P), "harness30", "out")
J = lambda f: json.load(open(os.path.join(H, f + ".json"), encoding="utf-8"))
L = {r["claim_id"]: r for r in csv.DictReader(open(f"{P}/CLAIMS_LEDGER_v4.csv", encoding="utf-8-sig"))}''',
'''_HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.environ.get("P014_ARTIFACTS", os.path.join(_HERE, "..", "..", "artifacts"))      # aggregate result artifacts
OUTDIR = os.environ.get("P014_TABLES", os.path.join(_HERE, "..", "..", "figures"))         # where tables.md is written
J = lambda f: json.load(open(os.path.join(ART, f + ".json"), encoding="utf-8"))
L = {r["claim_id"]: r for r in csv.DictReader(open(os.path.join(ART, "CLAIMS_LEDGER_v4.csv"), encoding="utf-8-sig"))}''')
mt=mt.replace('f"{P}/exhibits/tables.md"','os.path.join(OUTDIR, "tables.md")').replace('f"{P}/exhibits/appendix_tables.md"','os.path.join(OUTDIR, "appendix_tables.md")')
assert "ART =" in mt and "OUTDIR" in mt
open(f"{R}/code/build/make_tables.py","w",encoding="utf-8").write(mt)
me=open(f"{V}/build/make_exhibits.py",encoding="utf-8").read()
me=me.replace('''D = os.path.dirname(os.path.abspath(__file__)); P = os.path.dirname(D)
PKG = os.path.dirname(P); H = os.path.join(PKG, "harness30", "out")
EX = os.path.join(P, "exhibits"); os.makedirs(EX, exist_ok=True)
J = lambda f: json.load(open(os.path.join(H, f + ".json"), encoding="utf-8"))
L = {r["claim_id"]: r for r in csv.DictReader(open(f"{P}/CLAIMS_LEDGER_v4.csv", encoding="utf-8-sig"))}''',
'''_HERE = os.path.dirname(os.path.abspath(__file__))
ART = os.environ.get("P014_ARTIFACTS", os.path.join(_HERE, "..", "..", "artifacts"))      # aggregate result artifacts
EX = os.environ.get("P014_FIGURES", os.path.join(_HERE, "..", "..", "figures")); os.makedirs(EX, exist_ok=True)
J = lambda f: json.load(open(os.path.join(ART, f + ".json"), encoding="utf-8"))
L = {r["claim_id"]: r for r in csv.DictReader(open(os.path.join(ART, "CLAIMS_LEDGER_v4.csv"), encoding="utf-8-sig"))}''')
me=re.sub(r'SAVE\(fig, "(\w+)"\); plt\.close\(fig\); print\("[^"]*"\)', r'SAVE(fig, "\1"); plt.close(fig); print("saved \1.png / \1.pdf")', me)
assert "ART =" in me
open(f"{R}/code/build/make_exhibits.py","w",encoding="utf-8").write(me)
for f in ["verify_draft.py","assert_anchors.py","check_refs.py"]:
    shutil.copy(f"{V}/build/{f}",f"{R}/code/verification/{f}")

# ── 4. paper exhibits (reference copies for the consistency checks) ──
shutil.copy(f"{V}/exhibits/tables.md",f"{R}/paper_exhibits/tables.md"); shutil.copy(f"{V}/exhibits/appendix_tables.md",f"{R}/paper_exhibits/appendix_tables.md")
for p in glob.glob(f"{V}/exhibits/figure*.p??"): shutil.copy(p,f"{R}/paper_exhibits/figures/")

# ── 5. notebook builder ──
BUILD=open(f"{ROOT}/papers/P016_pipe-employment/11_replication/code/build/build_notebooks.py",encoding="utf-8").read()
BUILD=BUILD.replace('''        txt=buf.getvalue()
        if txt.strip():''','''        txt=buf.getvalue()
        # rich outputs handed back by the cell: `_md` (markdown string) and `_figs` (PNG bytes)
        if ns.get("_md"):
            outputs.append({"output_type":"display_data","metadata":{},
                            "data":{"text/markdown":[l+"\\n" for l in ns["_md"].split("\\n")],
                                    "text/plain":[l+"\\n" for l in ns["_md"].split("\\n")]}}); ns["_md"]=None
        for png in ns.get("_figs",[]) or []:
            outputs.append({"output_type":"display_data","metadata":{},
                            "data":{"image/png":base64.b64encode(png).decode()}})
        if "_figs" in ns: ns["_figs"].clear()
        if txt.strip():''')
assert "_md" in BUILD
open(f"{R}/code/build/build_notebooks.py","w",encoding="utf-8").write(BUILD)

shutil.copy(os.environ["CLAUDE_JOB_DIR"]+"/tmp/make_nb_p014.py", f"{R}/code/build/make_nb_p014.py")

# ── 6. manifest (before notebooks: NB03 reads it) ──
RETIRED={"I15.json":"superseded — hazard triple interaction; Table 7 uses specification (4) of Appendix Table F.4.1",
         "I49.json":"superseded — shared-control diagnostic on the 301-event design; replaced by I65 (286 events)",
         "I55_employment_horizons.json":"superseded — inline computation; replaced by I67",
         "I55.json":"superseded design (pre-state-balancing); kept for the record"}
rows=list(csv.DictReader(open(f"{R}/artifacts/CLAIMS_LEDGER_v4.csv",encoding="utf-8-sig")))
cited={}
for r in rows: cited[os.path.basename(r["source_json"])]=cited.get(os.path.basename(r["source_json"]),0)+1
lines=["# Artifact manifest","",
       "Aggregate result files in `artifacts/`. Each is the JSON written by one pipeline script in `code/pipeline/` (the `code` and `sha256_16` fields inside each file identify that script and its hash at run time). Titles are the pipeline's own (Korean) labels. `Ledger rows` counts the claims in `CLAIMS_LEDGER_v4.csv` sourced from the file.","",
       "| Artifact | sha256₁₆ | Bytes | Pipeline script | Title | Status | Ledger rows |","|---|---|---:|---|---|---|---:|"]
for a in arts:
    p=f"{R}/artifacts/{a}"; h=hashlib.sha256(open(p,"rb").read()).hexdigest()[:16]
    try: d=json.load(open(p,encoding="utf-8")); title=str(d.get("title",""))[:70]; code=os.path.basename(str(d.get("code",""))); status=d.get("status","")
    except Exception: title=code=status=""
    st=RETIRED.get(a, status)
    lines.append(f"| `{a}` | `{h}` | {os.path.getsize(p):,} | `{code}` | {title} | {st} | {cited.get(a,0)} |")
lines+=["","## Excluded on purpose","",
        "- `I05.json` (exit reversibility) lists business-registration numbers of the exit sample and is **not** in this repository; the appendix text that cites it remains traceable through the ledger's `source_json` column, and the file is available to editors and referees on request.",
        "- All firm-level derived files (business numbers, monthly headcounts, per-firm outcomes) are excluded — they derive from the licensed pension register.",
        "","`CLAIMS_LEDGER_v4.csv` is the claim-level ledger: one row per reported number, with value, interval, sample size, artifact, JSON path, generating script and its hash. `notebooks/03_traceability.ipynb` resolves every row."]
open(f"{R}/ARTIFACT_MANIFEST.md","w",encoding="utf-8").write("\n".join(lines)+"\n")

# ── 7. run the notebook builder ──
r=subprocess.run([sys.executable,f"{R}/code/build/make_nb_p014.py"],capture_output=True,text=True)
print(r.stdout[-3000:]); print(r.stderr[-3000:] if r.returncode else "builder rc=0")
sys.exit(r.returncode)
