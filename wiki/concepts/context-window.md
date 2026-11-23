---
title: 上下文視窗（context window）
layer: 對話內記憶
sources: [S1, S2]
---
> 白話：AI 這一輪「看得到」的所有文字就是它的工作記憶；沒放進來的，它就不知道。[S1]

## 是什麼
- 上下文視窗是語言模型產生回應時能參考的所有文字，包含回應本身 [S1]。
- 它不是模型訓練時用的大量資料，而是模型的「工作記憶（working memory）」[S1]。
- 在 Claude Code 裡，上下文視窗裝著 Claude 對這個 session 知道的一切：你的指示、它讀過的檔案、它自己的回應，以及從沒出現在終端機上的內容 [S2]。

## 怎麼運作
- 每一輪分成輸入與輸出：輸入包含之前所有對話歷史加上這次的使用者訊息，輸出產生的回應會成為下一輪輸入的一部分 [S1]。
- 請求裡的所有東西都算進視窗：system prompt、`messages` 裡每則訊息（含工具結果、圖片、文件）、工具定義，以及這一輪的輸出（含 extended thinking）[S1]。
- 在 Claude Code 中，你還沒打字之前，CLAUDE.md、自動記憶、MCP 工具名稱和 skill 說明就已經載入 context [S2]。

## 跟 token 的關係
- 視窗容量依模型最多可到 1M tokens [S1]。
- 如果輸入本身就超過視窗，API 會回傳 400 錯誤（"prompt is too long"）[S1]。
- 視窗越大可以處理越長的提示，但 context 越多不一定越好 [S1]，見 [[context-rot]]。

## 相關
- [[token]]、[[context-rot]]、[[history-resend]]、[[compaction]]
- 來源頁：[[s1-context-windows]]、[[s2-explore-context-window]]
