import json

from flask import jsonify, Flask, render_template, request, make_response, abort, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    # request 请求体对象, 浏览器传递过来的请求报文
    print('请求拥有的方法:\t', dir(request))
    print('请求方法:\t', request.method)
    print('请求头:\t', request.headers)
    print('请求地址:\t', request.url)
    print('请求参数:\t', request.args)
    return render_template('index.html')


@app.route('/login', methods=['POST'])  # login 登录只允许 post 请求
def login():
    # request 请求体对象, 浏览器传递过来的请求报文
    print('request.files:\t', request.files)
    # get 请求只有查询参数 request.args
    # post 提交后端才可以获取到提交参数
    print('request.form:\t', request.form)
    print('request.form:\t', request.form.get('comment'))
    # post 登录请求,登录成功之后应该调转到  /foo 如果登录失败 调转到 /
    # return render_template('index.html')  # 直接返回 index.html
    # redirect 后端调转到其他视图函数
    # return redirect('/')  # 直接返回 index.html
    # return redirect('/foo')  # 直接返回 index.html
    # url_for('foo') --> '/foo'
    return redirect(url_for('foo'))  # 直接返回 index.html


@app.route('/response', methods=['GET'])
def response_view():
    # return '<h1>Hello, Flask!</h1>', 201
    response = make_response('make response测试')
    response.headers["code"] = "Python"
    response.status = "404 not found"
    return response


@app.route('/not_found')
def not_found():
    abort(502)  # abort 服务器主动抛出错误
    return '页面不存在'


@app.route('/foo')
def foo():
    data = {'姓名': '张三', '性别': '男'}
    response = make_response(json.dumps(data))
    response.mimetype = 'application/json'
    # return response
    return data  # flask 2.x 版本可以直接返回字典
