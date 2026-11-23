# AGENTS.md — LLM Wiki：AI 怎麼記憶 & Token 怎麼耗

你是這個 Wiki 的維護者。目標：把 `raw/` 的官方資料整理成互相連結的 Wiki，之後用來產出一頁給同學看的教學 HTML。

## 資料夾
- `raw/`：原始資料（S1–S5），**唯讀**
- `wiki/concepts/`：概念頁，一頁一個概念
- `wiki/sources/`：每份資料一頁摘要（`s1-context-windows.md` …）
- `wiki/index.md`：目錄，依「三層記憶」排列
- `wiki/log.md`：操作紀錄，只能往後加
- `output/`：教學 HTML 與中間產物

## 規則（7 條）
1. **R1 原始資料不准改**：`raw/` 內任何檔案不得修改、刪除、搬移。
2. **R3 每個事實都要標來源**：句尾標 `[S1]`～`[S5]`。沒有來源的句子不准寫。
3. **R4 改了就要記**：新增或修改任何 Wiki 頁後，同步更新 `wiki/index.md`，並在 `wiki/log.md` 追加一筆：
   `## [YYYY-MM-DD HH:MM] 動作(ingest/query/lint/check) | 對象 | 做了什麼 | 約用 token`
4. **R5 互相連結＋檔名規則**：概念頁之間用 `[[檔名]]` 連結，每頁至少連 2 頁；檔名用英文小寫加連字號（例：`context-window.md`、`prompt-caching.md`）。
5. **R6 語言**：內容用繁體中文；術語第一次出現時附英文，例：上下文視窗（context window）。
6. **R7 不准自己補**：資料沒寫的不准推測或補充；不確定就標 `（待查）`，並寫進 log。
7. **R8 白話摘要**：每頁第一行放一句 `> 白話：……`，讓沒背景的同學也看得懂。

## 概念頁格式
```markdown
---
title: 上下文視窗（context window）
layer: 對話內記憶 | 跨對話記憶 | 外部檔案記憶 | token成本
sources: [S1, S2]
---
> 白話：……

## 是什麼
## 怎麼運作
## 跟 token 的關係
## 相關
- [[token]]、[[context-rot]]
```

## index.md 結構（照教學章節）
1. 對話內記憶（context window、context rot、compaction…）
2. 跨對話記憶（Claude 聊天記憶、搜尋過去對話…）
3. 外部檔案記憶（CLAUDE.md、自動記憶…）
4. Token 成本（token、每輪重送歷史、prompt caching…）
5. 來源（S1–S5）

## 三個操作
- **ingest**：讀一份 `raw/` 資料 → 寫 `wiki/sources/` 摘要 → 新增或更新概念頁 → 更新 index、log
- **query**：先讀 `wiki/index.md`，只打開需要的頁面（省 token），回答要附 `[S#]`
- **lint**：檢查孤兒頁（沒人連過來）、斷連結、沒標來源的句子、殘留的（待查），列出問題並修正
