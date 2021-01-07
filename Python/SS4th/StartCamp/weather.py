import requests
from decouple import config

W_KEY = config('WEATHER_API_KEY')
url = f'http://api.openweathermap.org/data/2.5/weather?q=Seoul,kr&appid={W_KEY}'
res = requests.get(url).json()

city = res['name']
weather = res['weather'][0]['main']
temp = res['main']['temp'] - 273.15
# max_temp = float(res['main']['temp_max']) - 273.15
# min_temp = float(res['main']['temp_min']) - 273.15

# print(f'{city}의 현재 날씨는 {weather}이며, {temp:.1f}도 입니다.')
print('{}의 현재 날씨는 {}이며, {:.1f}도 입니다.'.format(city, weather, temp))