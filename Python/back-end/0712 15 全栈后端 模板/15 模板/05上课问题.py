from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('上课问题vue.html', items=['西瓜', '橘子', '哈密瓜'])
