# Lab1 - Service Account的重複創建

## 建置Service Account

設定Service account 名字為

`cxcxc-sa-demo`

給予 `Storage Object Viewer` 的Role
***

## 建立GCE Instance

規格選擇 e2-micro

地區選擇 台灣

服務帳戶選用先前建置的`cxcxc-sa-demo`

***

## 連入Instance


使用gsutil驗證權限
```
gsutil ls
```
***

## 移除Service Account，並重新建立Service Account

設定Service account 名字為

`cxcxc-sa-demo`

給予 `Storage Object Admin` 的Role

在Instance內，重新輸入
```
gsutil ls
```
關機，重新設定Service account為 `cxcxc-sa-demo`

開機連入Instance，重新輸入
```
gsutil ls
````

***

# Lab2 - 客製化Role 

## 創建Role，並附加至Service Account

創建Role，名為

`CloudStorageReadOnly`

選用下方兩個動作

```
storage.objects.get
storage.objects.list
```

找到先前建置的cxcxc-sa-demo 服務帳戶，權限更換為此Role

## 測試Service Account的權限

為cxcxc-sa-demo 服務帳戶，追加自身Role為`Service account token creator `

### 啟用Cloud shell，輸入下方指令

```
gsutil -i <你的服務帳戶全名> ls

gsutil -i <你的服務帳戶全名> cp README.md <你的Cloud Storage Bucket名>
```

# Lab3 - 設定可設定其他權限的角色

### 切換至IAM 管理介面，添加第二用戶，賦予

```
Project IAM Admin Role
```

設置條件，此條件為關鍵，只允許該用戶管理特定服務的權限，範例為僅允許授權Storage Admin

```
api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', []).hasOnly(['roles/storage.admin'])
```
***
### 切換為第二用戶，透過第二用戶，添加第三用戶

權限為 Storage Viewer，發現失敗

將權限改為 Storage Admin，發現成功

### 切換為第三用戶，透過第三用戶，操作Cloud Storage

```
gcloud config set project <你的project-id>
gsutil ls
```


# Lab4 OpsAgent體驗

建立Service account

建立一台GCE Instance，透過Startup-script安裝stress
```
#!/bin/bash
apt-get install -y stress
```
設置alarm與notification

安裝opt agent

連入後，進行軟體壓力測試
```
nohup stress -c 2 -m 2 --vm-bytes 512M -t 600s &
```
收到警告


移除警告


機器刪除
