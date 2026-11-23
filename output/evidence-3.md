| # | 摘錄 | 來源 | 原文 |
|---|---|---|---|
| 1 | 之前的輪次完整保留 | S1 | each user message and assistant response accumulates within the context window, and previous turns are preserved completely |
| 2 | 變成下一輪輸入的一部分 | S1 | Generates a text response that becomes part of the input for the next turn |
| 3 | 第 1 次 | S5 | System + User(1) + Asst(1) + User(2) |
| 4 | 第 2 次 | S5 | System + User(1) + Asst(1) + User(2) + Asst(2) + User(3) |
| 5 | 第 3 次 | S5 | System + User(1) + Asst(1) + User(2) + Asst(2) + User(3) + Asst(3) + User(4) |
| 6 | 每送一則訊息都在花 token | S2 | costs tokens on every message |
| 7 | 這個現象叫 context rot | S1 | As token count grows, accuracy and recall degrade, a phenomenon known as context rot |
| 8 | 跟「視窗有多大」一樣重要 | S1 | This makes curating what's in context just as important as how much space is available |
| 9 | 擠掉你接下來真正需要的檔案 | S2 | Old conversation crowds out the files you need next |
| 10 | 超過視窗上限繼續進行 | S1 | Compaction automatically summarizes earlier parts of the conversation on the server, so the conversation can continue past the context window limit |
| 11 | 不會讓 session 結束 | S2 | Claude Code compacts automatically as you approach the limit, so a full context window doesn't end your session |
| 12 | 壓縮（/compact）之前 | S2 | 22,225 tokens are in use |
| 13 | 壓縮之後 | S2 | 17,095 tokens are in use |
| 14 | 對話摘要 | S2 | a 1,725-token conversation summary |
| 15 | 寫進 CLAUDE.md 才會在壓縮後保留 | S3 | Add conversation-only instructions to CLAUDE.md to make them persist |
