from flask import Flask, render_template, request
import requests
from pprint import pprint
app = Flask(__name__)

token = 'TOKEN'
chat_id = 'CHAT_ID'
app_url = f'https://api.telegram.org/bot{token}'

# 'https://api.telegram.org/bot1560662764:AAHqcSpCxTVfmNTrJF081Lwo-WvoCN8iKI4/setWebhook?url=https://a2119088a67c.ngrok.io/telegram'

@app.route('/')
def hello():
    return 'Hello World!'


@app.route('/write')
def write():
    return render_template('write.html')


@app.route('/send')
def send():
    text = request.args.get('message')
    message_url = f'{app_url}/sendMessage?chat_id={chat_id}&text={text}'
    requests.get(message_url)
    return render_template('send.html')


@app.route('/telegram', methods=['POST'])
def telegram():
    # update_url = f'{app_url}/getUpdates'
    # telegram_response = requests.get(update_url).json()
    # text = telegram_response.get('result')[-1].get('message').get('text')
    telegram_response = request.get_json()
    if telegram_response.get('message') is not None:
        chat_id = telegram_response.get('message').get('from').get('id')
        text = telegram_response.get('message').get('text')
        requests.get(f'{app_url}/sendMessage?chat_id={chat_id}&text={text}')

    return '', 200

if __name__ == '__main__':
    app.run(debug=True)