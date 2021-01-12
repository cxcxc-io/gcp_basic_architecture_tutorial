from google.cloud import storage

# 啟用客戶端
storage_client = storage.Client()

# 調度瀏覽功能
buckets = storage_client.list_buckets()

# 打印桶子
for bucket in buckets:
    print(bucket.name)