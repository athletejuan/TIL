import requests
import csv
from bs4 import BeautifulSoup

melon_url = 'https://www.melon.com/chart/index.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}
response = requests.get(melon_url, headers=headers).text

data = BeautifulSoup(response, 'html.parser')
songs = data.select('#frm > div > table > tbody > tr')

result_list = []
for idx, song in enumerate(songs, 1):
    name = song.select_one('td:nth-child(4) > div > div > div.ellipsis.rank01 > span > a').text
    # 대표가수 1명만
    # artist = song.select_one('td:nth-child(4) > div > div > div.ellipsis.rank02 > a').text
    # 가수 여러명인 경우 고려시
    artists = song.select('td:nth-child(4) > div > div > div.ellipsis.rank02 > span.checkEllipsis')
    result_dict = {'rank': idx, 'name': name, 'artist': ''.join([artist.text for artist in artists])}
    result_list.append(result_dict)
# print(result_list)

with open('melon_rank_200717.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ('rank', 'name', 'artist')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in result_list:
        writer.writerow(item)