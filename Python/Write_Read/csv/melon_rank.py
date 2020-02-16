import requests
import csv
from bs4 import BeautifulSoup
from pprint import pprint

# response = requests.get('https://www.melon.com/chart/index.htm')

# print(response.status_code)
melon_url = 'https://www.melon.com/chart/index.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

response = requests.get(melon_url, headers=headers).text

# print(response.status_code)
# print(response.text)

data = BeautifulSoup(response, 'html.parser')
songs = data.select('#lst50')
result_list = []
# pprint(songs)
for song in songs:
    rank = song.select_one('td:nth-child(2) > div > span.rank').text
    name = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    artist = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    # print(f'{rank}위: {name} / {artist}')
    result_dict = {'rank': rank, 'name': name, 'artist': artist}
    result_list.append(result_dict)

with open('melon_rank.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ('rank','name','artist')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in result_list:
        writer.writerow(item)