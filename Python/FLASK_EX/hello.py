from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('index.html')

@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY!'

from datetime import datetime

@app.route('/dday')
def dday():
    today = datetime.now()
    endgame = datetime(2020, 11, 29)
    td = endgame - today
    return f'{td.days}일 남았습니다.'

@app.route('/html')
def html():
    return '<h1>This is HTML H1 tag!</h1>'

@app.route('/html_line')
def html_line():
    return '''
    <h1>여러줄을 보내봅시다</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    '''

@app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다! {name}님'
    return render_template('greeting.html', html_name=name)

@app.route('/cube/<int:number>')
def cube(number):
    result = number ** 3
    # return f'{number}의 세제곱은 {result}입니다.'
    return render_template('cube.html', number=number, result=result)

import random

@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면','짬뽕','볶음밥','고추잡채밥','마파두부밥']
    order = random.sample(menu, people)
    return str(order)

@app.route('/movie')
def movie():
    movies = ['겨울왕국2','백두산','머니게임','포드vs페라리']
    return render_template('movie.html', movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age=age)

@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')
    flist = ['잘생김','못생김','어중간한']
    slist = ['재력','체력','지능','센스','개념']
    tlist = ['허세','식욕','물욕','성욕']

    first = random.choice(flist)
    second = random.choice(slist)
    third = random.choice(tlist)
    return render_template('godmademe.html', name=name, first=first, second=second, third=third)

import requests

@app.route('/ascii')
def ascii():
    return render_template('ascii.html')

@app.route('/art')
def arg():
    word = request.args.get('word')
    font_list = requests.get(f'http://artii.herokuapp.com/fonts_list').text
    fonts = font_list.split('\n')
    font = random.choice(fonts)
    result = requests.get(f'http://artii.herokuapp.com/make?text={word}&font={font}').text
    return render_template('art.html', result=result)

@app.route('/isitbirth')
def isitbirth():
    today = datetime.now()
    if today.month == 6 and today.day == 27:
        result = True
    else:
        result = False
    return render_template('isitbirth.html', result=result)

from bs4 import BeautifulSoup
# from decouple import config

@app.route('/dust')
def dust():
    api_key = '###'
    url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={api_key}&numOfRows=40&pageNo=1&startPage=3&sidoName=서울&ver=1.6'

    today = datetime.now()
    response = requests.get(url).text
    data = BeautifulSoup(response, 'xml')
    location = data('item')[27]

    dust = int(location.pm10Value.text)
    station = location.stationName.text

    if 150 < dust:
        dust_rate = '매우 나쁨'
    elif 80 < dust <= 150:
        dust_rate = '나쁨'
    elif 30 < dust <= 80:
        dust_rate = '보통'
    else:
        dust_rate = '좋음'

    return render_template('dust.html', today=today, dust_rate=dust_rate, station=station)

if __name__=='__main__':
    app.run(debug=True)