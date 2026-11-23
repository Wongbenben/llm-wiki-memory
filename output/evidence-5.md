| # | 摘錄 | 來源 | 原文 |
|---|---|---|---|
| 1 | 全新的上下文視窗開始 | S3 | Each Claude Code session begins with a fresh context window |
| 2 | 每個 session 開始時都會讀 | S3 | Claude reads them at the start of every session |
| 3 | 自己寫給自己的筆記 | S3 | notes Claude writes itself based on your corrections and preferences |
| 4 | 誰寫 | S3 | Who writes it \| You \| Claude |
| 5 | 指示與規則 | S3 | What it contains \| Instructions and rules \| Learnings and patterns |
| 6 | 只載入 MEMORY.md | S3 | Every session \| Sessions with auto memory on, up to the first 200 lines or 25KB of MEMORY.md |
| 7 | 程式規範 | S3 | Coding standards, workflows, project architecture \| Your preferences, corrections you give Claude |
| 8 | 分成四種 | S3 | Claude saves four kinds of notes for itself |
| 9 | 主題檔不會在啟動時載入 | S3 | Claude Code doesn't load topic files such as user_role.md or feedback_testing.md at startup |
| 10 | 讓 MEMORY.md 保持精簡 | S3 | Claude keeps MEMORY.md concise by moving detailed notes into separate topic files |
| 11 | System prompt | S2 | System prompt \| 4,200 |
| 12 | 專案 CLAUDE.md | S2 | Project CLAUDE.md \| 1,800 |
| 13 | 自動記憶 MEMORY.md | S2 | Auto memory (MEMORY.md) \| 680 |
| 14 | Skill 說明 | S2 | Skill descriptions \| 450 |
| 15 | 使用者層級 | S2 | ~/.claude/CLAUDE.md \| 320 |
| 16 | 環境資訊 | S2 | Environment info \| 280 |
| 17 | MCP 工具名稱 | S2 | MCP tool names \| 120 |
| 18 | 少於 200 行 | S3 | target under 200 lines per CLAUDE.md file. Longer files consume more context and reduce adherence |
| 19 | PreToolUse hook | S3 | They aren't enforced configuration. To block an action regardless of what Claude decides, use a PreToolUse hook instead |
| 20 | 透過匯入包含 AGENTS.md | S3 | with AGENTS.md included through the import |
| 21 | 你還沒打字之前 | S2 | Before you type anything: CLAUDE.md, auto memory, MCP tool names, and skill descriptions all load into context |
