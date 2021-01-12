import requests

name = 'juan'
url = f'https://api.nationalize.io/?name={name}'
response = requests.get(url).json()
print(response)

name = response['name']
country_id = response['country'][0]['country_id']
country_probability = response['country'][0]['probability'] * 100

print(f'{name}의 국적은 {country_probability}%로 {country_id}입니다.')