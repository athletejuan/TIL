import requests

url = 'https://www.naver.com'
response = requests.get(url)
print(response.text)