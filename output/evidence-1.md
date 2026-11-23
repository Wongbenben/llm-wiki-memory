| # | 摘錄 | 來源 | 原文 |
|---|---|---|---|
| 1 | 包含它正在寫的回應本身 | S1 | refers to all the text a language model can reference when generating a response, including the response itself |
| 2 | 工作記憶（working memory） | S1 | This is different from the large corpus of data the language model was trained on, and instead represents a "working memory" for the model |
| 3 | 從沒出現在終端機畫面上的內容 | S2 | your instructions, the files it reads, its own responses, and content that never appears in your terminal |
| 4 | 通通都算進視窗 | S1 | Everything in the request counts toward the context window: the system prompt, every message in messages (including tool results, images, and documents), and your tool definitions |
| 5 | 包括 extended thinking | S1 | The output Claude generates for the turn, including its extended thinking, counts too |
| 6 | System prompt | S2 | System prompt \| 4,200 |
| 7 | 專案 CLAUDE.md | S2 | Project CLAUDE.md \| 1,800 |
| 8 | src/api/auth.ts | S2 | Read src/api/auth.ts \| 2,400 |
| 9 | 第一句 prompt | S2 | Your prompt \| 45 |
| 10 | 最多可以到 1M tokens | S1 | up to 1M tokens, depending on the model |
| 11 | 400 錯誤 | S1 | If the input alone already exceeds the model's context window, the API returns a 400 |
| 12 | context 越多不一定越好 | S1 | more context isn't automatically better |
| 13 | 就只有視窗裡的文字 | S1 | all the text a language model can reference when generating a response |
