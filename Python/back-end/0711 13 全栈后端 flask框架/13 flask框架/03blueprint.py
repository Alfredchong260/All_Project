# 1. 导入 Blueprint 蓝图对象
from flask import Flask, Blueprint

from admin import admin_bp

app = Flask(__name__)


@app.route('/')
def index():
    print(__name__)
    return 'hello flask !'


# 2. 创建一个 蓝图实例对象
# url_prefix 给蓝图对象下的所有内容添加前缀
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')


# 3. 使用蓝图注册视图
@auth_bp.route('/login')
def auth_login():
    return '登录页面'


@auth_bp.route('/logout')
def auth_logout():
    return '退出页面'


# admin_bp = Blueprint('admin', __name__)
#
#
# @admin_bp.route('/admin/home')
# def admin_home():
#     return 'admin home'
#
#
# @admin_bp.route('/admin/users')
# def admin_users():
#     return 'admin users'


# 4. 将蓝图注册到 app 对象
# app.register_blueprint(auth_bp, url_prefix='/auth')

parent = Blueprint('parent', __name__, url_prefix='/parent')
child = Blueprint('child', __name__, url_prefix='/child')


@parent.route('/bbb')
def bbb():
    return 'bbb'


@child.route('/aaa')
def aaa():
    return 'aaa'


parent.register_blueprint(child)
app.register_blueprint(parent)
app.register_blueprint(auth_bp)
app.register_blueprint(admin_bp)

# /api/v1/admin/users
# /api/v1/admin/home
# /api/v2/profile/home
