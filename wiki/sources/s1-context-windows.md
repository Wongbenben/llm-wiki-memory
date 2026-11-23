---
title: S1 Context windows（上下文視窗）
source: https://platform.claude.com/docs/en/build-with-claude/context-windows
---
> 白話：這份官方文件說明 AI 的「工作記憶」怎麼運作，以及對話為什麼會越長越佔空間。[S1]

## 重點
- 上下文視窗（context window）是模型產生回應時能參考的所有文字，包含回應本身，是模型的「工作記憶（working memory）」[S1]。
- token 數越多，準確度和回想能力會下降，這叫 context rot [S1]。
- 每一輪的輸入 = 之前所有對話歷史 + 這次的使用者訊息；輸出會變成下一輪輸入的一部分 [S1]。
- system prompt、所有訊息（含工具結果、圖片、文件）、工具定義、這輪的輸出（含 thinking）全部都算進視窗 [S1]。
- 視窗最大可到 1M tokens，依模型而定 [S1]。
- 對話常常接近上限時，可用伺服器端壓縮（server-side compaction）自動摘要較早的內容 [S1]。
- 快取的前綴仍然佔視窗；prompt caching 改變的是付多少錢，不是算不算進視窗 [S1]。

## 對應概念頁
[[context-window]]、[[context-rot]]、[[history-resend]]、[[compaction]]、[[token]]、[[prompt-caching]]
