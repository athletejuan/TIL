import requests
import bs4

url = "https://www.naver.com/"

response = requests.get(url).text

document = bs4.BeautifulSoup(response,'html.parser')

rank = document.select('.ah_k')

for item in rank:
    print(item.text)
# print(rank)