from flask import Flask, render_template, request
from faker import Faker
from bs4 import BeautifulSoup
import random
import requests
fake = Faker('ko_KR')
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/pastlife")
def pastlife():        
    return render_template('pastlife.html')

names = {}

@app.route("/result")
def result():
    # 이름과 (가짜)직업을 알려준다
    name = request.args.get('name')
    
    # 1. 우리 names에 해당하는 이름이 있는지 확인  
    # 2. 없다면 => 랜덤으로 fake 직업 보여주고 데이터에 저장
    # 3. 있다면 => names에 저장된 직업 보여줌
    if name in names:
        job = names[name]        
    else:
        job = fake.job()
        names[name] = job

    # job = fake.job()
    return render_template('result.html', name=name, job=job)

@app.route("/goonghap")
def goonghap():
    return render_template('goonghap.html')

babos = {}
@app.route("/destiny")
def destiny():
    babo = request.args.get('babo')
    you = request.args.get('you')
    # hap = random.randint(51,100)
    # 1. 이름+이름 으로 저장
    # if babo + you in babos:
    #     hap = babos[babo + you]
    # else:
    #     hap = random.randint(51,100)
    #     babos[babo+you] = hap
    # 2. dict in dict 
    if babo in babos:
        if you in babos[babo]:
            hap = babos[babo][you]
        else:
            hap = random.randint(51,100)
            babos[babo][you] = hap
    else:
        hap = random.randint(51,100)
        babos[babo] = {you: hap}

    return render_template('destiny.html', babo=babo, you=you, hap=hap)

# babos에 있는 사람 모두 출력하기
@app.route('/admin')
def admin():
    # babos dictionary에 있는 모든 데이터를 admin.html에 출력
    # babo = request.args.get(babo)
    # you = request.args.get(you)
    # hap = request.args.get(hap)
    # for k,v in babos.items():
    #     print(babos[babo])
    return render_template('admin.html', babos=babos)

@app.route('/opgg')
def opgg():
    return render_template('opgg.html')

@app.route('/search')
def search():    
    url = "https://www.op.gg/summoner/userName=" + name
    res = requests.get(url)
    name = request.args.get('name')
    doc = BeautifulSoup(res.text, 'html.parser')
    win = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    lose = doc.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div > div.TierRankInfo > div.TierInfo > span.WinLose > span.lose')
    
    return render_template('search.html', name=name, win=win, lose=lose)

if __name__ == '__main__':
    app.run(debug=True)