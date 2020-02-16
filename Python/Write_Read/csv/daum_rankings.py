import requests
from bs4 import BeautifulSoup
from pprint import pprint as pp
import csv

url = 'https://www.daum.net'

response = requests.get(url).text
data = BeautifulSoup(response, 'html.parser')
rankings = data.select('#mArticle > div.cmain_tmp > div.section_media > div.hotissue_builtin > div.realtime_part > ol > li > div > div:nth-child(1) > span.txt_issue > a')

# pprint(rankings)

# DictWriter

# result_dict = {}
result_list = []
for idx, ranking in enumerate(rankings, 1):
    # print(f'{idx}위: {ranking.text}')
    # 데이터를 딕셔너리로 만들기
    # result_dict[f'{idx}위'] = ranking.text
    # 데이터를 json 처럼 만들기
    result_dict = {'rank': f'{idx}위', 'ranker': ranking.text}
    # result_dict = dict({'rank': f'{idx}위, 'ranker': ranking.text})
    # result_dict = dict([('rank', f'{idx}위'), ('ranker', ranking.text)])
    result_list.append(result_dict)
pp(result_list)

with open('daum_rank.csv','w', encoding='utf-8', newline='') as csvfile:
    # 1 - csv.writer
    # csv_writer = csv.writer(csvfile)
    # for item in result_dict.items():
    #     csv_writer.writerow(item)
    # 2 - DictWriter
    # 저장할 데이터들의 필드 이름을 미리 지정한다. (딕셔너리의 key 이름과 일치해야 한다.)
    fieldnames = ('rank','ranker')
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    # 필드 이름을 csv 파일 최상단에 작성한다.
    writer.writeheader()
    # 리스트를 순회하며 key(csv의 필드)를 통해 value(내용)를 필드에 맞게 작성한다.
    for item in result_list:
        writer.writerow(item)
    