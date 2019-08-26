# 최고 중간관리자
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cube/<int:number>')
def cube(number):
    return f'{number}의 세제곱은 {number**3} 입니다.'

@app.route('/dict/<string:word>')
def my_dict(word):
    d = {
        'apple':'사과',
        'banana':'바나나',
    }
    result = d.get(word)

    return (f'{word}은(는) {result}!' if result else f'{word}은(는) 단어장에 없는 단어입니다.'
    # if result:
    #     return f'{word}은(는) {result}!'
    # else:
    #     return f'{word}은(는) 단어장에 없는 단어 입니다.'

if __name__=='__main__':
    app.run(debug=True)