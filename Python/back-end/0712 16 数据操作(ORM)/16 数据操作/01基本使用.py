from flask import Flask
# 1. 导入 flask-sqlalchemy 插件对象
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# 2. 提前加载数据库配置
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///school.db'
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:root@127.0.0.1/school'
    SQLALCHEMY_ECHO = True


app.config.from_object(Config)

# 3. 创建数据库链接对象
db = SQLAlchemy()

# 4. 将数据库链接对象绑定到 app 对象
db.init_app(app)


# 5. 创建数据模型
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=20))
    math = db.Column(db.Integer)
    chinese = db.Column(db.Integer)
    english = db.Column(db.Integer)


class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=20), unique=True, index=True)


@app.route('/')
def index():
    return 'hello world !'


@app.cli.command()
def create():
    db.create_all()  # 创建数据表
    # db.drop_all()  # 删除数据表
