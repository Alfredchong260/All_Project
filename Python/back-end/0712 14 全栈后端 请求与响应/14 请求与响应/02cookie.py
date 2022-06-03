import json

from flask import jsonify, Flask, render_template, request, make_response, abort, url_for, redirect

app = Flask(__name__)


@app.route('/login', methods=["GET", "POST"])
def index():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == "POST":
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        print(email, pwd)
        # 登录成功之后记录一下邮箱
        response = make_response(redirect(url_for('admin')))
        response.set_cookie('email', email)  # 将身份信息设置到 cookies
        return response


@app.route('/admin')
def admin():
    # 在后端页面拿到前段页面的登录 邮箱
    email = request.cookies.get('email')

    return render_template('admin.html', email=email)


@app.route('/set_cookie')
def set_cookie():
    response = make_response('设置 cookie')
    response.set_cookie('username', 'tom', max_age=3600)
    return response


@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username', 'none')
    return "cookie 中的名字为：" + username


@app.route('/del_cookie')
def del_cookie():
    response = make_response('删除cookie')
    # response.set_cookie('username', '', expires=0)
    response.delete_cookie('username')
    return response
