from flask import Flask
from google.cloud import storage
app = Flask(__name__)
# 啟用客戶端
storage_client = storage.Client()


@app.route('/')
def hello_world():
    # 調度瀏覽功能
    buckets = storage_client.list_buckets()
    bucket_result=''
    for bucket in buckets:
        bucket_result= bucket_result + bucket.name + " \r\n "
    return bucket_result

app.run(host="0.0.0.0",port=8081)
