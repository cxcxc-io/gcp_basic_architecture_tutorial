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

### 1. 安裝必要套件
首先，確保你已經安裝 `google-cloud-storage` 和 `vertexai` 等 Python 套件。你可以執行以下指令來安裝：

```bash
pip install -r requirements.txt
```


### 2. 建立 .env 檔案

在專案根目錄建立 .env 檔案，並設定環境變數，例如：
```
CLOUD_STORAGE_BUCKET=your-bucket-name
MODEL_NAME=gemini-1.5-flash-002
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

## 在cloud run 執行的方式

### 1. 建立Service account

建立service account，並派發以下IAM Role

```
Storage Admin
Vertex AI User
```
### 2. 切換至cloud run 進行部屬


在建立過程中，環境變數記得要修改

```
CLOUD_STORAGE_BUCKET=your-bucket-name
MODEL_NAME=gemini-1.5-flash-002
```