import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/marketindex'
	
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
select = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print('현재 원/달러 환율은 ' + select)
# print(f'현재 원/달러 환율을 {select}')