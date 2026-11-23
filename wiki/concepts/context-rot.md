---
title: 上下文腐化（context rot）
layer: 對話內記憶
sources: [S1, S2, S3]
---
> 白話：塞進去的東西越多，AI 反而越抓不到重點，像是「忘記」前面講過的事。[S1]

## 是什麼
- 隨著 token 數增加，模型的準確度和回想能力（recall）會下降，這個現象叫 context rot [S1]。

## 怎麼運作
- 因此「挑選放進 context 的內容」跟「有多少空間」一樣重要 [S1]。
- 舊的對話會擠掉你接下來需要的檔案，而且每則訊息都要花 token [S2]。
- CLAUDE.md 超過 200 行會消耗更多 context，並降低 Claude 遵守指示的程度 [S3]。

## 跟 token 的關係
- 減少 context rot 的做法也同時省 token，例如換任務時用 `/clear`、把大量閱讀交給子代理 [S2]。

## 相關
- [[context-window]]、[[compaction]]、[[subagent-context]]、[[token-saving-tips]]
- 來源頁：[[s1-context-windows]]、[[s2-explore-context-window]]、[[s3-claude-code-memory]]
