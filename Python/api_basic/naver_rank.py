import requests
import bs4 
import datetime

html = requests.get('https://www.naver.com/').text
soup = bs4.BeautifulSoup(html, 'html.parser')
# firefox에서는 css path를 복사해야 함.
# tags = soup.select('.PM_CL_realtimeKeyword_rolling .ah_item .ah_k')
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(12) > a > span.ah_k
tags = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li .ah_k')
# print(tags)

now = datetime.datetime.now()
print(f'{now} 기준 네이버 검색어 순위')
# with open('naver.txt', 'w') as f:
#     f.write(f'{now} 기준 네이버 검색어 순위\r\n')
for i, tag in enumerate(tags):
    print(f'{i+1}. {tag.text}')
    # f.write(f'{i+1}. {tag.text}\r\n')