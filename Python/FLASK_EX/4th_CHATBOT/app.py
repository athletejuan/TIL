from flask import Flask, render_template, request
import requests
import random
from decouple import config
from bs4 import BeautifulSoup
from datetime import datetime
app = Flask(__name__)

token = config('TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secret = config('NAVER_CLIENT_SECRET')
base = 'https://api.telegram.org'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/write')
def write():
    return render_template('write.html')

@app.route('/send')
def send():
    text = request.args.get('message')
    res = f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(res)
    return render_template('send.html')

@app.route('/telegram', methods=['POST'])
def telegram():
    telegram_response = request.get_json()
    # print(telegram_response)

    if telegram_response.get('message') is not None:
        text = telegram_response.get('message').get('text') # echo

        if text[0:4] == '/번역 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret,
            }
            data = {'source':'ko', 'target':'en', 'text':text[4:]}
            papago_response = requests.post(
                'https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data
            )
            # print(papago_response.json())
            text = papago_response.json().get('message').get('result').get('translatedText')

        elif text == '미세먼지':
            today = datetime.now()
            dust_api = config('DUST_API_KEY')
            dust_url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?ServiceKey={dust_api}&stationName=강남구&dataTerm=DAILY'
            dust_res = requests.get(dust_url).text
            data = BeautifulSoup(dust_res, 'xml')
            dust = int(data('item')[0].pm10Value.text)

            if dust > 150:
                dust_rate = '매우 나쁨'
            elif dust > 80:
                dust_rate = '나쁨'
            elif dust > 30:
                dust_rate = '보통'
            else:
                dust_rate = '좋음'

            text = f'{today.month}월 {today.day}일 {today.hour}시, 강남구 미세먼지는 {dust}, {dust_rate} 수준 입니다.'

        elif text == '로또':
            lotto = ','.join(map(str, sorted(random.sample(range(1,46),6))))
            text = f'로또 추천번호는 {lotto}번 입니다.'

        elif text == '로또확인':
            lotto_url = 'https://dhlottery.co.kr/common.do?method=main'
            res = requests.get(lotto_url).text
            data = BeautifulSoup(res, 'html.parser')
            thistime = data.select_one('#lottoDrwNo').text
            winner = []
            for i in range(1,7):
                select = data.select_one(f'#numView > #drwtNo{i}').text
                winner.append(select)
            winNum = ','.join(winner)
            bnsNum = data.select_one('#bnusNo').text
            text = f'이번 {thistime}회차 로또 당첨번호는 {winNum}번 이고 보너스번호는 {bnsNum}번 입니다.'

    requests.get(f'{base}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
    return '', 200  # return이 없으면 함수가 끝나지않으니 500 에러 발생

# python app.py 로 실행했을때만 Debug mode, flask run으로 실행시 nono
if __name__=='__main__':
    app.run(debug=True)