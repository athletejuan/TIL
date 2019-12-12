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

@app.route('/lotto')
def lotto():
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=888')
    lotto = res.json()

    # 당첨번호 6개만 가져오기
    winner = []
    for i in range(1, 7):
        winner.append(lotto[f'drwtNo{i}'])

    # 랜덤 로또번호 리스트 만들기
    numbers = sorted(random.sample(range(1,46),6))
        
    matched = 0
    for num in numbers:
        if num in winner:
            matched += 1

    # matched = len(set(winner) & set(numbers))
    cnt = 0
    while matched < 4:
        numbers = sorted(random.sample(range(1,46),6))
        matched = 0
        for num in numbers:
            if num in winner:
                matched += 1
        cnt += 1
        print(f'{cnt}번째 구입한 로또번호')
        print(winner)
        print(numbers)
        if matched == 6:
            print('1등입니다!!!')
        elif matched == 5:
            if lotto['bnusNo'] in numbers: # 보너스 번호 확인
                print('2등입니다!!')
            else:
                print('3등입니다!')
        elif matched == 4:
            print('4등입니다.')
        elif matched == 3:
            print('5등입니다..')
        else:
            print('꽝입니다..')
    return '', 200

@app.route('/movie')
def movie():
    movies = ['겨울왕국2','머니게임','백두산','블랙위도우']
    return render_template('movie.html', movies=movies)

@app.route('/menu')
def menu():
    list = ["20층","짜장면","김밥","타코"]
    dict = {
        "20층":'http://mblogthumb2.phinf.naver.net/MjAxOTA0MjNfMjMw/MDAxNTU2MDAwMzY5NDA5.S5bjJfRukZcs_VFvFu67K0qppWGmC3zSXrDTPGKJiosg.4zRFCwlzT82cl3RYYqEAiV5fhgcAFtwR8Z0S24kV3msg.JPEG.ha00kim/IMG_20190423_124048605.jpg?type=w800',
        "짜장면":'http://recipe1.ezmember.co.kr/cache/recipe/2016/07/02/40c4f639ca973d9acccecdf7cbe0cbc41.jpg',
        "김밥":'http://www.nongsaro.go.kr/ps/img/interabang/num207/headerImg.jpg',
        "타코":'https://storage.googleapis.com/cbmpress/uploads/sites/2/2017/04/Taco-Bell.png'
    }
    pick = random.choice(list)
    url = dict[pick]
    return render_template("menu.html", pick=pick, url=url)


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

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    num = request.args.get('num')
    # numbers = request.args.get('numbers')
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}'
    lotto = requests.get(url).json()
    
    winner = []
    # 당첨번호 6개 가져오기
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])
    
    bonus = lotto['bnusNo']

    # 내 번호 리스트로 만들기
    numbers = []
    for num in request.args.get('numbers').split():
        numbers.append(int(num))
    
    if len(numbers) == 6:
        match = 0
        for num in numbers:
            if num in winner:
                match += 1
        # match = len(set(winner) & set(numbers))
        if match == 6:
            result = ('1등 당첨')
        elif match == 5:
            if lotto['bnusNo'] in numbers:
                result =('2등 당첨')
            else:
                result =('3등 당첨')
        elif match == 4:
            result =('4등 당첨')
        elif match == 3:
            result =('5등 당첨')
        else:
            result =('BBomb')
    else:
        result = '번호가 6개가 아닙니다.'
    return render_template('lotto_result.html', winner=winner, bonus=bonus, numbers=numbers, result=result)

if __name__=='__main__':
    app.run(debug=True)