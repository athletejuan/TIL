from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template()

@app.route('/cube/<num>')
def cube(num):
    # num을 세제곱하여 보내준다.
    return str(int(num) ** 3)