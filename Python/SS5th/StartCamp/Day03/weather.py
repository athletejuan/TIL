import requests
from pprint import pprint

url = 'https://www.metaweather.com/api/location/1132599/'

res = requests.get(url).json()
# pprint(res)

location = res['title']

# 6일치 날씨 예보
# weathers = res['consolidated_weather']
# for weather in weathers:
#     date = weather['applicable_date']
#     sky = weather['weather_state_name']
#     temp = round(weather['the_temp'], 1)
#     max_temp = round(weather['max_temp'], 1)
#     min_temp = round(weather['min_temp'], 1)
#     print(f'{date}일 {location}의 날씨는 {sky}로 예상되며 현재 기온은 {temp}도, 최고 기온은 {max_temp}도, 최저 기온은 {min_temp}도 로 예상됩니다.')  

# 오늘 날씨 예보
date = res['consolidated_weather'][0]['applicable_date']
weather = res['consolidated_weather'][0]['weather_state_name']
# temp = round(res['consolidated_weather'][0]['the_temp'], 1)
max_temp = round(res['consolidated_weather'][0]['max_temp'], 1)
min_temp = round(res['consolidated_weather'][0]['min_temp'], 1)

print(f'{date}일 {location}의 날씨는 {weather}로 예상되며, 최고 기온은 {max_temp}도, 최저 기온은 {min_temp}도 로 예상됩니다.')