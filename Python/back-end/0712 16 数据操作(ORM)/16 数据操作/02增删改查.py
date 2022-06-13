from flask import Flask
# 1. 导入 flask-sqlalchemy 插件对象
from flask_sqlalchemy import SQLAlchemy

# from sqlalchemy import and_, or_, not_

app = Flask(__name__)


# 2. 提前加载数据库配置
class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///school.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
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

    def __repr__(self):
        return f'<Student: {self.name}>'


@app.cli.command()
def create():
    # db.drop_all()  # 删除数据表
    # db.create_all()  # 创建数据表
    """新增数据"""
    # 使用类对象创建一个实例对象 --> 数据表里面的一条数据
    stu = Student(name='正心', math=100, chinese=100, english=100)
    stu = Student()
    stu.name = '山禾'
    stu.math = 60
    stu.chinese = 60
    stu.english = 60
    # 添加一条数据
    db.session.add(stu)
    # 提交更改
    db.session.commit()
    print(stu)
    print(stu.name)
    print(stu.id)
    print(stu.chinese)


@app.cli.command()
def search():
    """查询数据"""
    # students = Student.query.all()
    # print(students)

    # student = Student.query.first()
    # student: Student = Student.query.get(1)
    # print([student, student.name, student.math, student.chinese, student.english])

    # student = Student.query.filter(Student.name == '正心').all()
    # student = Student.query.filter_by(name='正心').all()
    # student = Student.query.filter(Student.chinese >= 60).all()
    student = Student.query.filter(
        Student.chinese >= 60).filter(
        ~Student.name.like('%正%')).all()
    print(student)

    print(Student.query.with_entities(Student.name, Student.math).filter_by(name='正心').all())


@app.cli.command()
def update():
    student: Student = Student.query.get(1)
    student.math = 150
    student.english = 150
    # 提交更改
    db.session.commit()


@app.cli.command()
def delete():
    """数据删除"""
    student: [Student] = Student.query.all()
    for stu in student:
        db.session.delete(stu)
    db.session.commit()
