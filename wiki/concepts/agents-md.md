---
title: AGENTS.md（給各種 coding agent 的指示檔）
layer: 外部檔案記憶
sources: [S3]
---
> 白話：AGENTS.md 是給各家 AI 工具共用的說明書，Claude Code 也讀得懂，但有優先順序。[S3]

## 是什麼
- Claude Code 可以把 `AGENTS.md` 當成專案指示，所以已經為其他 coding agent 設定好的專案不用另外加 CLAUDE.md [S3]。

## 怎麼運作
| 專案裡有 | Claude 讀 |
|---|---|
| 只有 `AGENTS.md`，沒有 CLAUDE.md | `AGENTS.md` [S3] |
| `AGENTS.md` 和 CLAUDE.md 都有 | 只讀 CLAUDE.md [S3] |
| CLAUDE.md 匯入了 `AGENTS.md` | CLAUDE.md，並透過匯入包含 `AGENTS.md` [S3] |

## 跟 token 的關係
- 匯入的檔案會跟匯入它的 CLAUDE.md 一起載入，所以不會降低 context 成本 [S3]。

## 相關
- [[claude-md]]、[[auto-memory]]
- 來源頁：[[s3-claude-code-memory]]
