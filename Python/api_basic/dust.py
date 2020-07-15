import requests
from bs4 import BeautifulSoup
from decouple import config

key = config('DUST_API_KEY')
# 서울 중 임의의 지역(API로 불러오는 데이터의 순서가 바뀔 수 있기 때문에) 미세먼지
url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=10&pageNo=1&sidoName=서울&ver=1.6'
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
item = soup('item')[0]
station = item.stationName.text
time = item.dataTime.text
dust = int(item.pm10Value.text)

# 강남구 미세먼지
# dust_url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?ServiceKey={key}&stationName=강남구&dataTerm=DAILY'
# dust_res = requests.get(dust_url).text
# data = BeautifulSoup(dust_res, 'xml')
# today = data.dataTime.text
# dust = int(data.item.pm10Value.text)
# 최근 결과 이전 시간 대의 결과가 보고싶을 때
# dust = int(data('item')[0].pm10Value.text)

# dust 변수에 들어 있는 내용을 출력해보세요.
print(f'{time} 기준 {station} 미세먼지 농도는 {dust},')
# print(f'{data.dataTime.text} 기준 강남구 미세먼지 농도는 {dust},')
# print(f'{today[:4]}년 {today[5:7]}월 {today[8:10]}일 {today[11:13]}시 기준 강남구 미세먼지 농도는 {dust},')

# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해부세요.
if 150 < dust:
  print('매우나쁨 입니다.')
elif 80 < dust:
  print('나쁨 입니다.')
elif 30 < dust:
  print('보통 입니다.')
else:
  print('좋음 입니다.')