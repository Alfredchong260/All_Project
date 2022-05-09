import json
import random
import glob
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS().init_app(app)
app.jinja_env.variable_start_string = '%%'
app.jinja_env.variable_end_string = '%%'

students = [
    {'name': '张三', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '李四', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '王五', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
    {'name': '赵六', 'chinese': '65', 'math': '65', 'english': '65', 'total': 195},
]


@app.route('/')
def index():
    return jsonify({'status': True, 'message': '欢迎来到学生信息管理系统'})


@app.route('/get')
def ajax_get():
    return jsonify(students)


@app.route('/post', methods=["POST"])
def ajax_post():
    try:
        name = request.form.get('name')
        chinese = request.form.get('chinese')
        math = request.form.get('math')
        english = request.form.get('english')

        students.append(
            {'name': name,
             'chinese': chinese,
             'math': math,
             'english': english,
             'total': int(chinese) + int(math) + int(english)}
        )
    except Exception as e:
        print(e)
        return jsonify({'status': False, 'message': '添加数据失败'}), 400
    return jsonify({'status': True, 'message': '添加数据成功'})


@app.route('/verify_email_address')
def ajax_verify_email_address():
    # 邮箱地址验证
    # 接收客户端传递过来的邮箱地址
    email = request.args.get('email')
    print(request.args)
    # 判断邮箱地址注册过的情况
    if email == 'qingdeng@qd.cn':
        # 设置http状态码并对客户端做出响应
        return jsonify({'message': '邮箱地址已经注册过了, 请更换其他邮箱地址'}), 400
    else:
        # 邮箱地址可用的情况
        # 对客户端做出响应
        return jsonify({'message': '恭喜, 邮箱地址可用'}), 200


@app.route('/search_auto_prompt')
def ajax_search_auto_prompt():
    # 输入框文字提示
    # 搜索关键字
    key = request.args.get('key')
    # 提示文字列表
    items = [
        'Python程序员',
        'Python程序员官网',
        'Python程序员校区',
        'Python程序员学院报名系统',
        '前端与移动端开发',
        '大数据',
        'python',
        'java',
        'c++',
    ]
    result = [item for item in items if key in item]
    return jsonify(result)


@app.route('/province')
def ajax_province():
    # 获取省份
    return jsonify([
        {'id': '001', 'name': '黑龙江省'},
        {'id': '002', 'name': '四川省'},
        {'id': '003', 'name': '河北省'},
        {'id': '004', 'name': '江苏省'}
    ])


@app.route('/cities')
def ajax_cities():
    # 根据省份id获取城市
    areas = {
        '001': [{'id': '300', 'name': '哈尔滨市'},
                {'id': '301', 'name': '齐齐哈尔市'},
                {'id': '302', 'name': '牡丹江市'},
                {'id': '303', 'name': '佳木斯市'}],
        '002': [{'id': '400', 'name': '成都市'},
                {'id': '401', 'name': '绵阳市'},
                {'id': '402', 'name': '德阳市'},
                {'id': '403', 'name': '攀枝花市'}],
        '003': [{'id': '500', 'name': '石家庄市'},
                {'id': '501', 'name': '唐山市'},
                {'id': '502', 'name': '秦皇岛市'},
                {'id': '503', 'name': '邯郸市'}],
        '004': [{'id': '600', 'name': '常州市'},
                {'id': '601', 'name': '徐州市'},
                {'id': '602', 'name': '南京市'},
                {'id': '603', 'name': '淮安市'}]
    }
    city_id = request.args.get('id')
    print(city_id)
    return jsonify(areas[city_id])


@app.route('/areas')
def ajax_areas():
    areas = {
        '300': [{'id': '20', 'name': '道里区', },
                {'id': '21', 'name': '南岗区'},
                {'id': '22', 'name': '平房区', },
                {'id': '23', 'name': '松北区'}],
        '301': [{'id': '30', 'name': '龙沙区'},
                {'id': '31', 'name': '铁锋区'},
                {'id': '32', 'name': '富拉尔基区'}]
    }
    area_id = request.args.get('id')
    return jsonify(areas[area_id])


@app.route('/form_data', methods=["POST"])
def ajax_form_data():
    print(request.form)
    return "ajax_form_data"


@app.route('/upload', methods=["POST"])
def ajax_upload():
    print(request.files)
    file = request.files.get('file')
    file.save(file.filename)
    return "ajax_upload"


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
