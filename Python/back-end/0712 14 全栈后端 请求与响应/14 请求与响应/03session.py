import json

from flask import jsonify, Flask, render_template, request, make_response, abort, url_for, redirect, session

app = Flask(__name__)

# session 会对数据进行加密
app.secret_key = b'\x0c\x87Ty3[h\x15\x18A\x02Uk\xef\xed\xf3!\x97\xa4\x06g\x92\x17\xb2\xa7\xdd\xe9\xe0\xc6\x92\xbf\xa5'


@app.route('/login', methods=["GET", "POST"])
def index():  # 同时 100 人进行请求 ?
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == "POST":
        email = request.form.get('email')
        pwd = request.form.get('pwd')
        print(email, pwd)
        # 登录成功之后记录一下邮箱
        session['email'] = email  # 将身份信息设置到 cookies
        return redirect(url_for('admin'))


@app.route('/admin')
def admin():
    # 在后端页面拿到前段页面的登录 邮箱
    email = session.get('email', 'none')

    return render_template('admin.html', email=email)


@app.route('/set_cookie')
def set_cookie():
    session['username'] = 'tom'
    return '设置 cookie'


@app.route('/get_cookie')
def get_cookie():
    username = session.get('username', '')
    return "cookie 中的名字为：" + username


@app.route('/del_cookie')
def del_cookie():
    response = make_response('删除cookie')
    session['username'] = ''
    return response
