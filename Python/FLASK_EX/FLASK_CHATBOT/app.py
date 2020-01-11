from flask import Flask, render_template, request
import requests
from decouple import config
from pprint import pprint as pp
app = Flask(__name__)

token = config('TOKEN')
chat_id = config('CHAT_ID')
naver_id = config('NAVER_CLIENT_ID')
naver_secret = config('NAVER_CLIENT_SECRET')
app_url = f'https://api.telegram.org/bot{token}'

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')
    message_url = f'{app_url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(message_url)
    return render_template('send.html')

@app.route('/telegram', methods=['POST'])
def telegram():
    # step 1. 구조 print해보기 & 변수 저장
    telegram_response = request.get_json()

    # step 2. 그대로 돌려보내기(echo)
    if telegram_response.get('message') is not None:
        chat_id = telegram_response.get('message').get('from').get('id')
        text = telegram_response.get('message').get('text')
        if text[0:4] == '/한영 ':
            headers = {
                'X-Naver-Client-Id': naver_id,
                'X-Naver-Client-Secret': naver_secret,
            }
            data = {'source':'ko', 'target':'en', 'text':text[4:]}
            papago_response = requests.post(
                'https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data
            )
            text = papago_response.json().get('message').get('result').get('translatedText')
        elif text[0:4] == '/영한 ':
            headers = {
                'X-Naver-Client-Id': naver_id,
                'X-Naver-Client-Secret': naver_secret,
            }
            data = {'source':'en', 'target':'ko', 'text':text[4:]}
            papago_response = requests.post(
                'https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data
            )
            text = papago_response.json().get('message').get('result').get('translatedText')
        elif text[0:4] == '/한불 ':
            headers = {
                'X-Naver-Client-Id': naver_id,
                'X-Naver-Client-Secret': naver_secret,
            }
            data = {'source':'ko', 'target':'fr', 'text':text[4:]}
            papago_response = requests.post(
                'https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data
            )
            text = papago_response.json().get('message').get('result').get('translatedText')
        elif text[0:4] == '/한중 ':
            headers = {
                'X-Naver-Client-Id': naver_id,
                'X-Naver-Client-Secret': naver_secret,
            }
            data = {'source':'ko', 'target':'zh-CN', 'text':text[4:]}
            papago_response = requests.post(
                'https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data
            )
        elif text[0:4] == '/월남 ':
            headers = {
                'X-Naver-Client-Id': naver_id,
                'X-Naver-Client-Secret': naver_secret,
            }
            data = {'source':'ko', 'target':'vi', 'text':text[4:]}
            papago_response = requests.post(
                'https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data
            )
            pp(papago_response.json())
            text = papago_response.json().get('message').get('result').get('translatedText')
        requests.get(f'{app_url}/sendMessage?chat_id={chat_id}&text={text}')
    return '', 200

if __name__=='__main__':
    app.run(debug=True)