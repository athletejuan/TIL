from flask import Flask, render_template, request
import datetime
import random
import requests
app = Flask(__name__)

@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('index.html')

@app.route('/ssafy')
def ssafy():
    return 'This is SSAFY!'

@app.route('/dday')
def dday():
    today = datetime.datetime.now()
    ssafy_start = datetime.datetime(2020, 1, 13)
    td = ssafy_start - today
    return f'{td.days}일 남았습니다.'

@app.route('/html')
def html():
    return '<h1> This is HTML h1 tag!</h1>'

@app.route('/html_line')
def html_line():
    return """
    <h1>여러줄을 보내봅시다.</h1>
    <ul>
        <li>1번</li>
        <li>2번</li>
    </ul>
    """

@app.route('/greeting/<name>')
def greeting(name):
    # return f'반갑습니다! {name}님!'
    return render_template('greeting.html', name=name)

@app.route('/cube/<int:number>')
def cube(number):
    # return f'{number}의 3제곱은 {number**3} 입니다.'
    result = number**3
    return render_template('cube.html', result=result)
    # 사용자가 입력한 숫자를 받아서
    # 세제곱 후 cube.html파일을 통해 응답


@app.route('/lunch/<int:people>')
def lunch(people):
    menu = ['짜장면','짬뽕','볶음밥','고추잡채밥','마파두부밥']
    order = random.sample(menu, people)
    return str(order)

@app.route('/movie')
def movie():
    movies = ['겨울왕국2','머니게임','백두산','블랙위도우']
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
    first_list = ['잘생김','못생김','어중간']
    second_list = ['자신감','쑥스러움','애교','잘난척']
    third_list = ['허세','돈복','식욕','물욕','성욕']

    first = random.choice(first_list)
    second = random.choice(second_list)
    third = random.choice(third_list)

    return render_template('godmademe.html', name=name, first=first, second=second, third=third)

@app.route('/throw')
def throw():
    return render_template('throw.html')

# artii API를 통해 ascii 아트로 변환하여 보여주는 페이지
@app.route('/catch')
def catch():
    base = 'http://artii.herokuapp.com'
    #1. form 태그로 날린 데이터를 받는다.
    word = request.args.get('word')

    #2. ascii api로 요청을 보내 응답 결과를 text로 fonts에 저장한다.
    fonts = requests.get(f'{base}/fonts_list').text
    
    #3. fonts(str)를 fonts(list)로 바꾼다.
    fonts = fonts.split('\n')

    #4. fonts(list)안에 들어있는 요소 중 하나를 선택해서 font라는 변수에 저장.
    font = random.choice(fonts)

    #5. 위에서 만든 word와 font를 가지고 다시 요청을 보냄.
    url = f'{base}/make?text={word}&font={font}'
    result = requests.get(url).text
    return render_template('catch.html', result=result)

@app.route('/isbirth')
def isbirth():
    # 6월 27일이면 예, 아니면 아니오
    today = datetime.datetime.now()
    if today.month == 6 and today.day == 27:
        result = True
    else:
        result = False
    return render_template('isitbirth.html', result=result)

if __name__=='__main__':
    app.run(debug=True)