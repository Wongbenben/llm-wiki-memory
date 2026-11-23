---
title: 壓縮（compaction）
layer: 對話內記憶
sources: [S1, S2, S3]
---
> 白話：對話太長時，把前面的內容濃縮成摘要，騰出空間繼續聊。[S1]

## 是什麼
- 伺服器端壓縮（server-side compaction）會自動摘要對話較早的部分，讓對話能超過上下文視窗上限繼續進行 [S1]。
- S1 把它列為長對話與 agent 工作流程管理 context 的主要策略 [S1]。
- 在 Claude Code，`/compact` 會用一份結構化摘要取代原本的對話 [S2]。

## 怎麼運作
- Claude Code 在接近上限時會自動壓縮，所以視窗滿了不會讓 session 結束 [S2]。
- 範例 session 中，`/compact` 前用了 22,225 tokens，之後剩 17,095 tokens，其中對話摘要是 1,725 tokens [S2]。
- 壓縮後，專案根目錄的 CLAUDE.md 和自動記憶會從磁碟重新注入 [S2]。
- 只在對話中講過的指示，壓縮後可能消失；要讓它持續存在，就寫進 CLAUDE.md [S3]。
- 也可以主動壓縮：`/compact focus on ...` 指定摘要重點，或用 `/autocompact` 設定多滿時自動壓縮 [S2]。

## 跟 token 的關係
- 壓縮把長長的歷史換成較短的摘要，範例中 context 用量從 22,225 降到 17,095 tokens [S2]。

## 相關
- [[context-window]]、[[claude-md]]、[[auto-memory]]、[[history-resend]]
- 來源頁：[[s1-context-windows]]、[[s2-explore-context-window]]、[[s3-claude-code-memory]]
