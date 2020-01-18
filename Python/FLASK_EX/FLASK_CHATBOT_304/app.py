from flask import Flask, render_template, request
import requests
import random
from bs4 import BeautifulSoup as bs
from datetime import datetime
from pprint import pprint as pp
app = Flask(__name__)

token = '###'
chat_id = '###'
naver_client_id = '###'
naver_client_secret = '###'
api_key = '###'
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
    # step 1. 구조 print 해보기 & 변수 저장
    telegram_response = request.get_json()
    # print(telegram_response)
    # print(request)

    # step 2. 그대로 돌려보내기
    if telegram_response.get('message') is not None:
        chat_id = telegram_response.get('message').get('from').get('id')
        text = telegram_response.get('message').get('text')
        
        if text[0:4] == '/한영 ':
            headers = {
                'X-Naver-Client-Id': naver_client_id,
                'X-Naver-Client-Secret': naver_client_secret,
            }
            data = {'source':'ko', 'target':'en', 'text':text[4:]}
            papago_response = requests.post(
                'https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data
            )
            # pp(papago_response.json())
            text = papago_response.json().get('message').get('result').get('translatedText')
        elif text == '미세먼지':
            api_url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={api_key}&numOfRows=40&pageNo=1&startPage=3&sidoName=서울&ver=1.6'
            today = datetime.now()
            response = requests.get(api_url).text
            data = bs(response, 'xml')
            station = data('item')[27]

            dust = int(station.pm10Value.text)
            location = station.stationName.text

            if dust > 150:
                dust_rate = '매우 나쁨'
            elif dust > 80:
                dust_rate = '나쁨'
            elif dust > 30:
                dust_rate = '보통'
            else:
                dust_rate = '좋음'

            text = f'{today.month}월 {today.day}일 {today.hour}시, {location} 미세먼지 {dust_rate} 입니다.'

        elif text == '로또':
            text = sorted(random.sample(range(1,46),6))
        requests.get(f'{app_url}/sendMessage?chat_id={chat_id}&text={text}')

    return '', 200

if __name__ == '__main__':
    app.run(debug=True)