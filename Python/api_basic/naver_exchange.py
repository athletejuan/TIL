import requests
from bs4 import BeautifulSoup

# 시장지표 상단
url = 'https://finance.naver.com/marketindex'
	
response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
select = data.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

# print('현재 원/달러 환율은 ' + select)
print(f'현재 원/달러 환율은 {select}원 입니다.')

# 시장지표 하단 표
# iframeurl = 'https://finance.naver.com/marketindex/exchangeList.nhn'
# response = requests.get(iframeurl).text
# fdata = BeautifulSoup(response, 'html.parser')
# fselect = fdata.select_one('body > div > table > tbody > tr:nth-child(1) > td.sale').text

# print('현재 원/달러 환율은 ' + fselect)


# 환율페이지
# exurl = 'https://finance.naver.com/marketindex/exchangeDetail.nhn?marketindexCd=FX_USDKRW'
# response = requests.get(exurl).text
# exdata = BeautifulSoup(response, 'html.parser')
# exselects = exdata.select('#content > div.spot > div.today > p.no_today > em > em > span')

# ex = ''
# for select in exselects:
#     ex += select.text
# print('현재 원/달러 환율은 ' + ex)

# 환율페이지 우측사이드바
# aselect = exdata.select_one('#container > div.aside > div:nth-child(2) > table > tbody > tr:nth-child(1) > td:nth-child(3)').text

# print('현재 원/달러 환율은 ' + aselect)