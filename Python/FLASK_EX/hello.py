from flask import Flask, render_template
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

if __name__=='__main__':
    app.run(debug=True)