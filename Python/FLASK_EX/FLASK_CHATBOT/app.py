from flask import Flask, render_template, request
import requests
from decouple import config
app = Flask(__name__)

token = config('TOKEN')
chat_id = config('CHAT_ID')
app_url = f'https://api.telegram.org/bot{token}'

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

if __name__=='__main__':
    app.run(debug=True)
