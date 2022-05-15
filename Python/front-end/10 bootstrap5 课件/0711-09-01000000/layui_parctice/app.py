import json

from flask import Flask, request, render_template
from flask.views import MethodView
from models import db

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


# @app.route('/student_add')
# def student_add():
#     return render_template('index_add.html')
#

@app.route('/students', methods=['GET', 'DELETE'])
def students():  # put application's code here
    if request.method == 'GET':
        username = request.args.get('name')
        rets = []
        if username:
            sql = "select * from student_info where student_name like '%" + username + "%';"
            db.cursor.execute(sql)
            students = db.cursor.fetchall()
            for student in students:
                rets.append({
                    'id': student[0],
                    'no': student[1],
                    'name': student[2],
                    'email': student[3],
                    'gender': student[4],
                    'city': student[5],
                })
        else:
            rets = db.fetch_students()
        return {
            "code": 0,
            "message": "获取数据成功",
            "data": rets,
            "count": len(rets)
        }
    if request.method == 'DELETE':
        ids = request.json.get('ids')
        print(ids)
        rets = db.fetch_students()
        return {
            "code": 0,
            "message": "获取数据成功",
            "data": rets,
            "count": len(rets)
        }


class StudentAPI(MethodView):
    def get(self, stu_id):
        if stu_id is None:
            rets = db.fetch_students()
            return {
                "code": 0,
                "message": "获取数据成功",
                "data": rets,
                "count": len(rets)
            }
        else:
            # 显示一个用户
            sql = "select * from student_info where id='" + str(stu_id) + "';"
            db.cursor.execute(sql)
            student = db.cursor.fetchone()
            return {
                "code": 0,
                "message": "获取数据成功",
                "data": {
                    'id': student[0],
                    'no': student[1],
                    'name': student[2],
                    'email': student[3],
                    'gender': student[4],
                    'city': student[5],
                },
            }

    def post(self):
        # 创建一个新用户
        print(request.json)
        no = request.json.get('no')
        name = request.json.get('name')
        email = request.json.get('email')
        gender = request.json.get('gender')
        city = request.json.get('city')
        sql = f"insert into student_info (`student_id`, `student_name`, `email`, `sex`, `city`) values ('{no}', '{name}', '{email}', '{gender}', '{city}');"
        db.cursor.execute(sql)
        db.conn.commit()
        return {
            "code": 1,
            "message": "获取数据成功",
        }

    def delete(self, stu_id):
        # 删除一个用户
        sql = "DELETE FROM student_info WHERE id='" + str(stu_id) + "';"
        db.cursor.execute(sql)
        db.conn.commit()
        return {
            "code": 1,
            "message": "删除数据成功",
        }

    def put(self, stu_id):
        # update a single user
        # `student_id`, `student_name`, `email`, `sex`, `city`
        print(request.json)
        no = request.json.get('no')
        name = request.json.get('name')
        email = request.json.get('email')
        gender = request.json.get('gender')
        city = request.json.get('city')
        sql = f"UPDATE student_info SET student_id='{no}',student_name='{name}',email='{email}',sex='{gender}',city='{city}' WHERE id='{stu_id}';"
        db.cursor.execute(sql)
        db.conn.commit()
        return {
            "code": 1,
            "message": "修改数据成功",
        }


student_view = StudentAPI.as_view('student_api')
app.add_url_rule('/student/', view_func=student_view, methods=['POST', ])
app.add_url_rule('/student/', defaults={'stu_id': None}, view_func=student_view, methods=['GET', ])
app.add_url_rule('/student/<int:stu_id>', view_func=student_view, methods=['GET', 'PUT', 'DELETE'])

"""
    sql --> python --> excel/word/... --> 浏览器

"""