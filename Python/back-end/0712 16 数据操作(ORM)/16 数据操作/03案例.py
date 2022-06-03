from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


class Config:
    # 数据库链接配置参数
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data_03.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_ECHO = True
    SECRET_KEY = 'secret key'


app.config.from_object(Config)

# 创建数据库链接对象
db = SQLAlchemy(app)


class Students(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(length=20))
    gender = db.Column(db.String(length=20))
    birth = db.Column(db.String(length=20))
    phone = db.Column(db.String(length=20))

    def __repr__(self):
        return '<Students %s>' % self.username


@app.route('/')
def index():
    return render_template('main.html')


@app.route('/add.html')
def add_user():
    return render_template('add.html')


@app.route('/edit/<int:user_id>')
def edit_user(user_id):
    stu = Students.query.get(user_id)
    return render_template('edit.html', stu=stu)


@app.route('/users')
def users():
    # 分页信息获取
    page = request.args.get('page', type=int, default=1)
    limit = request.args.get('limit', type=int, default=10)
    username = request.args.get('username', type=str, default='')
    phone = request.args.get('phone', type=str, default='')

    filters = []
    if username:
        filters.append(Students.username.like(f'%{username}%'))
    if phone:
        filters.append(Students.phone.like(f'%{phone}%'))

    print('*filters:\t', *filters)
    _paginate = Students.query.filter(*filters).paginate(page=page, per_page=limit, error_out=False)
    print(_paginate)
    return {"code": 0,
            "message": "数据查询成功",
            "count": _paginate.total,
            "data": [{
                'id': student.id,
                'username': student.username,
                'gender': student.gender,
                'birth': student.birth,
                'phone': student.phone,
            } for student in _paginate.items],
            'success': True}


@app.post('/users/add')
def users_add():
    # {"username":"正心","gender":"男","birth":"123","phone":"123"}
    username = request.json.get('username')
    gender = request.json.get('gender')
    birth = request.json.get('birth')
    phone = request.json.get('phone')
    stu = Students()
    stu.username = username
    stu.gender = gender
    stu.birth = birth
    stu.phone = phone
    db.session.add(stu)
    db.session.commit()
    return {"code": 200, "message": "数据添加成功", 'success': True}


# 删除与修改用的同一个路由,用的不同的方法
# get post delete put
# /user/<int:user_id> 操作用户数据
@app.route('/user/<int:user_id>', methods=['DELETE', "PUT"])
def delete_user(user_id):
    if request.method == 'PUT':
        # {id: "42", username: "丸子", gender: "女", birth: "123", phone: "21321"}
        stu = Students.query.get(user_id)
        stu.username = request.json.get('username')
        stu.gender = request.json.get('gender')
        stu.birth = request.json.get('birth')
        stu.phone = request.json.get('phone')
        db.session.commit()
        return {"code": 200, "message": "修改数据成功", 'success': True}
    if request.method == 'DELETE':
        stu = Students.query.get(user_id)
        db.session.delete(stu)
        db.session.commit()
        return {"code": 200, "message": "数据删除成功", 'success': True}


@app.cli.command()
def create():
    """新增数据"""
    db.drop_all()
    db.create_all()
    from data import students
    for student in students:
        stu = Students()
        for key, value in student.items():
            setattr(stu, key, value)
        db.session.add(stu)
    # 提交数据
    db.session.commit()


@app.cli.command()
def paginate():
    """删除数据"""
    _paginate = Students.query.paginate(
        page=5,  # 查询第几页
        per_page=10,  # 每一页多少条数据
        error_out=False)
    print(paginate)
    print('当前页码：\t', _paginate.page)
    print('总页数：\t', _paginate.pages)
    print('每页的条数：\t', _paginate.per_page)
    print('总条数：\t', _paginate.total)
    print('当前页的数据：\t', _paginate.items)
