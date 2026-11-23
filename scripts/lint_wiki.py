"""Wiki lint：孤兒頁、斷連結、連結數 < 2、沒標來源的句子、殘留（待查）、缺白話摘要。
用法：python scripts/lint_wiki.py
"""
import re, pathlib, sys
sys.stdout.reconfigure(encoding="utf-8")
W = pathlib.Path(__file__).resolve().parent.parent / "wiki"
pages = {p.stem: p for p in list((W/"concepts").glob("*.md")) + list((W/"sources").glob("*.md"))}
LINK = re.compile(r"\[\[([^\]]+)\]\]")
SRC = re.compile(r"\[S[1-5]\]")
inbound = {k: set() for k in pages}
problems = []
def body(text):
    return re.sub(r"\A---.*?---\s*", "", text, flags=re.S)
for name, p in pages.items():
    text = p.read_text(encoding="utf-8")
    links = set(LINK.findall(text))
    for l in links:
        if l in pages: inbound[l].add(name)
        else: problems.append(f"斷連結   {p.relative_to(W)} → [[{l}]]")
    if p.parent.name == "concepts" and len(links - {name}) < 2:
        problems.append(f"連結<2   {p.relative_to(W)}")
    lines = body(text).splitlines()
    first = next((l for l in lines if l.strip()), "")
    if not first.startswith("> 白話："):
        problems.append(f"缺白話   {p.relative_to(W)}")
    in_related = False
    for i, l in enumerate(lines):
        s = l.strip()
        if s.startswith("#"):
            in_related = s.startswith("## 相關") or s.startswith("## 對應概念頁"); continue
        if "（待查）" in s:
            problems.append(f"待查     {p.relative_to(W)}: {s}")
            continue
        if not s or in_related or re.fullmatch(r"\|[-:| ]+\|", s): continue
        if s.startswith("|") and s.count("|") >= 3:
            cells = [c.strip() for c in s.strip("|").split("|")]
            # 表頭列（下一行是分隔線）不用標
            nxt = lines[i+1].strip() if i+1 < len(lines) else ""
            if re.fullmatch(r"\|[-:| ]+\|", nxt): continue
            if not SRC.search(s): problems.append(f"漏標來源 {p.relative_to(W)}: {s}")
            continue
        if not SRC.search(s):
            problems.append(f"漏標來源 {p.relative_to(W)}: {s}")
idx = (W/"index.md").read_text(encoding="utf-8")
for l in set(LINK.findall(idx)):
    if l not in pages: problems.append(f"斷連結   index.md → [[{l}]]")
for name in pages:
    if not inbound[name]:
        problems.append(f"孤兒頁   {pages[name].relative_to(W)}（除了 index 沒有頁面連過來）")
    if f"[[{name}]]" not in idx:
        problems.append(f"未列索引 {pages[name].relative_to(W)}")
print(f"頁數：{len(pages)}（concepts {len(list((W/'concepts').glob('*.md')))}，sources {len(list((W/'sources').glob('*.md')))}）")
for x in problems: print(x)
print("OK" if not problems else f"問題數：{len(problems)}")
