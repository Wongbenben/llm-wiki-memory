---
title: S3 How Claude remembers your project（Claude Code 記憶）
source: https://code.claude.com/docs/en/memory
---
> 白話：Claude Code 每次開新 session 都從空白開始，靠 CLAUDE.md（你寫的）和自動記憶（它自己寫的）把知識帶到下一次。[S3]

## 重點
- 每個 Claude Code session 都從全新的上下文視窗開始 [S3]。
- CLAUDE.md 是你寫的指示，每個 session 都載入；自動記憶是 Claude 根據你的更正與偏好自己寫的筆記 [S3]。
- CLAUDE.md 建議少於 200 行，越長越吃 context、遵守度越低 [S3]。
- `@import` 只是整理用，不會降低 context 成本 [S3]。
- 自動記憶存在 `~/.claude/projects/<project>/memory/`，啟動時只載入 `MEMORY.md` 的前 200 行或 25KB [S3]。
- 自動記憶有四種類型：user、feedback、project、reference [S3]。
- Claude Code 可以讀 AGENTS.md；但如果同時有 CLAUDE.md，預設只讀 CLAUDE.md，除非 CLAUDE.md 匯入了 AGENTS.md [S3]。
- CLAUDE.md 是 context，不是強制設定；要強制擋住某個動作要用 PreToolUse hook [S3]。

## 對應概念頁
[[claude-md]]、[[auto-memory]]、[[agents-md]]、[[compaction]]、[[subagent-context]]
