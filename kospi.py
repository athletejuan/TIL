import requests
import bs4

url = "https://finance.naver.com/sise/"
ex_url = "https://finance.naver.com/marketindex/"
main_url = "https://www.naver.com/"

response = requests.get(url).text
response2 = requests.get(ex_url).text
response3 = requests.get(main_url).text

document = bs4.BeautifulSoup(response,'html.parser')
document2 = bs4.BeautifulSoup(response2,'html.parser')
document3 = bs4.BeautifulSoup(response3,'html.parser')

kospi = document.select_one('#KOSPI_now').text
kosdaq = document.select_one('#KOSDAQ_now').text
# ex = document2.select_one('#KOSDAQ_now').text
key = document3.select_one('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(1) > a > span.ah_k').text
key2 = document3.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(1) > a').text

print('현재 코스피 지수는: '+kospi)
print('현재 코스닥 지수는: '+kosdaq)
print('현재 검색어 1위는:'+key)
print('현재 검색어 순위는:'+key2)