# Index — AI 怎麼記憶 & Token 怎麼耗

> 白話：這是 Wiki 的目錄。AI 查資料時先看這頁，再打開需要的頁面。

## 1. 對話內記憶
- [[context-window]] — 上下文視窗：模型的工作記憶，所有東西都要放進來才算數 [S1][S2]
- [[context-rot]] — 上下文腐化：token 越多，準確度與回想能力下降 [S1]
- [[compaction]] — 壓縮：把舊對話濃縮成摘要以繼續對話 [S1][S2]
- [[subagent-context]] — 子代理的獨立視窗：大量閱讀不進主視窗 [S2]

## 2. 跨對話記憶
- [[claude-chat-memory]] — Claude App 把重要資訊存成主題，帶到新對話 [S4]
- [[search-past-chats]] — 用 RAG 搜尋過去對話 [S4]
- [[incognito-chat]] — 無痕聊天與單次關閉記憶 [S4]

## 3. 外部檔案記憶
- [[claude-md]] — 你寫給 Claude Code 的專案指示，每個 session 載入 [S3]
- [[auto-memory]] — Claude Code 自己寫的筆記，啟動時載入 MEMORY.md 索引 [S3]
- [[agents-md]] — 跨工具共用的指示檔與 CLAUDE.md 的優先順序 [S3]

## 4. Token 成本
- [[token]] — 計量單位、usage 欄位、範例用量 [S1][S2][S5]
- [[history-resend]] — 每輪都重送之前的歷史，越聊越長 [S1]
- [[prompt-caching]] — 重複前綴從快取讀，讀取約 0.1 倍價格 [S5]
- [[token-saving-tips]] — 省 token 小技巧 [S2][S3][S5]

## 5. 來源
- [[s1-context-windows]] · [[s2-explore-context-window]] · [[s3-claude-code-memory]] · [[s4-chat-search-and-memory]] · [[s5-prompt-caching]]
