| # | 摘錄 | 來源 | 原文 |
|---|---|---|---|
| 1 | 跑 /clear | S2 | run /clear when switching to unrelated work |
| 2 | 每則訊息都在花 token | S2 | Old conversation crowds out the files you need next and costs tokens on every message |
| 3 | 開始長任務前 | S2 | run /compact with instructions, like /compact focus on the auth bug fix, before starting a long new task |
| 4 | 讓自動壓縮去猜 | S2 | The summary keeps what you choose instead of what the automatic pass guesses is important |
| 5 | 把研究交給子代理 | S2 | Delegate large reads: send research to a subagent |
| 6 | 不在你的視窗 | S2 | so the file contents stay in its context window, not yours |
| 7 | 跑 /context | S2 | run /context for a live breakdown by category with optimization suggestions |
| 8 | 看到實際的 context 用量 | S2 | To see your actual context usage at any point, run /context for a live breakdown by category with optimization suggestions |
| 9 | 搬到 path-scoped rules | S3 | Move instructions that matter for only part of the codebase into path-scoped rules |
| 10 | 處理相關檔案時才載入 | S3 | which load only when Claude works with matching files |
| 11 | 寫給人看的備註 | S3 | Block-level HTML comments |
| 12 | 不會花到 context token | S3 | Use them to leave notes for human maintainers without spending context tokens on them |
| 13 | 減少處理時間和成本 | S5 | If found, it uses the cached version, reducing processing time and costs |
| 14 | 免費刷新 | S5 | By default, the cache has a 5-minute lifetime. The cache is refreshed for no additional cost each time the cached content is used |
| 15 | 快取點會隨著對話自動往前移 | S5 | With automatic caching, the cache point moves forward automatically as conversations grow |
| 16 | 寫入快取（5 分鐘） | S5 | Cache write tokens with a 5-minute TTL are 1.25 times the base input tokens price |
| 17 | 寫入快取（1 小時） | S5 | Cache write tokens with a 1-hour TTL are 2 times the base input tokens price |
| 18 | 從快取讀取 | S5 | Cache read tokens are 0.1 times the base input tokens price |
| 19 | 放在 prompt 開頭 | S5 | Place cached content at the prompt's beginning for best performance |
| 20 | 整個快取失效 | S5 | Modifying tool definitions (names, descriptions, parameters) invalidates the entire cache |
| 21 | 不會讓這些 token 不算進 | S1 | prompt caching changes what you pay for those tokens, not whether they count |
| 22 | 跟視窗有多大一樣重要 | S1 | This makes curating what's in context just as important as how much space is available |
| 23 | 是 0.05 倍 | S5 | Cache hits and refreshes on Claude Opus 5.5 and Claude Sonnet 5.5 are priced at 0.05x the base input price |
