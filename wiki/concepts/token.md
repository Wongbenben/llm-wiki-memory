---
title: token（詞元）
layer: token成本
sources: [S1, S2, S5]
---
> 白話：token 是 AI 計算「讀了多少、寫了多少」的單位，上下文視窗的大小和費用都用它來算。[S1][S5]

## 是什麼
- 上下文視窗的容量以 token 計算，依模型最多可到 1M tokens [S1]。
- 一段文字會被切成幾個 token，S1–S5 都沒有說明（待查）。

## 怎麼運作
- 每個回應都會在 `usage` 欄位回報這次請求用了多少 token [S1]。
- 送出前可以用 token counting API 估算用量 [S1]。
- thinking tokens 屬於 `max_tokens` 的一部分，以輸出 token 計費 [S1]。
- 在 Claude Code 中可以用 `/context` 看目前 context 用量的即時分類 [S2]。

## 跟 token 的關係（價格）
- 輸入與輸出分開計價，例如 Claude Opus 5.5 基本輸入 $4 / MTok、輸出 $20 / MTok [S5]。

| 範例 session 的項目 | token |
|---|---|
| System prompt | 4,200 [S2] |
| 專案 CLAUDE.md | 1,800 [S2] |
| 自動記憶 `MEMORY.md` | 680 [S2] |
| 讀一個檔案 `src/api/auth.ts` | 2,400 [S2] |
| 你的第一個 prompt | 45 [S2] |

## 相關
- [[context-window]]、[[history-resend]]、[[prompt-caching]]
- 來源頁：[[s1-context-windows]]、[[s2-explore-context-window]]、[[s5-prompt-caching]]
