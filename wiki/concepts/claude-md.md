---
title: CLAUDE.md（專案指示檔）
layer: 外部檔案記憶
sources: [S3, S2]
---
> 白話：你寫給 Claude Code 的「專案說明書」，每次開新 session 它都會先讀。[S3]

## 是什麼
- 每個 Claude Code session 都從全新的上下文視窗開始，CLAUDE.md 和自動記憶負責把知識帶到下一個 session [S3]。
- CLAUDE.md 是你用純文字寫的 markdown 檔，給 Claude 持續性的指示，Claude 每個 session 開始時都會讀 [S3]。
- 可以放在不同層級：組織政策、使用者（`~/.claude/CLAUDE.md`）、專案（`./CLAUDE.md`）、本機（`./CLAUDE.local.md`）[S3]。

## 怎麼運作
- 工作目錄以及它上層的 CLAUDE.md 會在啟動時載入，子目錄的則在需要時才載入 [S3]。
- 找到的多個 CLAUDE.md 會串接起來放進 context，不會互相覆蓋 [S3]。
- Claude 把 CLAUDE.md 當成 context，不是強制設定；要強制擋住某個動作，要用 PreToolUse hook [S3]。
- 適合加進 CLAUDE.md 的時機：Claude 第二次犯同樣的錯，或你又打了一次上次打過的更正 [S3]。

## 跟 token 的關係
- 建議每個 CLAUDE.md 少於 200 行；越長越吃 context，也越不容易被遵守 [S3]。
- `@path` 匯入只能幫忙整理，不會降低 context 成本，因為被匯入的檔案會一起載入 [S3]。
- 區塊級 HTML 註解會在注入 context 前被移除，可以留備註給人看而不花 context token [S3]。
- 範例 session 中，專案 CLAUDE.md 佔 1,800 tokens [S2]。

## 相關
- [[auto-memory]]、[[agents-md]]、[[compaction]]、[[context-window]]
- 來源頁：[[s2-explore-context-window]]、[[s3-claude-code-memory]]
