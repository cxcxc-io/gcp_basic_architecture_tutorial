建立Service account，權限為
```
Vertex AI User
```


建立GCE，Service account 指定為剛剛建立的Service account，並安裝Dify
```
curl -fsSL https://get.docker.com -o get-docker.sh
sh get-docker.sh
service docker start

curl -L https://github.com/docker/compose/releases/latest/download/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose 
chmod +x /usr/local/bin/docker-compose 
git clone -b 1.4.0 https://github.com/langgenius/dify.git 
cd dify/docker 
docker-compose up -d
```

# Lab1 - AI-Agent的第一次嘗試

目標： 知曉 LLM 與 Prompt

# Lab2 - Workflow的第一次嘗試

# Lab3 - 透過參數抽取器 做自然語言的json處理

# Lab4 - 透過問題分類器 做新型態的IF ELSE

# Lab5 - 透過LLM節點，做進階回復。

