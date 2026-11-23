## 5. Claude 實例 B：Claude Code 的 CLAUDE.md 與自動記憶

每個 Claude Code session 都是從全新的上下文視窗開始 [S3]，所以要靠兩種「寫在檔案裡的記憶」把知識帶到下一次。

### 兩種檔案記憶
CLAUDE.md 是你寫給 Claude 的指示檔，Claude 在每個 session 開始時都會讀 [S3]。
自動記憶（auto memory）則是 Claude 根據你的更正和偏好，自己寫給自己的筆記 [S3]。

| | CLAUDE.md | 自動記憶 |
|---|---|---|
| 誰寫 | 你 [S3] | Claude [S3] |
| 內容 | 指示與規則 [S3] | 學到的東西與模式 [S3] |
| 什麼時候載入 | 每個 session [S3] | 只載入 MEMORY.md 的前 200 行或 25KB [S3] |
| 適合放 | 程式規範、工作流程、專案架構 [S3] | 你的偏好、你給過的更正 [S3] |

自動記憶的筆記分成四種：user、feedback、project、reference [S3]。
它用 MEMORY.md 當索引，細節寫在一個個主題檔；主題檔不會在啟動時載入，需要時才去讀 [S3]。
Claude 會把詳細筆記移到主題檔，讓 MEMORY.md 保持精簡 [S3]。

### 開工前就先吃掉的 token
你還沒打字之前，CLAUDE.md、自動記憶、MCP 工具名稱和 skill 說明就已經載入 context [S2]：

| 啟動時載入的東西 | token |
|---|---|
| System prompt | 4,200 [S2] |
| 專案 CLAUDE.md | 1,800 [S2] |
| 自動記憶 MEMORY.md | 680 [S2] |
| Skill 說明 | 450 [S2] |
| 使用者層級 ~/.claude/CLAUDE.md | 320 [S2] |
| 環境資訊 | 280 [S2] |
| MCP 工具名稱 | 120 [S2] |

> 圖：橫向長條圖，依上表由長到短排列。

### 寫 CLAUDE.md 的三個提醒
- 每個 CLAUDE.md 建議少於 200 行，越長越吃 context，也越不容易被遵守 [S3]。
- CLAUDE.md 是 context，不是強制設定；要強制擋住某個動作，要用 PreToolUse hook [S3]。
- 如果專案已經有 AGENTS.md，可以在 CLAUDE.md 裡匯入它，Claude 就會讀 CLAUDE.md 並透過匯入包含 AGENTS.md [S3]。
