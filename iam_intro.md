 # IAM 初探

## Step 1 

在先前的Instance發現無法訪問Cloud Storage，原因在於有Service Account。

#### 創建Service Account
設定如下
```
 name : cxcxc-sa-operate-cs
 role: Storage管理員
```

對該機器關機，並Attach Service account  至該機器上，而後開機並連入，操作下列語句

```
gsutil ls 
```

發現權限已可使用，但缺點很明顯，就是權限開得太大了。

## Step 2 

為Service Account的權限添加Condition

將下列your-bucket-name改為 我方bucket名
```
projects/_/buckets/your-bucket-name
```

而後連入instance內

```
# 發現被禁止
gsutil ls 

# 發現可正常瀏覽
gsutil ls gs://your-bucket-name
```
