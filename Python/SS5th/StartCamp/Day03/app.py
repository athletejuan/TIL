from flask import Flask
# templates 사용시
# from flask import render_template, request
import requests
from datetime import datetime
import random
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY!'

@app.route('/lotto')
def lotto():
    numbers = range(1, 46)
    lucky = random.sample(numbers, 6)
    return f'{lucky}'


@app.route('/today')
def today():
    today = datetime.now()
    return f'오늘은 {today}!'

# 5월 28일 까지 남은 d-day 출력
@app.route('/dday')
def dday():
    today = datetime.now()
    endgame = datetime(2021, 5, 28)
    td = endgame - today
    return f'{td.days} 일 남았습니다.'

@app.route('/love')
def love():
    today = datetime.now()
    start = datetime(2021, 1, 15)
    love = today - start
    return f'러부러부 {love.days + 1} 일'

@app.route('/isitbirth')
def birth():
    today = datetime.now()
    if today.month == 6 and today.day == 27:
        return '예'
    else:
        return '아니오'


@app.route('/greeting/<name>')
def greeting(name):
    return f'반갑습니다! {name}님!'

@app.route('/posts/<int:number>')
def post(number):
    return f'{number}번 글을 보러 오셨군요!'

# optional
@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3}입니다.'

@app.route('/even/<int:number>')
def even(number):
    if number % 2 == 1:
        msg = '홀수'
    else:
        msg = '짝수'
    return msg


# # render template
# @app.route('/html')
# def html():
#     return '<h1>This is HTML h1 tag!</h1>'

# @app.route('/html2')
# def html2():
#     return '''
#     <h1>SSAFY</h1>
#     <ul>
#         <li>코딩</li>
#         <li>알고리즘</li>
#     </ul>
#     '''

# @app.route('/lunch')
# def lunch():
#     menu = ['짜장면', '짬뽕', '탕수육', '팔보채', '볶음밥']
#     lunch = random.choice(menu)
#     return str(lunch)

# @app.route('/movie')
# def movie():
#     movies = ['한국영화', '미국영화', '홍콩영화']
#     return render_template('movie.html', movies=movies)

# @app.route('/ping')
# def ping():
#     return render_template('ping.html')

# @app.route('/pong')
# def pong():
#     age = request.args.get('age')
#     return render_template('pong.html', age_in_html=age)

# @app.route('/naver')
# def naver():
#     return render_template("naver.html")

# @app.route('/google')
# def google():
#     return render_template("google.html")


# @app.route('/vonvon')
# def vonvon():
#     return render_template('vonvon.html')

# @app.route('/godmademe')
# def godmademe():
#     name = request.args.get('name')
#     first_list = ['잘생김', '못생김', '어중간한']
#     second_list = ['자신감', '쑥스러움', '애교', '잘난척']
#     third_list = ['허세', '돈복', '식욕', '물욕', '성욕']
    
#     first = random.choice(first_list)
#     second = random.choice(second_list)
#     third = random.choice(third_list)
#     return render_template('godmademe.html', name=name, first=first, second=second, third=third)


# @app.route('/dust')
# def dust():
#     key = 'API_KEY'
#     url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=10&pageNo=2&sidoName=서울&ver=1.0&returnType=json'
#     response = requests.get(url).json()
#     item = response.get('response').get('body').get('items')[9]
#     now = item.get('dataTime')
#     station = item['stationName']
#     dust = int(item.get('pm10Value'))
#     # ultrafine = int(item.get('pm25Value'))

#     if (150 < dust):
#         grade = '매우나쁨'
#     elif (80 < dust):
#         grade = '나쁨'
#     elif (30 < dust):
#         grade = '보통'
#     else:
#         grade = '좋음'

#     today = datetime.now()
#     return render_template('dust.html', station=station, dust=dust, grade=grade, today=today, now=now)

if __name__ == '__main__':
    app.run(debug=True)