import requests
import csv
from bs4 import BeautifulSoup
from pprint import pprint

# response = requests.get('https://www.melon.com/chart/index.htm')

# print(response.status_code)
# http 상태코드 검색 -> mdn 위주로 검색
melon_url = 'https://www.melon.com/chart/index.htm'

# 개발자도구 -> newwork -> 아무거나 -> headers -> User-Agent
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

response = requests.get(melon_url, headers=headers).text

# print(response.status_code)
# print(response.text)

# 1. 순위 / 가수 / 노래제목을 뽑아서 프린트
# 2. 데이터 가공 (json 처럼 데이터 만들기)
# 3. 2번에서 만든 데이터로 csv 작성

data = BeautifulSoup(response, 'html.parser')
songs = data.select('#lst50')

result_list = []
# pprint(songs)
for song in songs:
    rank = song.select_one('td:nth-child(2) > div > span.rank').text
    title = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    # artist = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    # 가수가 여러명인 경우 select로 list 형태로 받아오는 방법
    artists = song.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
    # print(f'{rank}위: {name} / {artist}')
    # item = {'rank': rank, 'title': title, 'artist': artist}
    item = {'rank': rank, 'title': title, 'artist': ','.join([artist.text for artist in artists])}
    result_list.append(item)

with open('melon_rank.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ('rank','title','artist')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in result_list:
        writer.writerow(item)