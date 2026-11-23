---
title: 每輪重送歷史（progressive token accumulation）
layer: token成本
sources: [S1, S2, S5]
---
> 白話：AI 不是真的「記得」上一句；每一輪都把之前的整段對話再送一次，所以越聊越長、越聊越貴。[S1]

## 是什麼
- 對話一輪一輪進行時，每則使用者訊息和助理回應都會累積在上下文視窗裡，之前的輪次完整保留 [S1]。
- 每一輪的輸入 = 之前所有對話歷史 + 這次的使用者訊息；這輪的輸出會成為下一輪輸入的一部分 [S1]。

## 怎麼運作
| 輪次 | 送進去的輸入 |
|---|---|
| 第 1 輪 | User(1) [S1] |
| 第 2 輪 | User(1) + Asst(1) + User(2) [S1] |
| 第 3 輪 | User(1) + Asst(1) + User(2) + Asst(2) + User(3) [S1] |

- claude.ai 這類聊天介面也可能用「先進先出」的滾動方式管理上下文視窗 [S1]。
- 在會保留 thinking 的模型上，保留下來的 thinking 區塊會成為之後請求的輸入，並以輸入 token 計費 [S1]。

## 跟 token 的關係
- 不相關的舊對話會擠掉你接下來需要的檔案，而且每則訊息都要花 token [S2]。
- Prompt caching 讓重複的前綴從快取讀，多輪對話中快取點會自動往前移 [S5]。
- 但快取的前綴仍然佔上下文視窗，快取改變的是付多少錢，不是算不算進去 [S1]。

## 相關
- [[context-window]]、[[token]]、[[prompt-caching]]、[[compaction]]
- 來源頁：[[s1-context-windows]]、[[s2-explore-context-window]]、[[s5-prompt-caching]]
