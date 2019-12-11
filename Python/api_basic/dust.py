import requests
from bs4 import BeautifulSoup
from decouple import config

key = config('KEY')
url = 'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={}&numOfRows=10&pageNo=1&startPage=3&sidoName=서울&ver=1.6'.format(key)
request = requests.get(url).text
soup = BeautifulSoup(request,'xml')
gangnam = soup('item')[1]
time = gangnam.dataTime.text
dust = int(gangnam.pm10Value.text)

# dust 변수에 들어 있는 내용을 출력해보세요.
print('{} 기준 미세먼지 농도는 {}입니다.'.format(time, dust))

# dust 변수에 들어 있는 값을 기준으로 상태 정보를 출력해부세요.
if 150 < dust:
  print('매우나쁨')
elif 80 < dust:
  print('나쁨')
elif 30 < dust:
  print('보통')
else:
  print('좋음')