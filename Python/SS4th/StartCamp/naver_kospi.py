import requests
from bs4 import BeautifulSoup

# 네이버 증권
finance_url = 'https://finance.naver.com/'

res = requests.get(finance_url).text
data = BeautifulSoup(res, 'html.parser')
kospi = data.select_one('#content > div.article > div.section2 > div.section_stock_market > div.section_stock > div.kospi_area.group_quot.quot_opn > div.heading_area > a > span > span.num').text
print(f'오늘의 코스피 지수는 {kospi}입니다.')

# 네이버 국내증시
sise_url = 'https://finance.naver.com/sise/'

res = requests.get(sise_url).text
data = BeautifulSoup(res, 'html.parser')
kospi = data.select_one('#KOSPI_now').text
print(f'오늘의 코스피 지수는 {kospi}입니다.')

# 네이버 KOSPI
kospi_url = 'https://finance.naver.com/sise/sise_index.nhn?code=KOSPI'

res = requests.get(kospi_url).text
data = BeautifulSoup(res, 'html.parser')
kospi = data.select_one('#now_value').text
print(f'오늘의 코스피 지수는 {kospi}입니다.')

# 네이버 KOSPI 하단 표
# kospi_iframe = 'https://finance.naver.com/sise/sise_index.nhn?code=KOSPI&amp;thistime=20200716185900'

# res = requests.get(kospi_iframe).text
# data = BeautifulSoup(res, 'html.parser')
# kospi = data.select_one('body > div > table.type_1 > tbody > tr:nth-child(3) > td:nth-child(2)') # None return