# Cloud Shell Editor的大功用

讓大家的環境都給統一起來，比如建構統一的專案環境。

複製下方連結，貼回瀏覽器上。

我們會發現他把github資料夾給下載到cloud shell內了。


https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fcxcxc-io%2Fgcp_basic_architecture_tutorial.git&cloudshell_open_in_editor=cloud_shell_editor_intro.md&cloudshell_workspace=.

## 設置資料夾為工作目錄(optional)

對新增的資料夾點擊右鍵，設置Workspace

## 先行安裝環境
```
sudo pip3 install -r requirements.txt
```

## 執行 hello_world.py

啟用terminal，觀察 Cloud Shell的Python3開發環境

在terminal內，使用python3執行hello_world.py

```
python3 --version

python3 hello_world.py
```

## 執行 flask_web_demo.py

點開flask_web_demo.py，得知其內容是啟用web server

在terminal內，使用python3執行flask_web_demo.py

彈跳出網頁連結，發現我方仍可觀看網頁開發結果

```
python3 flask_web_demo.py

```

## 執行 cloudstorage_integrate_demo.py

點開cloudstorage_integrate_demo.py，得知python調度cloudstorage的方式。

在terminal內，使用python3執行cloudstorage_integrate_demo.py

彈跳出網頁連結，發現我方仍可觀看網頁開發結果

```
python3 cloudstorage_integrate_demo.py

```

發現不能執行，原因在於沒有指定Project

兩種方案

### 第一種方案在當前terminal切換專案，並在當前terminal執行python腳本

```
gcloud config set project {YOUR-PROJECT-ID}
python3 cloudstorage_integrate_demo.py
```

### 第二種追加客製腳本，使自動進入專案

#### 打開客製化腳本，並鍵入 i ，開始編輯
```
vim ~/.customize_environment
```

#### 將下方Project-ID名更改後，貼入
```
gcloud config set project {YOUR-PROJECT-ID}
```

#### 點擊右上角功能，重開機


#### 運行腳本，發現可瀏覽所有bucket


# 執行integrate_flask_cloudstorage.py

發現已可編寫一個具備GCP調度能力的WEB應用

# 下一步教材準備

## 使用命令列，將 cxcxc.html放入先前建置好的Bucket(optional)

```
gsutil cp cxcxc.html gs://YOUR-BUCKET-NAME/FOLDER/
```





