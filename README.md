# LLM Wiki 作業工具包：AI 怎麼記憶 & Token 怎麼耗

## 開跑順序（預估 2–3 小時）
| # | 做什麼 | 用哪個檔 | 產出 |
|---|---|---|---|
| 0 | 用 Antigravity / Claude Code 開這個資料夾 | `AGENTS.md`（Claude Code 透過 `CLAUDE.md` 讀它） | - |
| 1 | 抓 5 份官方資料存進 `raw/` | `raw/SOURCES.md` | raw/s1～s5 |
| 2 | Ingest ×5，再跑 Lint | `prompts/00-ingest.md` | wiki/ 全部頁面 |
| 3 | 用 Obsidian 開 `wiki/`，截 graph view | - | **繳交 #2 截圖** |
| 4 | 產大綱＋關卡1 | `prompts/01-outline.md` | output/outline.md |
| 5 | 逐節寫＋關卡2 loop | `prompts/02-section-loop.md` | output/section-N.md |
| 6 | 組 HTML＋關卡3 loop | `prompts/03-assemble-html.md` | output/index.html |
| 7 | 上傳 GitHub Pages（或其他網頁空間）拿連結 | - | **繳交 #3 連結** |
| 8 | 填反思 | `docs/06-reflection.md` | **繳交 #6** |

全程把每一步填進 `docs/05-token-log.md`，並記進 `wiki/log.md` → **繳交 #5**。

## 繳交 6 項對照
| # | 項目 | 對應檔案 |
|---|---|---|
| 1 | 主題與規格介紹 | `docs/01-spec.md` |
| 2 | Wiki 資料夾或截圖 | `wiki/` ＋ Obsidian 截圖 |
| 3 | 教學 HTML 連結 | `output/index.html` 上線後的網址 |
| 4 | loop/graph 流程圖 | `docs/flow.png` ＋ `docs/04-flow.md` |
| 5 | 實際執行紀錄 | `docs/05-token-log.md` ＋ `wiki/log.md` ＋ 截圖 |
| 6 | 反思 | `docs/06-reflection.md` |

## 衝滿分的小提醒
- 截圖要拍到：Obsidian graph、關卡2 的 FAIL→PASS 過程、手機寬度的 HTML
- 反思一定要引用 log 的實際數字（FAIL 幾次、token 多少）
- 教學頁彩蛋可以放你自己的 token 數據：「做這頁本身花了多少 token」
