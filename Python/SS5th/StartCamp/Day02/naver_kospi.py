import requests
from bs4 import BeautifulSoup


url = "https://finance.naver.com/sise/"
response = requests.get(url).text
soup = BeautifulSoup(response, 'html.parser')
kospi = soup.select_one('#KOSPI_now')
text = kospi.text

# print(f'현재의 코스피 지수는 ' + text + '입니다.')
print(f'현재의 코스피 지수는 {text}입니다.')