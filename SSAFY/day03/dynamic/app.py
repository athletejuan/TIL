from flask import Flask, render_template
import requests
import random
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/hello/<name>")
def hello(name):
    # name에는 /hello/이름/ 활용가능
    return render_template('hello.html', name=name)

@app.route("/menu")
def menu():
    menus = ["burger","pizza","pasta","chicken","sandwich"]
    choice = random.choice(menus)
    images = {
        "burger":"https://tmbidigitalassetsazure.blob.core.windows.net/secure/RMS/attachments/37/1200x1200/exps28800_UG143377D12_18_1b_RMS.jpg",
        "pizza":"https://img.buzzfeed.com/thumbnailer-prod-us-east-1/dc23cd051d2249a5903d25faf8eeee4c/BFV36537_CC2017_2IngredintDough4Ways-FB.jpg",
        "pasta":"https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/spaghetti-bolognese_2.jpg",
        "chicken":"https://s23991.pcdn.co/wp-content/uploads/2013/10/batter-fried-chicken-recipe-fp.jpg",
        "sandwich":"https://www.bbcgoodfood.com/sites/default/files/recipe-collections/collection-image/2013/05/egg-cress-club-sandwich_0.jpg"
    }
    image = images[choice]
    # 랜덤으로 음식메뉴 추천하고 해당음식 사진 보여주는 기능 구현
    return render_template('menu.html', name=choice, image=image)

# /lotto 랜덤 넘버를 추천해주고, 최신 로또와 비교하여 등수를 알려주는 기능
@app.route("/lotto")
def lotto():
    lotto = sorted(random.sample(range(1,46),6))
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    res = requests.get(url)
    dict_lotto = res.json()
    winner=[]
    for i in range(1,7):
        winner.append(dict_lotto[f'drwtNo{i}'])
    count = 0
    for l in lotto:
        for w in winner:
            if l == w:
                count += 1
    if count == 6:
        rank = "1등"
    elif count == 5:
        rank = "3등"
    elif count == 4:
        rank = "4등"
    elif count == 3:
        rank = "5등"
    else:
        rank = "꽝"    
    return render_template('lotto.html', lotto=lotto, winner=winner, rank=rank)

if __name__ == "__main__":
    app.run(debug=True)