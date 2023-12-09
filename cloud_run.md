# 打開cloud shell editor , 下載教材

https://ssh.cloud.google.com/cloudshell/editor?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fcxcxc-io%2Fgcp_basic_architecture_tutorial.git&cloudshell_open_in_editor=cloud_shell_editor_intro.md&cloudshell_workspace=.

# 打開terminal, 切換project

```
gcloud config set project YOUR-PROJECT-ID
```

# 確認有個Dockerfile

# 確認有個app.py

# (optional) 在cloud shell editor 預載執行

```
pip3 install -r requirements.txt
python3 app.py
```

# 建立artifact registry 

```
gcloud artifacts repositories create cxcxc-demo --location=asia-east1 --repository-format=docker
```

# 透過cloud build 打包成image, 並存放在artifact registry

```
gcloud builds submit --tag asia-east1-docker.pkg.dev/$GOOGLE_CLOUD_PROJECT/cxcxc-demo/web-app:0.0.1
```

# 打開cloud run 介面，進行部屬
可設定環境變數 NAME為任意值
