# STEP 1

開機之後，嘗試安裝 男人的浪漫老遊戲，並把先前的網頁載入進來，發現Compute Engine也能跟GCP Resource溝通。

連入之後的指令如下
```
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo service docker start
sudo docker run -d --name dosgame -p 443:262 oldiy/dosgame-web-docker:latest
sudo docker run -d -p 80:5000 -e PORT=5000 -e METADATA_DEMO=abc  b97607065/gcp_metadata_demo:0.0.3 
```

# STEP 2

### Startup-script

```
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
service docker start
docker run -d --name dosgame -p 443:262 oldiy/dosgame-web-docker:latest
docker run -d -p 80:5000 -e PORT=5000 -e METADATA_DEMO=abc  b97607065/gcp_metadata_demo:0.0.3 
```

訪問外部IP，發現有網頁

瀏覽tmp資料夾，確認沒有cxcxc檔案
```
ls /tmp
```

# STEP 3

對機器進行關機，並更新Startup-script內容，並撤下Service account，並在console內追加meatadata

### metadata內容值

```
欄位:內容
METADATA_DEMO:cxcxc

```

### Startup-script
```
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
service docker start

METADATA_DEMO=$(curl "http://metadata.google.internal/computeMetadata/v1/instance/attributes/METADATA_DEMO" -H "Metadata-Flavor: Google")
touch /tmp/$METADATA_DEMO
docker run -d -p 80:5000 -e PORT=5000 -e METADATA_DEMO=$METADATA_DEMO  b97607065/gcp_metadata_demo:0.0.3 
```

編輯完成後，再開機，並連入

連入後，觀察tmp資料夾，發現已有檔案出現
```
ls /tmp
```

# STEP4

重新以gsutil訪問桶子，發現沒有service account 不能訪問
```
gsutil ls
```

從內部訪問Webserver，發現可行
```
curl localhost:80/cxcxc.html
```

從外部訪問，發現無法訪問，原因是在於firewall沒開放 

為該instance貼network-tag，內容如下

```
http-server
```






