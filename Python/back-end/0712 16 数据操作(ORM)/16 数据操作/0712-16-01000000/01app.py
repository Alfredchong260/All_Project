import click
from flask_migrate import Migrate

"""
    1. 新建一个数据库 python
    2. 使用数据迁移生成数据表
    3. 补全修改的逻辑
        3.1 在页面上新增一个修改按钮
        3.2 点就新增按钮时，将对应的数据显示到第二个表单
        3.3 修改表单提交之后，修改数据
"""
from flask import Flask, render_template, request, redirect

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config:
    SQLALCHEMY_DATABASE_URI = r'sqlite:///data_01.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True


app.config.from_object(Config)

db = SQLAlchemy()
migrate = Migrate()

db.init_app(app)
migrate.init_app(app, db)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(length=20))
    chinese = db.Column(db.Float)
    math = db.Column(db.Float)
    english = db.Column(db.Float)

    def __repr__(self):
        return '<Student {} {},{},{}>'.format(self.name, self.chinese, self.math, self.english)


@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


@app.route('/insert', methods=["POST"])
def insert():
    data = request.form
    print(data)
    stu = Student(
        name=data.get('username'),
        chinese=data.get('chinese'),
        math=data.get('math'),
        english=data.get('english'),
    )
    db.session.add(stu)
    db.session.commit()
    return redirect('/')


@app.route('/delete/<int:user_id>')
def delete(user_id):
    db.session.delete(Student.query.get(user_id))
    db.session.commit()
    return redirect('/')


@app.route('/change', methods=['POST'])
def change():
    data = request.form
    print(data)
    stu = Student.query.get(-1)
    print(stu)
    return render_template('/', old_stu=stu)


@app.cli.command()
def create():
    """新建数据表格"""
    db.drop_all()
    db.create_all()
