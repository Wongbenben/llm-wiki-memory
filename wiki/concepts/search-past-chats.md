---
title: 搜尋過去對話（search past chats）
layer: 跨對話記憶
sources: [S4, S1]
---
> 白話：叫 Claude 去翻舊對話，把你們之前聊過的東西找回來。[S4]

## 是什麼
- 你可以請 Claude 搜尋過去的對話，找到相關資訊並引用細節 [S4]。
- 這個功能開放給付費方案（Pro、Max、Ultra、Team、Enterprise），在網頁、桌面、手機 App 都能用 [S4]。

## 怎麼運作
- 搜尋使用檢索增強生成（Retrieval-Augmented Generation，RAG），在對話中會以工具呼叫（tool call）的形式出現 [S4]。
- 可搜尋範圍：專案外的所有聊天；專案內的對話只能在該專案內搜尋 [S4]。
- Claude 引用舊對話時，會附上連回原對話的引用 [S4]。
- 可以在設定裡關掉「Search and reference chats」[S4]。

## 跟 token 的關係
- 搜尋的結果以工具呼叫的形式進到目前的對話 [S4]，而工具結果都會算進上下文視窗 [S1]。

## 相關
- [[claude-chat-memory]]、[[incognito-chat]]、[[context-window]]
- 來源頁：[[s1-context-windows]]、[[s4-chat-search-and-memory]]
