from flask import Flask, request, render_template, jsonify
import os
import base64
from datetime import datetime
from google.cloud import storage
import vertexai
from vertexai.generative_models import GenerativeModel, Part, SafetySetting


app = Flask(__name__)

text1 = """input: 考雲端證照，有什麼用呢
output: 可以給公司作為政府標案的能力量化依據
可以作為自身能力的證明

input: 我想考GCP證照，應該從哪張開始入門呢
output: GCP-ACE這張證照，雖然名字上有工程師
但是考試內容涵蓋了 預算、權限、網路、開發、維運
是很適合學員們了解GCP的課程

input: 我想考AWS證照，應該從哪張開始入門呢
output: 建議先上雲育鏈的經典架構實作課，對雲端有經驗之後
再上AWS解決方案架構師認證課。

input: AWS-SAA 這張證照要怎麼準備呢
output: 自學的話，可以去買大話AWS架構。
想要節省時間的話，可以去買一些外部課程
想要有真實師傅領進門的話，就來上雲育鏈的課程吧

input: 你們AI課都在教些什麼呢？
output: * **課程內容:** 課程內容包含：
    *  AI、ML 和生成式 AI 的基本概念和術語
    *  人工智慧、機器學習和生成式人工智慧的用例
    *  基礎模型的設計注意事項
    *  模型訓練與微調
    *  及時工程
    *  基礎模型評價標準
    *  負責任的人工智慧
    *  人工智慧系統的安全性和合規性
    *  將業務流程打造成一個 AI-Agent
    *  利用多重 AI-Agent 完成複雜任務流，強化 AI 產出品質
    *  引導同仁資料共享與上雲的 – Google Sheet
    *  打造 AI 分身的必要關鍵 – Appscript
    *  台灣最火爆的 Line 官方號運維 – Line Official Account

input: AI的課程，會需要寫程式嗎？
output: 現在已經可以讓AI幫我們寫很精準的程式了
只要能夠很好地讓他了解我們的業務流程
而我們這門課即將帶您了解AI-Agent，知道如何高效地讓他完成任務。

input: 我是一個非資訊業的人士，想要跨足到雲端產業，該怎麼做呢？
output: 把時間專注學習，好好念書，上秉鴻老師的課。

input: AWS-Sysops課程在教什麼呢？
output: 引領學員掌握AWS雲端維運技術，強調實作與理論知識的結合，目的在於全面提升學員的雲端技術實力。鑒於SOA課程調性，我們建議學員在參加本課程前，先完成 AWS認證解決方案架構師考證班 的學習，以確保有堅實的基礎。

以情境式的專案實作進行課程，課程結束可建置出一個產品。
以資訊業界常用的維運情境，呼應AWS核心服務的知識要點。
針對不同維運情境，而設計出來的實作Lab，紮根強化技術能力。
會有兩次的題型解析，剖析考題內的維運要點，精準答題。

input: 雲育鏈的課程跟外面的課程有什麼差別呢？
output: 秉鴻老師是兼具產業界、學界、補教業的前輩
從工程師、資料科學、商業規劃、專案管理、標案申請等均有經驗

上課也會先用人類世界案例，引起同學思想之後，再做類比，之後總結。
課後還會有餐會，連結眾人的社會關係。

input: 課程會不會很難？導致我聽不懂？
output: 可以到任一課程的官網頁面最下方看同學評論

https://www.cxcxc.io/aws-solution-architect-course/

謝謝秉鴻老師上課幽默風趣的言談 用人類世界的生活來解釋對比複雜雲端世界 淺顯易懂也更加深刻印象！對於變化中的雲端資訊技術也一直應變更新！獲益良多！謝謝

老師的 AWS SAA 課程真的是非常出色！他能把原本有點枯燥的技術概念講解得既清晰又有趣，讓學習變得輕鬆許多。老師對 AWS 的理解非常深厚，不僅知識紮實，還能很有效地傳遞給學生。雲育鍊老師的教學方式讓我們能夠輕鬆掌握關鍵概念和實戰技巧。同時，他也很樂於解答問題，給出的建議和實例都非常實用。這堂課我給予滿分評價，推薦給所有想深入了解 AWS 的學習者！

input: 我想報名AWS-SAA課程
output: ## AWS雲端解決方案架構師考證班 - 雲育鏈 | AWS雲端培訓合作夥伴 | 雲端課程培訓

課程內容為最新認證版本【 SAA-C03 】
可順利考取 AWS Solutions Architect – Associate 認證(SAA-C03)，並具有充足理論與實戰經驗，能因應各IT部門的專案需求及雲端代理商的案件，設計出專案中客戶所需的雲端架構，提出可行的雲端解決方案。

先以生活化的故事方式旁徵博引，牽引至技術面做深入的探討。
以資訊業界常用的架構為主，帶出AWS核心服務的重點內容。
課程針對各服務精準介紹、案例考題加強印象，整體考題練習。
每單元上完立即練習，增加考照記憶點，並透過雲端認證小幫手練習。

**課程時間:**
詳見報名連結
https://lihi1.com/OSdQi

**上課地點:**

* 台北市中山區長安東路二段80號5樓 (近松江南京捷運站4號出口)
* 在家遠端直播上課

**多種在雲端上常見的架構延伸討論:**

**加入LINE官方號，詢問課程內容**

https://lin.ee/27OG8ZS

input: 我想報名GCP-ACE課程
output: ## GCP 雲端工程師實作考證班 - 雲育鏈 | AWS雲端培訓合作夥伴 | 雲端課程培訓

本課程將以NIST新方向的雲概念進行實作，當中以「零信任安全」及「雲端原生」技術，貫穿整個GCP雲端架構的思路，結訓後具備考取GCP Cloud Engineer認證的資格與實力。

主要考的都是NIST新方向的雲概念，老師也會在裡面放入多種強化元素：

* 部署應用程式
* 監控運維
* 管理企業解決方案
* 使用Console和CLI來進行開發及運維
* 設計並實作企業應用場景的雲端架構
* 透過架構設計提出解決方案

**課程時間:**
查看下方連結
https://lihi1.com/MJf3i

**上課地點:**

* 台北市中山區長安東路二段80號5樓 (近松江南京捷運站4號出口)
* 在家遠端直播上課

**更多架構與實作Lab:**

以架構思維進行系統設計的培訓，除了學習雲端技術實作外，更是在系統設計思路。剖析各種不同應用場景的架構，並以實作的方式解決。

**加入LINE官方號，詢問課程內容**

https://lin.ee/27OG8ZS


input: 請問你們有專人可以服務嗎？
output: **加入LINE官方號**

https://lin.ee/27OG8ZS

加入之後記得傳張貼圖，我們才能知道喔

input: 你們有提供企業包班服務嗎？
output: 有的，可以加入LINE官方號
https://lin.ee/27OG8ZS

裡面有專人跟您洽談企業包班細節，加入之後記得傳張貼圖，我們才能知道喔

input: 我們公司想要上雲，你們這邊可以怎麼幫忙我們？
output: 每一間公司的企業文化都有不同，會建議找顧問進行討論，設計一個逐步引導的過程
可以加入LINE官方號
https://lin.ee/27OG8ZS

裡面有專人跟您洽談顧問細節，加入之後記得傳張貼圖，我們才能知道喔

input: 我們公司雲端費用很貴，該怎麼辦？
output: 雲端節費是我們公司的強項，您可以選擇上課了解各類服務的節費方向，或聯絡我們，替您安排顧問。
可以加入LINE官方號
https://lin.ee/27OG8ZS

裡面有專人跟您洽談顧問細節，加入之後記得傳張貼圖，我們才能知道喔

input: 你們這裡有教室場地租借嗎？
output: 有的，可以聯絡專人，確認場地可行的租借時間。

一個時段是1600元，當月最優惠，預訂上午+下午時段只要3000$ !!

相關網址如下
https://www.cxcxc.io/space-rental/

input: 你們公司在哪裡啊？
output: 台北據點是長安東路二段80號5樓
中壢是明德路60號四樓
來訪前，建議先打電話詢問是否在辦公室喔， 電話是02-25078554

input: 要如何聯絡到李秉鴻老師呢？
output: 可以加入LINE官方號，由我們替您安排聯絡喔
https://lin.ee/27OG8ZS

input: 我想要團報課程，有人可以幫我嗎？
output: 可以加入LINE官方號，由我們替您安排聯絡喔
https://lin.ee/27OG8ZS"""

# 設定上傳檔案的目錄
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# 初始化 Vertex AI
vertexai.init(location="asia-east1")

# 取得 Cloud Storage bucket 名稱
BUCKET_NAME = os.environ.get('CLOUD_STORAGE_BUCKET')

# 模型名稱，從環境變數取得，若無則使用預設值
MODEL_NAME = os.environ.get('MODEL_NAME', "projects/904506393037/locations/asia-east1/endpoints/9016721025437532160")

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
        combined_input = [text1, user_message, image_part]
    else:
        # 如果沒有圖片，僅使用文字訊息
        combined_input = [text1, user_message]

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

if __name__ == '__main__':
    app.run(debug=True,port=5000)
