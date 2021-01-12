# 미세먼지 데이터 json으로 가져와서 TELEGRAM 메시지 전송
import requests

key = 'API_KEY'

url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=10&pageNo=2&sidoName=서울&ver=1.0&returnType=json'
response = requests.get(url).json()
item = response.get('response').get('body').get('items')[9]
time = item.get('dataTime')
station = item['stationName']
dust = int(item.get('pm10Value'))
ultrafine = int(item.get('pm25Value'))

if (150 < dust):
    grade = '매우나쁨'
elif (80 < dust):
    grade = '나쁨'
elif (30 < dust):
    grade = '보통'
else:
    grade = '좋음'

# print(f'{time} 기준 {station}의 미세먼지 농도는 {dust}, 초미세먼지 농도는 { ultrafine }이며, {grade} 수준입니다.')
message = f'{time} 기준 {station}의 미세먼지 농도는 {dust}, 초미세먼지 농도는 { ultrafine }이며, {grade} 수준입니다.'

def send_telegram_message(message):
    bot_token = 'TOKEN'
    my_chat_id = 'CHAT_ID'

    telegram_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?'
    query = f'chat_id={my_chat_id}&text={message}'

    requests.get(telegram_url+query)

send_telegram_message(message)