# 1. LLM Wiki 主題與規格介紹

## 主題
**AI 是怎麼「記憶」的？以 Claude 為例，順便看 token 怎麼被吃掉**

主線一句話：
> AI 記住的東西，最後都要放進 context window（上下文視窗）才有用；放得越多，token 就耗得越多。

## 受眾與教學目標
- 受眾：同班同學（用過 AI、懂一點 agent）
- 看完教學頁之後，同學應該能：
  1. 說出 AI 的三種記憶：對話內、跨對話、外部檔案，各有什麼差別
  2. 解釋為什麼對話越長，token 越耗、AI 越容易忘記前面的內容
  3. 看懂 Claude 實際怎麼記：聊天記憶、CLAUDE.md、自動記憶
  4. （彩蛋）會用幾招省 token

## 資料來源（raw，共 5 份，全部是 Anthropic 官方文件）
| 代號 | 資料 | 用途 |
|---|---|---|
| S1 | Context windows | 工作記憶的定義、context rot、每輪累積 |
| S2 | Explore the context window（Claude Code） | token 被什麼吃掉、省 token 建議 |
| S3 | How Claude remembers your project | CLAUDE.md、自動記憶 |
| S4 | Claude chat search and memory | 聊天版的跨對話記憶 |
| S5 | Prompt caching | 快取省成本 |

## Wiki 結構
```
raw/              原始資料（唯讀）
wiki/
  concepts/       概念頁（一頁一個概念）
  sources/        每份資料的摘要
  index.md        目錄（照三層記憶＋token 成本排）
  log.md          操作紀錄
output/           大綱、各節內容、index.html
AGENTS.md         規則檔（7 條）
```

## 規則檔重點（AGENTS.md）
| 規則 | 內容 |
|---|---|
| R1 | raw/ 唯讀 |
| R3 | 每個事實標 [S#] |
| R4 | 改了就更新 index、寫 log |
| R5 | [[連結]] 每頁至少 2 個；檔名英文小寫加連字號 |
| R6 | 繁體中文，術語附英文 |
| R7 | 沒寫的不准補，不確定標（待查） |
| R8 | 每頁第一行放白話摘要 |

## 工作流程
採用 **Graph 套 Loop**：3 個檢查關卡，其中 2 個是有次數上限的 loop。詳見 `04-flow.md`。
另外全程記錄 token 用量（`05-token-log.md`），把作業本身當成「token 怎麼耗」的實際案例。
