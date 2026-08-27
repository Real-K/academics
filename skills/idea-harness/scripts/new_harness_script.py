# -*- coding: utf-8 -*-
"""하네스 스크립트 스텁 생성. 사용: python3 new_harness_script.py <harness-dir> <slug> "<한 줄 질문>" "<사전 예측>"
번호는 폴더의 기존 iNN 최대값+1 — 기존 산출물을 덮어쓰는 사고를 막는다."""
import os, re, sys
d, slug, q, pred = sys.argv[1:5]
nums = [int(m.group(1)) for f in os.listdir(d) for m in [re.match(r"i(\d+)_", f)] if m]
outs = [int(m.group(1)) for f in os.listdir(os.path.join(d, "out")) for m in [re.match(r"I(\d+)\.json", f)] if m] if os.path.isdir(os.path.join(d, "out")) else []
n = max(nums + outs + [0]) + 1; name = f"i{n:02d}_{slug}.py"
open(os.path.join(d, name), "w", encoding="utf-8").write(f'''# -*- coding: utf-8 -*-
"""I-{n:02d} {q}

[왜] <어느 약점·어느 리뷰·어느 아이디어 카드에서 왔는가>
[사전 예측] {pred}
[Kill] <이 조건이면 KILL 로 판정하고 다른 레버로 간다>

Panel A  ...
Panel B  ...
"""
from emit_contract import emit, qci, SEED
import numpy as np
rng = np.random.default_rng(SEED)
# ... 분석 ...
emit("I-{n:02d}", "{q}", "PARTIAL", {{}}, prediction="{pred}", verdict="<한 줄 판정>", kill_met=False, n=None)
''')
print("created", name)
