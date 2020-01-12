import requests
from decouple import config

key = config('GOOGLE_API_KEY')
api_url = 'https://translation.googleapis.com/language/translate/v2'
data = {'q':'반갑습니다', 'source':'ko', 'target':'en'}
response = requests.post(f'{api_url}?key={key}', data).json()
print(response)