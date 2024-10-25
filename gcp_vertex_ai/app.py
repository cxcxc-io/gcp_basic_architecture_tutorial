from flask import Flask, request, render_template, jsonify
import os
import base64
from datetime import datetime
from google.cloud import storage
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting


app = Flask(__name__)

# 設定上傳檔案的目錄
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 初始化 Vertex AI
vertexai.init(location="asia-east1")

# 取得 Cloud Storage bucket 名稱
BUCKET_NAME = os.environ.get('CLOUD_STORAGE_BUCKET')

# 模型名稱，從環境變數取得，若無則使用預設值
MODEL_NAME = os.environ.get('MODEL_NAME', 'gemini-1.5-flash-002')

# Vertex AI 的配置
generation_config = {
    "max_output_tokens": 8192,
    "temperature": 1,
    "top_p": 0.95,
}

safety_settings = [
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
    ),
    SafetySetting(
        category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
        threshold=SafetySetting.HarmBlockThreshold.BLOCK_ONLY_HIGH
    ),
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get('message')
    image_base64 = request.form.get('image_base64')  # 從請求中獲取 Base64 圖片

    if not user_message:
        return jsonify({'error': '必須提供文字訊息'}), 400

    # 處理圖片資料，如果有的話
    if image_base64:
        # 將 Base64 字串轉換為二進位資料
        image_data = base64.b64decode(image_base64)

                # 將圖片儲存到 Cloud Storage
        try:
            image_url = save_image_to_bucket(image_data)
            conversation_history_entry = f"你上傳了一張圖片: {image_url}"
        except Exception as e:
            return jsonify({'error': f'圖片儲存失敗: {str(e)}'}), 500

        # 創建 Part 對象以包含圖片資料
        image_part = Part.from_data(
            mime_type="image/png",  # 可以根據實際檔案類型調整
            data=image_data
        )
        # 將文字訊息與圖片的 Part 物件一起作為輸入
        combined_input = [user_message, image_part]
    else:
        # 如果沒有圖片，僅使用文字訊息
        combined_input = [user_message]

    # 使用 Vertex AI 生成回應
    try:
        model = GenerativeModel(MODEL_NAME)
        responses = model.generate_content(
            combined_input,
            generation_config=generation_config,
            safety_settings=safety_settings,
            stream=True,
        )

        # 取得生成的回應
        response_message = ""
        for response in responses:
            response_message += response.text
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': response_message})

def save_image_to_bucket(image_data):
    """將圖片儲存到指定的 Cloud Storage bucket，並返回圖片的公開 URL"""
    # 初始化 Cloud Storage 客戶端
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)

    # 取得當前日期和時間
    current_datetime = datetime.utcnow()
    date_folder = current_datetime.strftime('%Y-%m-%d')
    filename = current_datetime.strftime('%Y-%m-%d-%H-%M-%S') + '.jpg'

    # 建立儲存路徑
    blob_path = f"{date_folder}/{filename}"
    blob = bucket.blob(blob_path)

    # 將圖片上傳到 Cloud Storage
    blob.upload_from_string(image_data, content_type='image/jpeg')

    # 設置 blob 為公開可讀
    blob.make_public()

    # 返回公開的 URL
    return blob.public_url

# if __name__ == '__main__':
#     app.run(debug=True,port=5000)
