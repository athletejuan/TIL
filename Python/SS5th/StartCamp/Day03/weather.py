import requests
from decouple import config
from pprint import pprint

TOKEN = config('TOKEN')
CHAT_ID = config('CHAT_ID')
API_KEY = config('API_KEY')

url = 'https://www.metaweather.com/api/location/1132599/'

res = requests.get(url).json()

city = res['title']

# 6일치 날씨 예보
# weathers = res['consolidated_weather']
# for weather in weathers:
#     date = weather['applicable_date']
#     sky = weather['weather_state_name']
#     temp = round(weather['the_temp'], 1)
#     max_temp = round(weather['max_temp'], 1)
#     min_temp = round(weather['min_temp'], 1)
#     print(f'{date}일 {location}의 날씨는 {sky}로 예상되며 현재 기온은 {temp}도, 최고 기온은 {max_temp}도, 최저 기온은 {min_temp}도 로 예상됩니다.')  

# 오늘 날씨 예보
date = res['consolidated_weather'][0]['applicable_date']
weather = res['consolidated_weather'][0]['weather_state_name']
# temp = round(res['consolidated_weather'][0]['the_temp'], 1)
max_temp = round(res['consolidated_weather'][0]['max_temp'], 1)
min_temp = round(res['consolidated_weather'][0]['min_temp'], 1)

# print(f'{date}일 {location}의 날씨는 {weather}로 예상되며, 최고 기온은 {max_temp}도, 최저 기온은 {min_temp}도 로 예상됩니다.')

dust_url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={API_KEY}&numOfRows=10&pageNo=2&sidoName=서울&ver=1.0&returnType=json'
response = requests.get(dust_url).json()
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

if (75 < ultrafine):
    ugrade = '매우나쁨'
elif (35 < ultrafine):
    ugrade = '나쁨'
elif (15 < ultrafine):
    ugrade = '보통'
else:
    ugrade = '좋음'

# print(f'{time} 기준 {station}의 미세먼지 농도는 {dust}, 초미세먼지 농도는 { ultrafine }이며, {grade} 수준입니다.')
# message = f'{time} 기준 {station}의 미세먼지 농도는 {dust}, 초미세먼지 농도는 { ultrafine }이며, {grade} 수준입니다.'

text = f'''{date[5:7]}월 {date[8:10]}일 {city}의 날씨는 {weather}로 예상되며, 낮 최고기온은 {max_temp}도 , 아침 최저기온은 {min_temp}도 로 예상됩니다.
현재 서울 {station}의 미세먼지 농도는 {dust}로 {grade}수준, 초미세먼지 농도는 { ultrafine }이며, {ugrade} 수준입니다.
'''

app_url = f'https://api.telegram.org/bot{TOKEN}'
message_url = f'{app_url}/sendMessage?chat_id={CHAT_ID}&text={text}'

requests.get(message_url)