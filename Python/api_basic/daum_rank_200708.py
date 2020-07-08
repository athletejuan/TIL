import requests
from bs4 import BeautifulSoup

url = 'https://www.daum.net/'
res = requests.get(url).text
data = BeautifulSoup(res, 'html.parser')
# 한 화면에 보이는 검색어(1페이지)
selects = data.select('#wrapSearch > div.slide_favorsch > ul:nth-child(1) > li > a')
# 숨어있는 검색어까지
# selects = data.select('#wrapSearch > div.slide_favorsch > ul > li > a')

for select in selects:
    print(select.text)