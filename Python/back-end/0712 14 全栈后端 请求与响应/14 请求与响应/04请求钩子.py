import json

from flask import jsonify, Flask, render_template, request, make_response, abort, url_for, redirect, session

app = Flask(__name__)

# session 会对数据进行加密
app.secret_key = b'\x0c\x87Ty3[h\x15\x18A\x02Uk\xef\xed\xf3!\x97\xa4\x06g\x92\x17\xb2\xa7\xdd\xe9\xe0\xc6\x92\xbf\xa5'


@app.route('/')
def index():
    print('index 视图被请求了')
    return 'hello world !'


@app.route('/hello')
def hello():
    print('hello 视图被请求了')
    abort(403)
    return 'hello hello !'


# 在第一次请求之前调用，可以在此方法内部做一些初始化操作
@app.before_first_request
def before_first_request():
    print("服务器运行起来之后的第一次请求")


@app.before_request
def before_request():
    email = request.cookies.get('email', None)
    print('email:\t', email)
    # abort(403)
    # print("每一次视图函数处理之前都会调用")


@app.after_request
def after_request(response):
    print("每一次视图函数处理之后都会调用")
    # response.headers["Content-Type"] = "application/json"
    return response


# 请每一次请求之后都会调用，会接受一个参数，参数是服务器出现的错误信息
@app.teardown_request
def teardown_request(e):
    print("请每一次请求之后都会调用")


# hook

@app.errorhandler(404)
def internal_server_error(e):
    response = make_response(render_template('小米商城.html'))
    # response.mimetype = 'text/html;charset=utf-8'
    return response
