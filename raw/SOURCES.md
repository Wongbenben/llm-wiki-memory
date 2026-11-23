# 原始資料清單（全部是 Anthropic 官方文件）

請把每個網址的**全文**存成 markdown 放在 `raw/`（可以叫 agent 抓，或瀏覽器「另存」後貼上）。
存好之後，這個資料夾就不要再改了（規則 R1）。

| 代號 | 存成檔名 | 標題 | 網址 | 對應教學目標 |
|---|---|---|---|---|
| S1 | `s1-context-windows.md` | Context windows | https://platform.claude.com/docs/en/build-with-claude/context-windows | ① 三種記憶、② 越長越耗 |
| S2 | `s2-explore-context-window.md` | Explore the context window（Claude Code） | https://code.claude.com/docs/en/context-window | ② 越長越耗、⑤ 省 token |
| S3 | `s3-claude-code-memory.md` | How Claude remembers your project | https://code.claude.com/docs/en/memory | ③ Claude 實例 |
| S4 | `s4-chat-search-and-memory.md` | Use Claude's chat search and memory | https://support.claude.com/en/articles/11817273 | ① 三種記憶、③ Claude 實例 |
| S5 | `s5-prompt-caching.md` | Prompt caching | https://platform.claude.com/docs/en/build-with-claude/prompt-caching | ⑤ 省 token |

小提醒：S1、S3、S5 網址後面加 `.md` 可以直接拿到純文字版，例如
`https://code.claude.com/docs/en/memory.md`。

每份檔案最上面加三行：
```
來源: <網址>
抓取日期: 2026-11-23
代號: S1
```
