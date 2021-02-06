# GCP

### Project 為基底資源管理

# CloudBilling

### 建置帳單帳戶（供付款使用）

### 設置快訊（Alarm，帳單警告）

# Cloud VPC

### VPC建置

### Route配置 - 僅允許特定標籤的用戶可訪問Internet Gateway

### Firewall建置 -  並考慮使用Cloud IAP，使可用GCP Console 管理私網機器

#### (Optional) Private Google Access 建置
#### Cloud NAT建置 
#### Cloud VPN 建置 
#### Network Peering Connection 建置

# Cloud Storage

### Bucket建置

### 存取權限設置 - IAM or ACL

#### 資料保護相關措施

# Cloud IAM - 管理

### 建置 Service account，並給予有條件的Role

### 引入 Member account(用戶)，並給予其調度Service account的權限

### 配發Service account 的 Credential 給 用戶

# Cloud Shell & Editor

### 登入專案

### 以https連結，快速打造公司專案環境與程式碼，快速協作

### 將service account的credential 結合環境變數，開發者在寫程式時，可編寫安全的程式碼。

### 以命令列調度service account，將本地的程式資源，放到遠端Cloud Storage Bucket

# Compute Engine

## 部署階段

### 開啟機器階段，選用機型與 Service account

### 開啟機器階段，並透過Metadata 設置 外部環境變數

### 開啟機器階段，設置Startup-script，將Storage內的程式拉取安裝部署

### 開啟機器階段，設定Network-tag，允許ssh或public-subnet訪問

## 維護管理階段

### 啟用OS Login 功能，後續人員皆能以email登入該機器管理。

