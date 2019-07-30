# SSAFY Day 3

## SSAFY 최종 목표: telegram 기반의 chatbot

### Today 목표: 경량형 web server 구축



1. Github TIL 중요성, IT 각 분야 성공사례, MVP, Software Engineering
2. flask intro(variable routing)
3. flask 연습(계산기, 로또, 점심메뉴, 코스피)
4. flask contents formatting HTML 문서 작성
5. flask HTML serving



flask 활용법

python flask

isitchristmas



from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")

def home():

​    return render_template('home.html')



@app.route("/hello/<name>")

def hello(name):

​    \# name에는 /hello/이름/ 활용가능

​    return render_template('hello.html', name=name)



@app.route("/menu")

def menu():

​    menus = ["burger","pizza","pasta","chicken","sandwich"]

​    choice = random.choice(menus)

​    images = {

​        "burger":"https://tmbidigitalassetsazure.blob.core.windows.net/secure/RMS/attachments/37/1200x1200/exps28800_UG143377D12_18_1b_RMS.jpg",

​        "pizza":"https://img.buzzfeed.com/thumbnailer-prod-us-east-1/dc23cd051d2249a5903d25faf8eeee4c/BFV36537_CC2017_2IngredintDough4Ways-FB.jpg",

​        "pasta":"https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/spaghetti-bolognese_2.jpg",

​        "chicken":"https://s23991.pcdn.co/wp-content/uploads/2013/10/batter-fried-chicken-recipe-fp.jpg",

​        "sandwich":"https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/egg-cress-club-sandwich_0.jpg"

​    }

​    image = images[choice]

​    \# 랜덤으로 음식메뉴 추천하고 해당음식 사진 보여주는 기능 구현

​    return render_template('menu.html', name=choice, image=image)



if __name__ == "__main__":

​    app.run(debug=True)



count = len(set(winner) & set(your_lotto))



https://github.com/sspy21