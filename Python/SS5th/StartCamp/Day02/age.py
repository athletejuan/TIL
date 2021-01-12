import requests


name = 'juan'
url = f'https://api.agify.io/?name={name}'
response = requests.get(url).json()
print(response)
print(type(response))

name = response['name']
age = response['age']
print(f'{name}의 나이는 {age}세 입니다.')