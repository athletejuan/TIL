from flask import Flask, render_template
import requests
import random
app2 = Flask(__name__)

@app2.route("/")
def home():
    return render_template('home.html')

@app2.route("/lotto")
def lotto():
    lotto = sorted(random.sample(range(1,46),6))
    url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=866"
    res = requests.get(url)
    dict_lotto = res.json()
    winner = []
    for i in range(1,7):
        winner.append(dict_lotto[f'drwtNo{i}'])
    count = 0
    for i in lotto:
        for j in winner:
            if i == j:
                count += 1
    if count == 6:
        rank = '1등'
    elif count == 5:
        rank = '3등'
    elif count == 4:
        rank = '4등'
    elif count == 3:
        rank = '5등'
    else:
        rank = '꽝꽝꽝'
    return render_template('lotto.html', lotto=lotto, winner=winner, rank=rank)

if __name__ == "__main__":
    app2.run(debug=True)