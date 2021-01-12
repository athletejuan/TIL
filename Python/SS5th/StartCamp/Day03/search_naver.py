import requests 

# 함수일 필요 없지만, 정의하는 연습을 해봅시다.
def search_naver(query):
    naver_client_id = 'NAVER_CLIENT_ID'
    naver_client_secret = 'NAVER_CLIENT_SECRET'
    URL = 'https://openapi.naver.com/v1/search/shop.json?query='

    headers = {
        'X-Naver-Client-Id': naver_client_id,
        'X-Naver-Client-Secret': naver_client_secret,
    }
    
    result = requests.get(URL+query, headers=headers)
    product = result.json()['items'][0]
    message = f"{product['title']}\n{product['lprice']}원\n{product['link']}"
    return message


def send_telegram_message(message):
    bot_token = 'TOKEN'
    my_chat_id = 'CHAT_ID'

    telegram_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?'
    query = f'chat_id={my_chat_id}&text={message}'
    
    requests.get(telegram_url+query)


message = search_naver('PS5')  # 원하는 상품명
send_telegram_message(message)
