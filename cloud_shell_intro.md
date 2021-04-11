# 本地端使用gcloud


```
# 登入aws console
# 啟用aws 的cloud shell vm，充當外部筆電
https://cxcxc-learning.signin.aws.amazon.com/console

# 在裡面植入gcloud sdk套件庫
sudo tee -a /etc/yum.repos.d/google-cloud-sdk.repo << EOM
[google-cloud-sdk]
name=Google Cloud SDK
baseurl=https://packages.cloud.google.com/yum/repos/cloud-sdk-el7-x86_64
enabled=1
gpgcheck=1
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
       https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOM

# 安裝gcloud sdk
sudo yum install -y google-cloud-sdk


# 登入指令，而後彈跳出一個網址，點擊後，輸入google帳號進行驗證
# gcloud auth login
gcloud init

# 設定要操作的專案
gcloud config set project {PROJECT_ID}
```


# 在Cloud Shell 內使用gcloud

省略了 gcloud auth login 這個環節，直接跳到設定操作專案的環節

```
gcloud config set project {PROJECT_ID}
```

# 使用gsutil 訪問 cloud storage

不要記指令，只需要記核心名詞，而後丟到Google去快速檢索。

比如 gsutil bucket list  就能馬上找到範例

https://cloud.google.com/storage/docs/listing-buckets

google goo得好， 工程師當到老。

```
# 瀏覽 當前專案下所有的bucket
gsutil ls 

# 瀏覽 bucket內，有哪些object
gsutil ls gs://your-bucket-name/folder/

# 將準備好的範例網頁，而後將該檔案上傳 至 指定的bucket內
gsutil cp cxcxc.html gs://your-bucket-name/folder/

# 瀏覽 bucket內，有哪些object
gsutil ls gs://your-bucket-name/folder/

# 刪除 該object，範例，先不要用
# gsutil rm gs://your-bucket-name/folder/object



```
# 調度那些GCP沒放在Console上的功能
```
# 瀏覽 bucket目前的屬性
gsutil ls -L -b {YOUR-BUCKET-NAME}

# 對桶子設定版本號
gsutil versioning set on {YOUR-BUCKET-NAME}

# 瀏覽 bucket目前的屬性
gsutil ls -L -b {YOUR-BUCKET-NAME}

# 關閉桶子的版本號
gsutil versioning set off {YOUR-BUCKET-NAME}

```

# 變更Cloud Shell的基底環境

```
# .customize_enviroment 是cloud shell預設的隱藏腳本
echo touch /tmp/cxcxc_demo.txt > ~/.customize_environment

# 透過網頁重新啟動cloud shell

# 搜尋 /tmp 資料夾，發現已有cxcxc_demo.txt檔案
ls /tmp

```

# 清除Cloud Shell環境

```
# 刪除家目錄內所有內容
sudo rm -rf $HOME


# 透過網頁重新啟動cloud shell

```
