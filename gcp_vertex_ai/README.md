# GCP Vertex AI Chat Application

這個專案是一個簡單的 Flask 應用程式，允許用戶與 Vertex AI 的生成式模型進行對話，並可以上傳圖片進行處理。圖片會被儲存到 Google Cloud Storage 中。

## 專案結構

```

GCP_VERTEX_AI/ 
├── templates/ 
│ └── index.html # 前端 HTML 頁面 
├── uploads/ # 用於本地存儲上傳文件的資料夾 
├── app.py # Flask 應用程式主程式碼 
├── Dockerfile # Docker 建置設定 
├── README.md # 專案說明文件 
└── requirements.txt # Python 套件需求

```


## 環境變數
應用程式使用以下環境變數來配置：
- `CLOUD_STORAGE_BUCKET`: 用於指定儲存圖片的 Google Cloud Storage bucket 名稱。
- `MODEL_NAME`: 指定 Vertex AI 模型的名稱，預設為 `gemini-1.5-flash-002`。


## 在cloud shell editor 使用方式

### 1. 設定Project、安裝必要套件


首先點擊左上角Open Folder，指定gcp_vertex_ai為專案資料夾，確保你已經安裝 `google-cloud-storage` 和 `vertexai` 等 Python 套件。你可以執行以下指令來安裝：

```bash
gcloud config set project 你的PROJECT-ID
pip install -r requirements.txt
```

### 1-2. 為你的模型添加記憶(Optional)

在vertex ai studio內，添加example之後，選擇Get code，複製裡面的text1，並貼回我方的app.py，替代原有的text1

### 1-3. 打造自己的example(Optional)

準備一個QA 問答知識集 csv， 把qa_converted.json的資料樣本交給gpt，並將csv也交給gpt，進行格式轉換。

或用我方已準備好的qa_converted.json 上傳給vertex，點集 Get Code，取得裏面的變數text1

### 2. 在開發環境設定環境變數

開啟terminal，並設定環境變數，例如：
```
export CLOUD_STORAGE_BUCKET=你的桶子名字
export Model_NAME=如果想要換自己的模型或是其他模型
```

### 3. 啟動應用程式
```
python app.py
```

### 4. 推送回Artifact Registry

建立 Artifact Registry

```
gcloud artifacts repositories create cxcxc-vertex-ai-demo --location=asia-east1 --repository-format=docker
```

推送回 Artifact Registry

```
gcloud builds submit --tag asia-east1-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/cxcxc-vertex-ai-demo/ai-app:0.0.1
```
## 在Compute Engine 部屬的方式

### 1. 建立Service account

建立service account，名字為aigc-demo-sa，並派發以下IAM Role

```
Storage Admin
Vertex AI User
Artifact registry reader
```
### 2. 建立機器，選用剛建立的Service-account，並設定防火牆

Service account 選擇 aigc-demo-sa 

Access scopes 選擇 Allow full access to all Cloud APIs

勾選 允許http訪問


### 3. 建立機器，設定Startup-script
```
#! /bin/bash

# 安裝 Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
service docker start

# 獲取專案 ID
PROJECT_ID=$(curl -H "Metadata-Flavor: Google" "http://metadata.google.internal/computeMetadata/v1/project/project-id")

# 配置 Docker 認證
gcloud auth configure-docker asia-east1-docker.pkg.dev -q

# 拉取容器映像
docker pull asia-east1-docker.pkg.dev/$PROJECT_ID/cxcxc-vertex-ai-demo/ai-app:0.0.1

# 從元數據服務獲取 CLOUD_STORAGE_BUCKET
CLOUD_STORAGE_BUCKET=$(curl "http://metadata.google.internal/computeMetadata/v1/instance/attributes/CLOUD_STORAGE_BUCKET" -H "Metadata-Flavor: Google")

# 從元數據服務獲取 MODEL_NAME，如果未設置則使用默認值
MODEL_NAME=$(curl "http://metadata.google.internal/computeMetadata/v1/instance/attributes/MODEL_NAME" -H "Metadata-Flavor: Google")


# 運行容器
docker run -p 80:8080 -e PORT=8080 -e MODEL_NAME=$MODEL_NAME -e CLOUD_STORAGE_BUCKET=$CLOUD_STORAGE_BUCKET -d asia-east1-docker.pkg.dev/$PROJECT_ID/cxcxc-vertex-ai-demo/ai-app:0.0.1

```
### 4. 設定Metadata
```
CLOUD_STORAGE_BUCKET=你要存放照片的桶子
MODEL_NAME=gemini-1.5-flash-002
```


## 在cloud run 執行的方式

### 1. 建立Service account 或沿用先前的Service account

建立service account，並派發以下IAM Role

```
Storage Admin
Vertex AI User
Artifact registry reader
```

### 2. 切換至cloud run 進行部屬


在建立過程中，環境變數記得要修改

```
CLOUD_STORAGE_BUCKET=your-bucket-name
MODEL_NAME=gemini-1.5-flash-002
```
