import json

from flask import jsonify, Flask, render_template, request, make_response, abort, url_for, redirect, session, g, current_app

app = Flask(__name__)


@app.route('/')
def index():
    # current_app --> app
    print(current_app.config)
    return 'hello world !'


@app.route('/login')
def login():
    return 'login'


@app.route('/logout')
def logout():
    return 'logout'


@app.route('/user')
def user():
    # email = request.cookies.get('email', None)
    print('user email:\t', g.email)
    search_by_name()
    return 'user'


@app.before_request
def before_request():
    email = request.cookies.get('email', None)
    # g 可以理解为一次请求里面的全局对象
    g.email = email
    print('before_request email:\t', email)


def search_by_name():
    # query(name)
    print('search_by_name:\t', g.email)
