import requests
from pprint import pprint

key = 'API_KEY'
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=5&pageNo=1&sidoName=서울&ver=1.0&returnType=json'
response = requests.get(url).json()

pprint(response)
print(type(response))


# 미니 과제(옵션)
# 'sidoName의 미세먼지 농도는 pm10value입니다.'라는 메시지를 출력하시오.

sidoName = response['response']['body']['items'][0]['sidoName']
dust = response['response']['body']['items'][0]['pm10Value']

print(f'{sidoName}의 미세먼지 농도는 {dust}입니다.')