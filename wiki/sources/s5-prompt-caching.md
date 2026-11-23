---
title: S5 Prompt caching（提示快取）
source: https://platform.claude.com/docs/en/build-with-claude/prompt-caching
---
> 白話：每輪都要重送的開頭內容，如果沒有變，就從快取拿，又便宜又快。[S5]

## 重點
- 系統會檢查 prompt 前綴（到快取斷點為止）最近是否已快取；有就使用快取版本，減少處理時間和成本 [S5]。
- 快取涵蓋完整前綴：`tools`、`system`、`messages`，依這個順序 [S5]。
- 預設快取壽命 5 分鐘，每次使用都會免費刷新；也可以付額外費用用 1 小時 [S5]。
- 價格倍率：5 分鐘寫入 1.25 倍、1 小時寫入 2 倍、讀取 0.1 倍基本輸入價（部分模型例外）[S5]。
- 多輪對話用自動快取時，快取點會自動往前移，前面的內容從快取讀 [S5]。
- 改到 tools → system → messages 某一層，該層和後面全部失效 [S5]。
- 太短的 prompt 不能快取，而且不會回傳錯誤 [S5]。

## 對應概念頁
[[prompt-caching]]、[[history-resend]]、[[token]]、[[token-saving-tips]]
