---
title: S2 Explore the context window（Claude Code）
source: https://code.claude.com/docs/en/context-window
---
> 白話：這份文件用一個範例 session，逐步列出 Claude Code 的 context 被什麼東西吃掉、各吃多少 token。[S2]

## 重點
- 你還沒打字前，CLAUDE.md、自動記憶、MCP 工具名稱、skill 說明就已載入 context [S2]。
- Claude 工作時，每讀一個檔案都會加進 context [S2]。
- 子代理（subagent）在自己的獨立視窗做研究，只把摘要和一小段 metadata 帶回來 [S2]。
- 範例 session：`/compact` 前用了 22,225 tokens，之後剩 17,095 tokens；子代理另外在自己的視窗用了 9,890 tokens [S2]。
- 壓縮後，專案根目錄 CLAUDE.md 和自動記憶會從磁碟重新注入 [S2]。
- 省 context 的做法：`/compact` 指定重點、`/clear` 換任務、把大量閱讀交給子代理、用 `/context` 看用量 [S2]。

## 對應概念頁
[[context-window]]、[[compaction]]、[[subagent-context]]、[[claude-md]]、[[auto-memory]]、[[token]]、[[token-saving-tips]]
