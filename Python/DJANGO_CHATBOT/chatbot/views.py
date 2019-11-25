from django.shortcuts import render, redirect
from decouple import config
from django.views.decorators.csrf import ensure_csrf_cookie
import requests
import random
import json

base = "https://api.telegram.org"
token = config('TELEGRAM_TOKEN')
ngrok = config('NGROK')

@ensure_csrf_cookie
def chatting(request):
    url = f'{base}/bot{token}/setWebhook?url={ngrok}/{token}'
    # 그대로 전송
    requests.get(url).json()

    # res = request.get_json()
    body = request.body.decode('utf-8')
    res = json.loads(body)
    print(res)

    # text = res.get('message').get('text')
    # chat_id = res.get('message').get('chat').get('id')

    if res.get('message'):
        text = res.get('message').get('text')
        if text == 'lotto':
            text = str(sorted(random.sample(range(1,46),6)))
        chat_id = res.get('message').get('chat').get('id')
        method = "sendMessage"

    # if text == 'lotto':
    #     text = str(sorted(random.sample(range(1,46),6)))

        url = f'{base}/bot{token}/{method}?chat_id={chat_id}&text={text}'
        requests.get(url)
    return '', 200