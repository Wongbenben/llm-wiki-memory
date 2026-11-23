"""關卡2 來源檢查：python scripts/check_sources.py N
讀 output/section-N.md 和 output/evidence-N.md（| # | 摘錄 | 來源 | 原文 |），檢查：
 1. 每一個證據列的「原文」真的出現在 raw/ 對應來源（忽略 markdown 符號、連結網址、彎引號、空白差異）
 2. 段落裡每一行有 [S#] 的事實，每個 S# 都有一列證據（摘錄是這行的一部分、來源一樣）
 3. 沒有標來源的事實行（標題、空行、表頭、「> 圖：」說明除外）
 4. 沒有殘留（待查）
全部通過印 PASS，否則印 FAIL 和問題清單。
"""
import re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
R = pathlib.Path(__file__).resolve().parent.parent
N = sys.argv[1]
RAW = {f"S{i}": next((R/"raw").glob(f"s{i}-*.md")).read_text(encoding="utf-8") for i in range(1, 6)}
def norm(s):
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)          # [text](url) → text
    s = re.sub(r"<[^>]+>", " ", s)                             # html tags
    s = s.replace("“", '"').replace("”", '"').replace("’", "'").replace("‘", "'").replace("​", "")
    s = re.sub(r"[*`]", "", s)                                # markdown 粗體、程式碼標記直接拿掉
    s = re.sub(r"[>|]", " ", s)
    return re.sub(r"\s+", " ", s).strip().lower()
RAWN = {k: norm(v) for k, v in RAW.items()}
sec = (R/"output"/f"section-{N}.md").read_text(encoding="utf-8").splitlines()
ev = []
for l in (R/"output"/f"evidence-{N}.md").read_text(encoding="utf-8").splitlines():
    c = [x.strip() for x in l.strip().strip("|").split("|")]
    if len(c) >= 4 and c[0].isdigit():
        ev.append({"no": c[0], "ex": c[1], "src": c[2].strip("[]"), "quote": "|".join(c[3:])})
problems = []
for e in ev:
    if e["src"] not in RAWN: problems.append(f"#{e['no']} 來源代號錯誤 {e['src']}")
    elif norm(e["quote"].replace("\|", "|")) not in RAWN[e["src"]]:
        problems.append(f"#{e['no']} 原文在 {e['src']} 找不到：{e['quote'][:70]}")
used = set()
for i, l in enumerate(sec):
    s = l.strip()
    if not s or s.startswith("#") or s.startswith("> 圖") or re.fullmatch(r"\|[-:| ]+\|", s): continue
    if s.startswith("|") and i+1 < len(sec) and re.fullmatch(r"\|[-:| ]+\|", sec[i+1].strip()): continue
    if "（待查）" in s: problems.append(f"殘留（待查）：{s}")
    tags = set(re.findall(r"\[(S[1-5])\]", s))
    if not tags:
        problems.append(f"漏標來源：{s}"); continue
    for t in tags:
        hit = [e for e in ev if e["src"] == t and e["ex"] in s]
        if not hit: problems.append(f"沒有證據：[{t}] {s[:60]}")
        used.update(e["no"] for e in hit)
for e in ev:
    if e["no"] not in used: problems.append(f"#{e['no']} 證據沒對到任何句子（摘錄：{e['ex']}）")
print(f"section-{N}：證據 {len(ev)} 列")
for p in problems: print(" -", p)
print("PASS" if not problems else f"FAIL（{len(problems)} 個問題）"); sys.exit(1 if problems else 0)
