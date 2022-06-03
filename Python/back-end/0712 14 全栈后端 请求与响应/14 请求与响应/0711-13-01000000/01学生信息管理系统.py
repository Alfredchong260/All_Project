from flask import jsonify, Flask, render_template

""""""
"""
编写一个flask服务器，实现以下需求

get /  返回欢迎来到学生信息管理系统
get /user/<name> 返回对应学生的数据（拼接成字符串） 或者使用 jsonify(字典)进行返回
get /auth/login  返回登录页面的html。页面中需要有 form表单、用户名、密码、提交按钮组件（不需要实现登录需求）
get /admin  返回字符串 '欢迎来到后台登录页面'
"""
students = [
    {'name': '张三', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '李四', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '王五', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '赵六', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
]

app = Flask(__name__)


@app.route('/')
def index():
    return '返回欢迎来到学生信息管理系统'


@app.route('/user/<name>')
def user_name(name):
    for stu in students:
        if stu['name'] == name:
            return jsonify(stu)
    return f'{name} 学生不存在'


@app.route('/auth/login')
def login():
    return render_template('login.html')


@app.route('/admin')
def admin():
    return '欢迎来到后台登录页面'
