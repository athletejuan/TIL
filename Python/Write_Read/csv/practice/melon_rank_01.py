from bs4 import BeautifulSoup
import csv
import requests
from pprint import pprint

melon_url = 'https://www.melon.com/chart/index.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

response = requests.get(melon_url, headers=headers).text
# pprint(response)

data = BeautifulSoup(response, 'html.parser')
# print(data)

songs = data.select('#lst50')
# print(songs)

result_list = []
for song in songs:
    rank = song.select_one('td:nth-child(2) > div > span.rank').text
    name = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank01 > span > a').text
    # artist = song.select_one('td:nth-child(6) > div > div > div.ellipsis.rank02 > a').text
    # artists = song.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > a')
    artists = song.select('td:nth-child(6) > div > div > div.ellipsis.rank02 > span.checkEllipsis')
    # result_dict = {'rank': rank, 'name': name, 'artist': artist}
    # result_dict = {'rank': rank, 'name': name, 'artist': ','.join([artist.text for artist in artists])}
    result_dict = {'rank': rank, 'name': name, 'artist': [artist.text for artist in artists]}
    result_list.append(result_dict)
# print(result_list)

with open('melon_rank_01.csv', 'w', encoding='utf-8', newline='') as csvfile:
    fieldnames = ('rank','name','artist')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for item in result_list:
        writer.writerow(item)