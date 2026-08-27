# -*- coding: utf-8 -*-
"""한국 기업명 정규화 — 법인격 표기·공백·괄호·영문 접미사를 제거해 비교 키를 만든다.
P-014 파이프라인(i05a/i19)에서 쓰던 정규식. 사용: from name_normalize import norm; norm("(주)코리아에너지홀딩스") == norm("코리아에너지홀딩스 주식회사")
"""
import re, unicodedata
_SUF = re.compile(r"주식회사|유한회사|유한책임회사|합자회사|합명회사|\(주\)|\(유\)|㈜|㈜|limited|ltd\.?|inc\.?|corp\.?|corporation|company|co\.?\b", re.I)
def norm(x: str) -> str:
    if not isinstance(x, str): return ""
    x = unicodedata.normalize("NFKC", x); x = _SUF.sub("", x)
    x = re.sub(r"[\s\-\_\.,·&'\"()\[\]/]+", "", x)
    return x.lower().replace("홀딩즈", "홀딩스")
if __name__ == "__main__":
    import sys; [print(norm(a)) for a in sys.argv[1:]]
