from flask import jsonify, Flask, request, render_template, Blueprint, session, abort

""""""
"""
编写一个flask服务器，实现以下需求

get /  返回欢迎来到学生信息管理系统
get /user/<name> 返回对应学生的数据（拼接成字符串） 或者使用 jsonify(字典)进行返回
get /admin  返回字符串 '欢迎来到后台登录页面'

get /auth/login 返回登录页面的html
get /auth/logout  可以进行退出
post /auth/login  可以进行用户的校验用户名与密码，如果信息正确就可以进行登录。登录成功之后将信息记录到session

登录之后 可以进行以下操作（没有登录的需要进行拦截，提示登录之后才能进行操作）
get /user 返回录入学院信息的html(有语文、数学、英语三个input的html的表单页面，html内用jquery发送请求)
post /user/<name> 可以将提交的数据添加到 students 里面，然后返回提交信息
get /user/<name> 返回对应学生的数据（拼接成字符串） 或者使用 jsonify(字典)进行返回
"""
students = [
    {"name": "张三", "chinese": "65", "math": "65", "english": "65", "total": 195},
    {"name": "李四", "chinese": "65", "math": "65", "english": "65", "total": 195},
    {"name": "王五", "chinese": "65", "math": "65", "english": "65", "total": 195},
    {"name": "赵六", "chinese": "65", "math": "65", "english": "65", "total": 195},
]

app = Flask(__name__, static_folder="static", template_folder="templates")
app.secret_key = "123456"


@app.route("/")
def index():
    return "欢迎来到学生信息管理系统"


@app.route("/admin")
def admin_index():
    return "欢迎来到后台登录页面"


@app.route("/user/<username>")
def get_user(username):
    # 字典变量
    for stu in students:
        if stu["name"] == username:
            return jsonify(stu)
    return f"{username} 学员不存在"


auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        print(request.json)
        username = request.json.get('username')
        password = request.json.get('password')
        if username == 'admin' and password == 'admin':
            session['username'] = username
            return {'status': 'ok', 'message': '登陆成功'}
        return {'status': 'error', 'message': '登陆失败'}


@auth_bp.route("/logout")
def logout():
    del session['username']
    return {'status': 'error', 'message': '退出成功'}


app.register_blueprint(auth_bp, url_prefix="/auth")

user_bp = Blueprint("user", __name__)


@user_bp.before_request
def before_request():
    username = session.get('username', None)
    if not username:
        abort(403)
        # return {'status': 'error', 'message': '登陆之后才能进行访问'}

@user_bp.route("/")
def index_user():
    return render_template('user.html')

app.register_blueprint(user_bp, url_prefix="/user")
