# STEP 1

# STEP 2

### Startup-script

再開一台機器，將YOUR-BUCKET與Folder 改為自己先前建立的桶子與資料夾名

```
#!/bin/bash

apt-get install -y apache2
service apache2 start
gsutil cp gs://YOUR-BUCKET/Folder/cxcxc.html /var/www/html/

```

# STEP 3

對機器進行關機，並更新Startup-script內容，並撤下Service account，並在console內追加label

### label內容值

```

METADATA_DEMO : cxcxc

```


### Startup-script
```
#!/bin/bash

apt-get install -y apache2
service apache2 start
gsutil cp gs://YOUR-BUCKET/Folder/cxcxc.html /var/www/html/

METADATA_DEMO=$(curl "http://metadata.google.internal/computeMetadata/v1/instan
ce/attributes/METADATA_DEMO" -H "Metadata-Flavor: Google")
touch /tmp/$METADATA_DEMO

```

編輯完成後，再開機

# STEP4

連入後，觀察tmp資料夾，發現已有檔案出現
```
ls /tmp
```

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






