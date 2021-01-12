import requests
from bs4 import BeautifulSoup
from pprint import pprint

url = 'https://www.daum.net'

response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
rankings = data.select('#wrapSearch > div.slide_favorsch > ul:nth-child(2)')

pprint(rankings)

for rank in rankings:
    print(rank.text)