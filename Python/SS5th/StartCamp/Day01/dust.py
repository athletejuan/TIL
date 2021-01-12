# 미세먼지 데이터 구버전(xml)
import requests
from bs4 import BeautifulSoup

key = 'API_KEY'

# url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getMsrstnAcctoRltmMesureDnsty?ServiceKey={key}&numOfRows=10&pageNo=3&stationName=강남구&dataTerm=DAILY&ver=1.6'
url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={key}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'
response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
# print(data)
item = data('item')[5]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)

if (150 < dust):
    grade = '매우나쁨'
    # print('매우나쁨')
elif (80 < dust):
    grade = '나쁨'
    # print('나쁨')
elif (30 < dust):
    grade = '보통'
    # print('보통')
else:
    grade = '좋음'
    # print('좋음')

print(f'{time} 기준 {station}의 미세먼지 농도는 {dust}이며, {grade} 수준입니다.')