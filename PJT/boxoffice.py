import requests
from decouple import config
from datetime import datetime, timedelta, date
from pprint import pprint

API_Key = config('Movie_Key')

targetDt_list =[]
now = datetime.today().date()
# targetDt = datetime.today().strftime('%Y%m%d')
# endDt = '2019-07-13'
endDt = now + timedelta(weeks=-1)
# startDt = now + datetime.timedelta(weeks=-50)
for i in range(50):
    Dt = endDt + timedelta(weeks=-i)
    targetDt = Dt.strftime('%Y%m%d')
    targetDt_list.append(targetDt)

base = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
weekGb='0'
for targetDt in targetDt_list:
    url = f'{base}?key={API_Key}&targetDt={targetDt}&weekGb={weekGb}'
    res = requests.get(url).json()
    movies = res.get('boxOfficeResult').get('weeklyBoxOfficeList')
    result={}
    # def movie_list():
    for movie in movies:        
        # key_name = ['movieCd','movieNm','audiAcc']
        title = movie.get('movieNm')
        # for k,v in movie.items():
        if not title in result:
        # if k in key_name:
            result[title] = {
            'movieCd': movie.get('movieCd'),
            'movieNm': movie.get('movieNm'),
            'audiAcc': movie.get('audiAcc')}
            with open('boxoffice.csv','w',encoding='utf-8') as f:
                for k,v in result.items():
                    f.write(f'{k},{v} \n')

# re={}
# for key,value in result.items():
#     re={}

# with open('boxoffice.csv','w',encoding='utf-8') as f:
#     # key_name = ['movieCd','movieNm','audiAcc']
#     for k,v in result.items():          
#         f.write(f'{k},{v} \n')
