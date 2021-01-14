# STEP 1

### Startup-script

將YOUR-BUCKET與Folder 改為自己先前建立的桶子與資料夾名

```
#!/bin/bash

apt-get install -y apache2
service apache2 start
gsutil cp gs://YOUR-BUCKET/Folder/cxcxc.html /var/www/html/

```

# STEP 2

再開一台機器，並且不給予Service account，並將下面的開機腳本內的YOUR-BUCKET與Folder 改為自己先前建立的桶子與資料夾名

貼回至Console

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