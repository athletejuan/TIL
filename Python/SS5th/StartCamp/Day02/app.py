from flask import Flask, render_template, request
from datetime import datetime
import random
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('index.html')

@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY!'

@app.route('/lotto')
def lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    # return f'{lucky}'
    return render_template('lotto.html', numbers=lucky)


@app.route('/today')
def today():
    today = datetime.datetime.now()
    # return f'오늘은 {today}!'
    return render_template('today.html', today=today)

# 5월 28일 까지 남은 d-day 출력
@app.route('/dday')
def dday():
    today = datetime.now()
    endgame = datetime(2021, 5, 28)
    td = endgame - today
    # return f'{td.days} 일 남았습니다.'
    return render_template('dday.html', td=td)

@app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다! {name}님!'
    # return render_template('greeting.html', name=name)
    return render_template('greeting.html', html_name=name)

@app.route('/posts/<int:number>')
def post(number):
    return f'{number}번 글을 보러 오셨군요!'

# optional
@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3}입니다.'
    # result = number**3
    # return render_template('cube.html', result=result, number=number)

@app.route('/even/<int:number>')
def even(number):
    if number % 2 == 1:
        msg = '홀수'
    else:
        msg = '짝수'
    return msg


# render template
@app.route('/html')
def html():
    return '<h1>This is HTML h1 tag!</h1>'

@app.route('/html2')
def html2():
    return '''
    <h1>SSAFY</h1>
    <ul>
        <li>코딩</li>
        <li>알고리즘</li>
    </ul>
    '''

@app.route('/lunch')
def lunch():
    menu = ['짜장면', '짬뽕', '탕수육', '팔보채', '볶음밥']
    lunch = random.choice(menu)
    # return str(order)
    return render_template('lunck.html', lunch=lunch)

@app.route('/movie')
def movie():
    movies = ['한국영화', '미국영화', '홍콩영화']
    return render_template('movie.html', movies=movies)

@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    age = request.args.get('age')
    return render_template('pong.html', age_in_html=age)

@app.route('/naver')
def naver():
    return render_template("naver.html")

@app.route('/google')
def google():
    return render_template("google.html")


@app.route('/vonvon')
def vonvon():
    return render_template('vonvon.html')

@app.route('/godmademe')
def godmademe():
    name = request.args.get('name')
    first_list = ['잘생김', '못생김', '어중간한']
    second_list = ['자신감', '쑥스러움', '애교', '잘난척']
    third_list = ['허세', '돈복', '식욕', '물욕', '성욕']
    
    first = random.choice(first_list)
    second = random.choice(second_list)
    third = random.choice(third_list)
    return render_template('godmademe.html', name=name, first=first, second=second, third=third)


@app.route('/dust')
def dust():
    key = 'API_KEY'
    url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?ServiceKey={key}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'
    res = requests.get(url).text
    data = BeautifulSoup(res, 'xml')
    item = data('item')[7]
    station = item.stationName.text
    dust = item.pm10Value.text
    grade = item.pm10Grade.text
    if grade == '1':
        grade = '좋음'
    elif grade == '2':
        grade = '보통'
    elif grade == '3':
        grade = '나쁨'
    else:
        grade = '매우나쁨'
    now = item.dataTime.text
    today = datetime.now()
    return render_template('dust.html', data=data, station=station, dust=dust, grade=grade, today=today, now=now)

if __name__ == '__main__':
    app.run(debug=True)