# -*- coding: utf-8 -*-
r"""공백 무시 정확 치환기. 하드랩된 마크다운에서 문장을 안전하게 바꾼다.

- 패턴의 공백은 \s+ 로 해석 → 줄바꿈 위치가 달라도 매치.
- 정확히 count 번 매치해야만 치환(기본 1). 0 이나 2 이상이면 예외 → 잘못된 곳을 고치지 않는다.
- 모든 치환이 성공한 뒤에만 파일에 쓴다(done()). 실패 시 파일은 그대로.

모듈:  from ed import make; rep, done = make("draft.md"); rep(old, new); rep(old2, new2, 2); done()
CLI :  python3 ed.py --batch edits.json     # [{"file":..,"old":..,"new":..,"count":1}, ...]
"""
import re, sys, json
def make(path):
    s = open(path, encoding="utf-8").read(); log = []
    def rep(old, new, n=1):
        nonlocal s
        pat = re.compile(r"\s+".join(re.escape(t) for t in old.split()))
        m = pat.findall(s); assert len(m) == n, (path.split("/")[-1], len(m), old[:70])
        s = pat.sub(lambda _: new, s, count=n); log.append(old[:45])
    def done():
        open(path, "w", encoding="utf-8").write(s); print(f"  {path.split('/')[-1]}: {len(log)}건")
    return rep, done
if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--batch":
        edits = json.load(open(sys.argv[2], encoding="utf-8")); byfile = {}
        for e in edits: byfile.setdefault(e["file"], []).append(e)
        for f, es in byfile.items():
            rep, done = make(f)
            for e in es: rep(e["old"], e["new"], e.get("count", 1))
            done()
    else: print(__doc__)
