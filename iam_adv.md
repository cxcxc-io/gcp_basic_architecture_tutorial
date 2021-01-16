# Step1

#### 登入AWS Console 充當本地機器

https://cxcxc-learning.signin.aws.amazon.com/console

帳密：課程時詢問老師

啟用aws版本的CloudShell，並在裡面安裝Google的CloudSDK

#### 輸入指令編輯，遠端套件庫
```
sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM

```

#### 更新遠端套件庫網址
```
[google-cloud-sdk]
name=Google Cloud SDK
baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=1
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOM
```

#### 安裝  CloudSDK 與 python套件
```
sudo yum install -y google-cloud-sdk
sudo pip3 install google-cloud-storage
```

#### 在AWS CloudShell 內登入
輸入後，會彈跳出連結，要求我方使用google驗證
```
google auth application-default login
```

#### 啟用python3命令
```
python3
```

#### 輸入list bucket的python相關語句

```
from google.cloud import storage

# 啟用客戶端
storage_client = storage.Client()

# 調度瀏覽功能
buckets = storage_client.list_buckets()

# 打印桶子
for bucket in buckets:
    print(bucket.name)

```

#### 江湖一點訣，點破不值錢
```
# 該些credential暫存在家目錄內 (~/.config/gcloud/application_default_credentials.json)
ls ~/.config/gcloud/

```




# Step2

重新安裝一個新的AWS Cloud Shell
原因是這種登入方式，是GCP不建議的，他希望我們Member都透過service account 調度服務

為IAM User設置 可調度service account的role，Service Account User 與 Token Creator兩個權限。

登入新的IAM User，並輸入指令，要求透過先前建置的service account調度gcloud storage

```
gcloud compute instances list --impersonate-service-account=cxcxc-cloud-logging-demo@gcp-practice-123.iam.gserviceaccount.com

```
