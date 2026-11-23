---
title: 省 token 小技巧（reduce token usage）
layer: token成本
sources: [S2, S3, S5, S1]
---
> 白話：context 裡只留需要的東西，就能同時省錢、又讓 AI 更準。[S1][S2]

## 是什麼
- 挑選放進 context 的內容，跟有多少空間一樣重要 [S1]。

## 怎麼運作
| 技巧 | 做法 | 來源 |
|---|---|---|
| 換任務就清空 | 換到不相關的工作時跑 `/clear` | [S2] |
| 指定重點壓縮 | 開始長任務前跑 `/compact focus on ...` | [S2] |
| 外包大量閱讀 | 把研究交給子代理，檔案內容留在它的視窗 | [S2] |
| 先看用量 | 用 `/context` 看各類別用量和建議 | [S2] |
| CLAUDE.md 精簡 | 每檔少於 200 行，只跟部分程式有關的放 path-scoped rules | [S3] |
| 備註用 HTML 註解 | 區塊級 HTML 註解不會進 context | [S3] |
| 穩定內容放前面 | 把快取內容放在 prompt 開頭，斷點放在最後一個不變的區塊 | [S5] |
| 別亂改工具定義 | 修改工具定義會讓整個快取失效 | [S5] |

## 跟 token 的關係
- 舊對話會擠掉需要的檔案，而且每則訊息都要花 token [S2]。

## 相關
- [[compaction]]、[[subagent-context]]、[[claude-md]]、[[prompt-caching]]、[[context-rot]]
- 來源頁：[[s1-context-windows]]、[[s2-explore-context-window]]、[[s3-claude-code-memory]]、[[s5-prompt-caching]]
