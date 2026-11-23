---
title: 自動記憶（auto memory）
layer: 外部檔案記憶
sources: [S3, S2]
---
> 白話：Claude Code 會自己記筆記——你糾正過它的事、你的偏好，下次開新 session 就記得。[S3]

## 是什麼
- 自動記憶讓 Claude 不需要你寫任何東西，就能跨 session 累積知識 [S3]。
- 筆記分四種：`user`（你的角色與偏好）、`feedback`（你的更正）、`project`（進行中的工作與決定）、`reference`（外部資訊在哪裡）[S3]。
- Claude 會跳過能從程式碼推得的東西，以及 CLAUDE.md 已經寫過的東西 [S3]。

| | CLAUDE.md | 自動記憶 |
|---|---|---|
| 誰寫 | 你 [S3] | Claude [S3] |
| 內容 | 指示與規則 [S3] | 學到的東西與模式 [S3] |
| 載入 | 每個 session [S3] | 開啟時載入 `MEMORY.md` 前 200 行或 25KB [S3] |

## 怎麼運作
- 存放在 `~/.claude/projects/<project>/memory/`，裡面有一個 `MEMORY.md` 索引，加上每個記憶一個主題檔 [S3]。
- session 開始時只載入 `MEMORY.md` 的前 200 行或 25KB（先到者為準）[S3]。
- 主題檔不會在啟動時載入，Claude 需要時才用檔案工具去讀 [S3]。
- 自動記憶只存在本機，不會跨機器共享 [S3]。
- 本機 session 預設開啟，可以用 `/memory` 切換 [S3]。

## 跟 token 的關係
- Claude 會把細節移到主題檔，讓 `MEMORY.md` 保持精簡 [S3]。
- 範例 session 中，`MEMORY.md` 佔 680 tokens [S2]。
- 壓縮後，自動記憶會從磁碟重新注入 [S2]。

## 相關
- [[claude-md]]、[[claude-chat-memory]]、[[compaction]]、[[subagent-context]]
- 來源頁：[[s2-explore-context-window]]、[[s3-claude-code-memory]]
