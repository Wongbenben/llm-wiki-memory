# 教學頁大綱：AI 是怎麼「記憶」的？（節點 1 產出，待關卡 1 審核）

> 主線：AI 記住的東西，最後都要放進 context window（上下文視窗）才有用；放得越多，token 就耗得越多。
> 受眾：同班同學（用過 AI、懂一點 agent）。產生方式：只依 `wiki/index.md` 規劃。

| # | 標題 | 2–3 個重點 | 概念頁 | 表/圖 | 對應目標 |
|---|---|---|---|---|---|
| 1 | AI 的記憶其實只有一個地方：上下文視窗 | ① 視窗＝工作記憶，回應時只看得到裡面的東西 ② system prompt、訊息、工具結果、輸出全部都算 ③ 容量用 token 計，最多 1M | [[context-window]]、[[token]] | 圖：一個視窗方塊，裡面堆疊 system／指示檔／對話／檔案 | ① |
| 2 | 三種記憶一次看懂 | ① 對話內：視窗本身 ② 跨對話：聊天記憶、搜尋舊對話 ③ 外部檔案：CLAUDE.md、自動記憶 → 三者最後都要「被放進視窗」 | [[context-window]]、[[claude-chat-memory]]、[[search-past-chats]]、[[claude-md]]、[[auto-memory]] | 表：三種記憶 × 存在哪／誰寫／什麼時候進視窗 | ① |
| 3 | 為什麼越聊越貴、越容易忘 | ① 每輪重送全部歷史（累積）② token 越多準確度下降（context rot）③ 滿了就壓縮成摘要 | [[history-resend]]、[[context-rot]]、[[compaction]] | 圖：每輪輸入越疊越高的長條圖；表：壓縮前後 22,225 → 17,095 tokens | ② |
| 4 | Claude 實例 A：聊天 App 怎麼記住你 | ① 記憶存成一個個主題、專案各自分開 ② 搜尋舊對話用 RAG、以工具呼叫出現 ③ 不想被記：無痕／單次關記憶 | [[claude-chat-memory]]、[[search-past-chats]]、[[incognito-chat]] | 表：記憶 vs 搜尋 vs 無痕 | ③ |
| 5 | Claude 實例 B：Claude Code 的 CLAUDE.md 與自動記憶 | ① 每個 session 從空白開始 ② CLAUDE.md（你寫）vs 自動記憶（Claude 寫，只載 MEMORY.md 前 200 行）③ 開工前就吃掉的 token | [[claude-md]]、[[auto-memory]]、[[agents-md]] | 表：CLAUDE.md vs 自動記憶；圖：「還沒打字就載入」的 token 長條圖 | ③ |
| 6 | 彩蛋：省 token 小技巧 | ① /clear、/compact、子代理 ② CLAUDE.md 精簡 ③ prompt caching：重複前綴讀取約 0.1 倍價，但仍佔視窗 ＋ 做這頁花了多少 token | [[token-saving-tips]]、[[subagent-context]]、[[prompt-caching]] | 表：技巧清單；表：快取價格倍率 | ⑤ |

## 關卡 1 檢查表（人工勾選）
- [ ] ①②③⑤ 都有涵蓋（①→1,2　②→3　③→4,5　⑤→6）
- [ ] 每一節都對得到 index 裡的概念頁
- [ ] 不超過 6 節（目前 6 節）
