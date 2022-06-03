# 1. 导入 Flask 对象
from flask import Flask
from werkzeug.routing import BaseConverter


class MobileConverter(BaseConverter):
    """
    手机号格式
    """
    regex = r'1[3-9]\d{9}'


# 2. 创建一个 flask 应用程序
app = Flask(__name__)

# 将自定义转换器添加到转换器字典中，并指定转换器使用时名字为: mobile
app.url_map.converters['mobile'] = MobileConverter


@app.route('/')
def index():
    return '<h1>Hello world!</h1><img src="https://www.python.org/static/img/python-logo.png">'


# app.route 路由
@app.route('/home')
def home():
    return 'welcome to flask !'


# 一个视图可以绑定多个路由
@app.route('/index')
@app.route('/admin')
def admin():
    return 'welcome to index !'


# @app.route('/user/1')
# def user1_home():
#     return 'user 1'
#
#
# @app.route('/user/2')
# def user2_home():
#     return 'user 2'

@app.route('/user/<int:user_id>')
def user1_home(user_id):
    print(type(user_id), user_id)
    return f'user {user_id}'


@app.route('/send/<mobile:phone_number>')
def go_back(phone_number):
    # 查询数据库 电话号码是否存在
    return '<p>信息已经发送到 %s !</p>' % phone_number


"""
Endpoint(端点 函数)  Methods(请求方法)  Rule(路由规则)

url_for('Endpoint') --> Rule
"""
