# GCP經典課程Lab總覽


*描述如下*

有部分實作，為瀏覽器行為操作，這種Lab請同學參照講義進行實作
還有另一部分實作，為指令或程式碼類型操作，請參照此Repo相關的檔案

# Cloud Billing

*參照講義，進行內容操作。*

## 1. 帳號、信用卡付費關聯與預算警告


# Cloud Storage

*參照講義，進行內容操作。*

## 1. 桶子建立、上下傳物件

參照講義，進行內容操作，在過程中，老師會逐步講解看到的實作環節背後的意義。

## 2. 桶子權限操作

參照講義，按實作圖進行操作，在過程中，老師將會逐步講解Cloud Storage的權限設計內容。

## 3. 利用桶子的快取進行節費

先將下面兩張圖片儲存到本地端
https://github.com/cxcxc-io/gcp_basic_architecture_tutorial/blob/master/FB%E4%B8%80%E8%88%AC%E5%BB%A3%E5%91%8AV1.png
https://github.com/cxcxc-io/gcp_basic_architecture_tutorial/blob/master/FB%E4%B8%80%E8%88%AC%E5%BB%A3%E5%91%8AV2.png

確認先前建立桶子的權限是對外公開

上傳第一張照片(FB一般廣告V1.png) 至先前的桶子，並點擊右方三個點，編輯中繼資料，找到Cache-Control的欄位，輸入下方欄位值
```
public, max-age=90
```

儲存後，點擊該物件的公開連結，確認照片的模樣

將第二張照片(FB一般廣告V2.png)的名字改為(FB一般廣告V1.png), 上傳至先前的桶子，並點擊右方三個點，編輯中繼資料，找到Cache-Control的欄位，輸入下方欄位值
```
public, max-age=90
```

按下F12,打開Console，並點擊F5重新整理先前已下載圖片的瀏覽器頁面，發現要等一陣子才會變化


# Cloud Shell

請參照 [cloud_shell_intro.md](https://github.com/cxcxc-io/gcp_basic_architecture_tutorial/blob/master/cloud_shell_intro.md) 內的指令


## 1. 登入驗證，操作指定專案內的資源，以命令列操作CloudStorage


## 2. 透過客製化腳本，自動化更改用戶端的Cloud Shell環境，以利公司同仁們統一環境


## 3. 將用戶端的CloudShell環境，還原至最初始狀態

# Compute Shell Editor

請參照 [cloud_shell_editor_intro.md](https://github.com/cxcxc-io/gcp_basic_architecture_tutorial/blob/master/cloud_shell_editor_intro.md) 內的流程指令

## 1. 讓CloudShell快速布建同事們需要的共同開發環境

## 2. 同事們依舊可以開發網頁應用

## 3. 同事們可以安全地調度雲端資源

## 4. 在雲端上製作整合雲端資源的網頁應用

# Compute Engine

請參照 [compute_engine.md](https://github.com/cxcxc-io/gcp_basic_architecture_tutorial/blob/master/compute_engine.md) 內的流程指令

## 1.機器建立，並連入系統內，建立網頁伺服器

## 2.重建一台機器，並設置開機腳本，自動載入網頁

## 3.關機，重設置開機腳本，引入外部metadata

## 4.防火牆設置，並觀察到Service account的重要性

# IAM 初探

請參照 [iam_intro.md](https://github.com/cxcxc-io/gcp_basic_architecture_tutorial/blob/master/iam_intro.md) 內的流程指令

## 1.Service account建置與權限配置

## 2.權限的限制條件實作

## 3.添加外部用戶進入帳號

# VPC

*參照講義，進行內容操作。*

## 1.建置具備經典公私網段的VPC

## 2.Cloud IAP調度使用，使內網可連線

# IAM進階探討

請參照 [iam_adv.md](https://github.com/cxcxc-io/gcp_basic_architecture_tutorial/blob/master/iam_adv.md) 內的流程指令


## 1.在非GCP的環境內使用User Credential 進行開發 

## 2.用戶可透過任一Service Account 調度雲服務資源，強化本地開發安全性

## 3.用戶僅能透過指定Service Account調度雲服務資源，具體強化雲端安全

## 4.用戶在本地端經常性調度service account的方式，並進行程式碼開發
