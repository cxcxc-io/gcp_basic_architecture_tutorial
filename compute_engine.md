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