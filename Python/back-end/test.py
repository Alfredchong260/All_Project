from flask import Flask, request, render_template, make_response, abort

app = Flask(__name__)

@app.route('/')
def index():
    print(request.headers)
    print(request.url)
    print(request.args)
    return '<h1>Hello</h1>', 204

@app.route('/login', methods=['POST', 'GET'])
def login():
    response = make_response('make response test')
    response.headers['code'] = "Python"
    response.status = "404 not found"
    return response

@app.route('not_found')
def not_found():
    abort(502)
    return '页面不存在'