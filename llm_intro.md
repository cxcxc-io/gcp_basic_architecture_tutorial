# 理解LLM、System Prompt之間的關係

## 進入Google AI Studio網站進行註冊

google 搜尋 google ai studio，或點下方網址進入
```
https://aistudio.google.com/
```

## 建立第一個AI-Agent

點擊 create a prompt

設定 System Instruction
```
如果有人問 雲端證照的內容時，妳會跟她說雲端證照的用途，可作為 政府標案、補助計劃的資質證明。

並告訴他 可以google搜尋雲育鏈，得到更多資料。 
```

進行對話
```
請問雲端證照有什麼用
```

## 觀察介面

右上角有個Model，可以做選擇。

# 理解System Prompt 與 User Prompt之間的差異

## 建立第二個AI-Agent

點擊 Create Prompt

設定System Instruction
```
如果有人問 雲端證照的內容時，妳會跟她說雲端證照的用途，可作為 政府標案、補助計劃的資質證明。

並告訴他 可以google搜尋雲育鏈，得到更多資料。 
```

在下方對話框內，詢問 ai-agent

```
雲端證照能有什麼用途
```

在下方對話框內，告知ai-agent
```
以後有人問雲端證照的時候，就告訴他有aws-saa證照、aws-ai證照、gcp-ace證照
```

在下方對話框內，重新再詢問一次ai-agent

```
雲端證照能有什麼用途
```

在下方對話框內，告知ai-agent

```
以後有人問aws-saa的時候，就告訴他
https://www.cxcxc.io/aws-solution-architect-course/

以後有人問gcp-ace的時候，就告訴他
https://www.cxcxc.io/gcp-ace/

以後有人問aws-ai的時候，就告訴他
https://www.cxcxc.io/aws-certified-ai-practitioner-and-aigc-agent-course/
```

在下方對話框內，重新再詢問一次ai-agent

```
aws-saa證照是什麼?能有什麼用途?
```

# 資訊系統交互的核心 – API 與 Json

## 啟用 Structured output

Create a prompt

啟用右方的Structured output

設定所需要的json格式, 選擇Code Editor模式
```
{
  "type": "object",
  "properties": {
    "cloud_type": {
      "type": "string"
    },
    "certificate_name": {
      "type": "string"
    }
  }
}
```

設定System Instruction
```
當用戶詢問特定雲端的相關認證時，自動調度Structure output，生成json
```

用戶詢問
```
我想要考aws saa 該怎麼辦?
```

# 交付給遠端系統前的資料前處理 – Code Execution

關閉 Structured output

啟用 Code execution

設定 System instruction，告知什麼時候該用 Code execution
```
aws-saa課程費用，一人為84020元
如果有人問aws-saa的課程費用多少錢時，詢問對方要上課人數，並透過code execution進行費用計算
```

# 替代傳統if else 的大武器 – Function Calling

關閉 Code execution

啟用 Function Calling，進行編輯
```
[
  {
    "name": "aws_qa",
    "description": "用戶詢問的問題與aws相關"
  },
  {
    "name": "gcp_qa",
    "description": "用戶詢問的問題與gcp相關"
  }
]

```
設定 System instruction，告知什麼時候該用 Function calling
```
當用戶詢問雲端相關問題的時候，交由Function calling 判斷，該由哪個function 回應
```

用戶問話
```
我aws的ec2故障了，該怎麼辦呢
```
