# Log（只能往後加）

格式：`## [YYYY-MM-DD HH:MM] 動作 | 對象 | 做了什麼 | 約用 token`

## [2026-11-23 15:00] init | 全部 | 建立資料夾骨架、AGENTS.md、index.md | -

## [2026-11-23 14:45] ingest | raw/ S1–S5 | 抓 5 份官方文件存進 raw/（S1/S2/S3/S5 用 .md 純文字版；S4 是 HTML，轉成文字），每份加上來源/日期/代號三行 | 約 3k（估算）
## [2026-11-23 14:50] ingest | S1 | 新增 sources/s1-context-windows.md；新增 concepts/context-window、context-rot、history-resend；概念清單由 agent 列出後直接採用（使用者指示「開始作業」，未逐份停下確認） | 約 7k（估算：raw 約 16k 字元＋寫頁）
## [2026-11-23 14:55] ingest | S2 | 新增 sources/s2-explore-context-window.md；新增 concepts/compaction、subagent-context、token；context-window 補 Claude Code 的說法 | 約 6k（估算：raw 約 11k 字元＋寫頁）
## [2026-11-23 15:00] ingest | S3 | 新增 sources/s3-claude-code-memory.md；新增 concepts/claude-md、auto-memory、agents-md；compaction 補「指示要寫進 CLAUDE.md 才不會被壓縮掉」 | 約 12k（估算：只讀相關章節約 30k 字元）
## [2026-11-23 15:05] ingest | S4 | 新增 sources/s4-chat-search-and-memory.md；新增 concepts/claude-chat-memory、search-past-chats、incognito-chat | 約 10k（估算：raw 約 30k 字元）
## [2026-11-23 15:10] ingest | S5 | 新增 sources/s5-prompt-caching.md；新增 concepts/prompt-caching、token-saving-tips；history-resend 補快取點自動往前移 | 約 12k（估算：S5 全文 155k 字元，只讀說明段落約 35k，範例程式碼沒讀）
## [2026-11-23 15:15] lint | wiki 全部 | 第1輪（scripts/lint_wiki.py）：孤兒頁 5（sources 只有 index 連過來）、（待查）2 → 修正：每個概念頁加「來源頁」連結 | 約 2k
## [2026-11-23 15:17] lint | wiki 全部 | 第2輪：剩（待查）2 筆，資料沒寫、依 R7 保留不補：① claude-chat-memory「記憶佔多少 token」② token「文字怎麼切成 token」；這兩句不會用進教學頁 | 約 1k
## [2026-11-23 14:53] check | wiki/log.md | 更正：上面 ingest/lint 八筆的時間是 agent 預填的，不是實際時間。實際上 raw 抓取約 14:40，S1–S5 ingest 在 14:50–14:51 寫入，lint 兩輪在 14:51–14:52。log 只能往後加，所以用這筆更正、不改舊紀錄 | -
## [2026-11-23 14:53] query | outline | 節點1：依 index.md 產出 output/outline.md（6 節）。註：同一個 session 剛 ingest 完，context 裡已經有全部概念頁，所以「只讀 index」這次沒有真的省到 token | 約 2k
## [2026-11-23 15:00] check | outline | 關卡1 通過（使用者回覆「OK，進下一步」） | -
## [2026-11-23 14:55] check | wiki/log.md | 更正：上一筆「關卡1 通過」實際時間是 14:55，不是 15:00。之後一律用系統時間自動填 | -
## [2026-11-23 14:55] check | section-1 | 關卡2 第1輪 FAIL：1 句漏標來源（「換句話說，AI 只看得到視窗裡的東西」是自己加的轉述）| 約 3k
## [2026-11-23 14:55] check | section-1 | 關卡2 第2輪 PASS（13 列證據都在 raw 找得到原文）| 約 1k
## [2026-11-23 14:56] check | section-2 | 關卡2 第1輪 FAIL：①#6 證據原文多抄了 S2 的粗體標題，比對不到 ② 開頭「三種記憶最後都要放進視窗」是自己的總結、沒有來源 → 刪掉該句（重點留在小標）、修正原文 | 約 3k
## [2026-11-23 14:56] check | section-2 | 關卡2 第2輪 PASS（11 列）| 約 1k
## [2026-11-23 14:56] check | section-3 | 關卡2 第1輪 FAIL：#12、#13 證據原文裡的 /compact 在 S2 有程式碼標記，比對不到 → 改成只抄數字那段 | 約 3k
## [2026-11-23 14:56] check | section-3 | 關卡2 第2輪 PASS（15 列）| 約 1k
## [2026-11-23 14:56] check | section-4 | 關卡2 第1輪 FAIL：證據 #10 的摘錄裡有「|」，把表格欄位切壞，來源代號讀不到 → 改摘錄；另把圖說標成（示意），避免被當成事實 | 約 3k
## [2026-11-23 14:57] check | section-4 | 關卡2 第2輪 PASS（16 列）。註：第一次用 sed 修證據檔時 \| 被當成正規表達式的「或」，把每一列都改壞，改用 Python 修回 | 約 2k
## [2026-11-23 14:57] check | section-4 | 補記：上一筆 PASS 時證據檔第 10 列仍是壞的（實際 15 列有效），已修好重跑，16 列 PASS | -
## [2026-11-23 14:57] check | scripts/check_sources.py | 改檢查器：markdown 的 * 和 ` 改成直接刪掉（原本換成空白，造成「/compact ,」這種比對失敗）。改完重跑 section-1～4 都仍 PASS。這是格式正規化，沒有放寬內容比對 | 約 1k
## [2026-11-23 14:58] check | section-5 | 關卡2 第1輪 FAIL：①證據 #6 摘錄又含「|」（同 section-4 的錯）②表格前的引導句沒標來源 ③人工複查發現：檢查器沒抓到的錯——「和本作業的 Wiki 是同一個思路」標了 [S3]，但 S3 沒講這件事（摘錄對得上、意思對不上）→ 刪掉這半句 | 約 3k
## [2026-11-23 14:58] check | section-5 | 關卡2 第2輪 PASS（21 列）。另外人工複讀 section-1～4 的語意，沒有發現類似「摘錄對、意思錯」的句子 | 約 2k
## [2026-11-23 14:58] check | section-6 | 關卡2 第1輪 FAIL：①開頭總結句沒來源 ②人工複查：「知道 token 花在哪才知道要砍什麼」是自己加的推論；「讀取 0.1 倍」漏了 S5 註腳的例外（Opus 5.5、Sonnet 5.5 是 0.05 倍）→ 都改成照原文 | 約 3k
## [2026-11-23 14:58] check | section-6 | 關卡2 第2輪 PASS（23 列）| 約 1k
## [2026-11-23 15:01] check | output/index.html | 關卡3 第1輪 FAIL：375px 下頁面沒有橫向爆版、6 節都有表或圖、103 個 [S#] 連結都點得到；但 ①SVG 圖跟著縮小，圖 3 的字只剩約 7px 看不清 ②表格、圖說、附註字體 14–15.5px，低於規定的 16px → 圖改成最小寬度＋框內左右滑、字體全部拉到 16px 以上 | 約 4k
## [2026-11-23 15:02] check | output/index.html | 關卡3 第2輪 PASS：375px 下無橫向爆版、p/td/li/圖說全部 ≥16px、SVG 最小字約 11px（原本 6px）、103 個 [S#] 連結都點得到、6 節都有表＋圖。另跑一致性檢查：HTML 文字和 section-1～6 完全一致 | 約 3k
## [2026-11-23 15:04] check | docs | 填完 05-token-log、04-flow（v2 修改）、06-reflection；更新 flow.dot 與 prompts/02-section-loop.md（v2）。flow.png 沒有重新產生（這台電腦沒有 Graphviz）| 約 6k
## [2026-11-23 15:19] publish | 全部 | 上傳到 GitHub（Wongbenben/llm-wiki-memory）：git push 兩次都卡在登入視窗，改用網頁上傳 59 個檔（少 3 個空的 .gitkeep）；開 GitHub Pages（main / root）。用 375px 檢查線上版：6 節、5 張圖、103 個 [S#] 連結正常、無橫向爆版。教學頁：https://wongbenben.github.io/llm-wiki-memory/output/ | 約 3k
