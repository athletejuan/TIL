from flask import Flask, render_template, request
from decouple import config
from pprint import pprint
import requests
import random
app = Flask(__name__)
token = config('TELEGRAM_TOKEN')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/send')
def send():
    # chat_id를 가져오는 코드
    # 1. getUpdates 메소드로 요청 보내기
    base = "https://api.telegram.org"    
    method = "getUpdates"
    
    url = f"{base}/{token}/{method}"
    res = requests.get(url).json()

    # 2. 받아온 응답(json)을 dictionary로 바꿔서 첫번째 메시지의 chat_id를 가져온다.
    chat_id = res['result'][0]['message']['chat']['id']
    # chat_id = res.get('result').get('message').get('chat').get('id')

    # home에 보내온 msg를 받아 telegram api를 통해 메시지 전송
    # base = "https://api.telegram.org"    
    method = "sendMessage"     
    text = request.args.get('msg')

    url = f"{base}/{token}/{method}?chat_id={chat_id}&text={text}"

    requests.get(url)
    return render_template('send.html')

@app.route(f'/{token}', methods=['POST'])
def webhook():
    # 1. 메아리 챗봇
    # (1) webhook을 통해 telegram 보낸 요청 안에 있는 메시지를 가져와
    # (2) 그대로 전송
    res = request.get_json()
    text = res.get('message').get('text')
    chat_id = res.get('message').get('chat').get('id')
    
    base = "https://api.telegram.org"    
    method = "sendMessage"
    
    if res.get('message').get('photo') is not None:
        file_id = res.get('message').get('photo')[-1].get('file_id')
        file_res = requests.get(f"{base}/bot{token}/getFile?file_id={file_id}")
        file_path = file_res.json().get('result').get('file_path')
        file_url = f"{base}/file/bot{token}/{file_path}"

        image = requests.get(file_url, stream=True)

        url = 'https://openapi.naver.com/v1/vision/celebrity'

        headers = {
            'X-Naver-Client-Id': config('NAVER_ID'), 
            'X-Naver-Client-Secret': config('NAVER_SECRET')
        }
        files = {
            'image': image.raw.read()
        }

        clova_res = requests.post(url, headers=headers, files=files)
        text = clova_res.json().get('faces')[0].get('celebrity').get('value')
        
    else:
        if text == 'lotto':
            text = str(sorted(random.sample(range(1,46),6)))
        
        # elif text[0:3] == "/번역":
        #     # 파파고로 번역 결과를 알려준다
        #     url = 'https://openapi.naver.com/v1/papago/n2mt'
        #     headers = {
        #         'X-Naver-Client-Id': config('NAVER_ID'),
        #         'X-Naver-Client-Secret': config('NAVER_SECRET')
        #     }
        #     data = {
        #         'source': 'ko',
        #         'target': 'en'
        #         # 'text': "res.get('message').get('result').get('translatedText')"
        #     }
        #     text = res.get('message').get('result').get('translatedText')
        #     res = requests.post(url, headers=headers, data=data)
        #     # text = res.get('message').get('result').get('translatedText')        

    url = f'{base}/bot{token}/{method}?chat_id={chat_id}&text={text}'
    requests.get(url)
    # return render_template('send.html')
    return '', 200

if __name__ == "__main__":
    app.run(debug=True)    