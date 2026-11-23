---
title: Claude 聊天記憶（memory）
layer: 跨對話記憶
sources: [S4]
---
> 白話：Claude App 會把你聊過的重要事情記成一個個主題，下次開新對話它也知道。[S4]

## 是什麼
- Claude 可以根據你的聊天產生記憶，讓它從無狀態（stateless）的聊天介面，變成隨時間累積理解的合作者 [S4]。
- Free、Pro、Max、Ultra 方案在網頁、Claude Desktop、Claude Mobile 上，記憶預設是開的 [S4]。

## 怎麼運作
- Claude 在聊天過程中把記憶存成一組個別主題，而不是等對話結束後才做摘要 [S4]。
- Claude 會自己決定要存什麼，你也可以說「remember this」直接叫它存 [S4]。
- 每個專案（project）有自己的記憶；在專案裡，Claude 會用專案記憶加上專案外的聊天記憶，但不會用其他專案的記憶 [S4]。
- 會記的內容包括：你的角色與專案、工作與生活中的人和地方、溝通偏好、技術偏好、進行中的工作 [S4]。
- 預設不存健康、種族、宗教、政治等敏感主題，除非你自己開啟 [S4]。
- 政府身分證號、犯罪紀錄、金融帳號、移民身分，就算你要求也不會存 [S4]。
- 在 設定 > Your Claude 可以查看每個主題，並編輯或刪除 [S4]。

## 跟 token 的關係
- 記憶內容放進對話時會佔用多少 token，S4 沒有說明（待查）。

## 相關
- [[search-past-chats]]、[[incognito-chat]]、[[auto-memory]]
- 來源頁：[[s4-chat-search-and-memory]]
