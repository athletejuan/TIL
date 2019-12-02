import random
from bs4 import BeautifulSoup
from datetime import datetime
from flask import Flask
import requests
app = Flask(__name__)

# 1. 주문을 받는 방식(어떻게)
@app.route("/")
# 2. 무엇을 제공할지(무엇)
def hello():
    return "Hello World!"

@app.route("/hi")
def hi():
    return "hi"

# 1. /name
# 2. 영문이름

@app.route("/name")
def name():
    return "juan"

@app.route("/morning/juan")
def morning():
    return "good morning, juan"

# variable routing
@app.route("/afternoon/<person>")
def afternoon(person):
    # return "hello " + person
    return f"hello {person}"

# /cube/1 => 1
# /cube/2 => 8
# /cube/3 => 27
@app.route("/cube/<num>")
def cube(num):   
    result = int(num)**3
    return str(result)

# 1. /lotto => lotto 추천
@app.route("/lotto")
def lotto():
    return str(sorted(random.sample(range(1,46), 6)))

# 2. /lunch => 점심 메뉴 추천
@app.route("/lunch")
def lunch():
    menu = ["burger","pizza","pasta"]
    return str(random.choice(menu))

# 3. /kospi => kospi 지수 출력
@app.route("/kospi")
def kospi():
    url = 'https://finance.naver.com/sise/'
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'html.parser')
    kospi = soup.select_one('#KOSPI_now')
    return str(kospi)

# newyear
@app.route("/newyear")
def newyear():
    month = datetime.now().month
    day = datetime.now().day
    # 만약 오늘이 1월 1일이라면
    if month == 1 and day == 1:        
        return "<h1>예</h1>"
    else:        
        return "<h1>아니오</h1>"
    # return str(month) + "월" + str(day) + "일"

# /index
@app.route("/index")
def index():
    return "<html><head><body><h1>HomePage</h1><p>contents</p></body></head></html>"