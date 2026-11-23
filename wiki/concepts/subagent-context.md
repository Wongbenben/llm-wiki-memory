---
title: 子代理的獨立視窗（subagent context）
layer: 對話內記憶
sources: [S2, S3]
---
> 白話：派一個小幫手在它自己的記憶空間裡讀大量資料，只把摘要帶回主對話。[S2]

## 是什麼
- 子代理（subagent）在自己獨立的上下文視窗處理研究工作，大量的檔案讀取不會進到你的視窗；只有摘要和一小段 metadata 會回來 [S2]。

## 怎麼運作
- 範例 session 中，子代理的摘要帶回 420 tokens，而子代理自己的視窗另外用了 9,890 tokens [S2]。
- 主對話的自動記憶不會載入子代理；例外是 fork，它會繼承父對話與 system prompt [S3]。

## 跟 token 的關係
- 把大量閱讀交給子代理，檔案內容就留在它的視窗，而不是你的 [S2]。

## 相關
- [[context-window]]、[[token-saving-tips]]、[[auto-memory]]
- 來源頁：[[s2-explore-context-window]]、[[s3-claude-code-memory]]
