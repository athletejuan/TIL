from flask import Flask, render_template, request
from decouple import config
import requests
import random

app = Flask(__name__)

base = 'https://api.telegram.org'
token = config('TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')


@app.route('/')
def hello():
    return "Hello World"

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')
    requests.get(f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return render_template('send.html')

@app.route(f'/{token}', methods=['POST'])
def telegram():
    # step 1. 구조 print 해보기 & 변수 저장
    # print(request.get_json())
    from_telegram = request.get_json()

    # step 2. 그대로 돌려보내기
    if from_telegram.get('message') is not None:    # NoneType일 경우 예외처리
        chat_id = from_telegram.get('message').get('from').get('id')
        text = from_telegram.get('message').get('text')
        # CFR
        if from_telegram.get('message').get('photo') is not None:
            url = "https://openapi.naver.com/v1/vision/celebrity"
            files = {'image': open('YOUR_FILE_NAME', 'rb')}
            headers = {'X-Naver-Client-Id': naver_client_id, 'X-Naver-Client-Secret': naver_client_secret}
            cfr_res = requests.post(url, files=files, headers=headers)
            text = cfr_res.text
        # 파파고 번역
        else:
            if text[0:4] == '/한영 ':
                headers = {'X-Naver-Client-Id': naver_client_id, 'X-Naver-Client-Secret': naver_client_secret}
                data = {'source':'ko', 'target':'en', 'text':text[4:]}
                papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
                text = papago_res.json().get('message').get('result').get('translatedText')
            elif text[0:4] == '/영한 ':
                headers = {'X-Naver-Client-Id': naver_client_id, 'X-Naver-Client-Secret': naver_client_secret}
                data = {'source':'en', 'target':'ko', 'text':text[4:]}
                papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
                text = papago_res.json().get('message').get('result').get('translatedText')
            elif text[0:4] == '/한불 ':
                headers = {'X-Naver-Client-Id': naver_client_id, 'X-Naver-Client-Secret': naver_client_secret}
                data = {'source':'ko', 'target':'fr', 'text':text[4:]}
                papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
                text = papago_res.json().get('message').get('result').get('translatedText')
            # 로또
            elif text == '로또추천':
                text = sorted(random.sample(range(1,46),6))
            elif text[:4] == '로또확인':
                num = text[4:]
                url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
                res = requests.get(url).json()

                winner = []
                for i in range(1,7):
                    winner.append(res[f'drwtNo{i}'])
                bonus_num = res['bnusNo']
                text = f'로또 {num}회차의 당첨번호는 {winner}이고, 보너스번호는 {bonus_num}입니다.'
        requests.get(f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return '', 200
