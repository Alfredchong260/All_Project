import json
import random
import glob
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS().init_app(app)
app.jinja_env.variable_start_string = '%%'
app.jinja_env.variable_end_string = '%%'


@app.route('/')
def index():
    return 'hello world !'


@app.route('/verify_username')
def ajax_verify_username():
    username = request.args.get('username')
    print(username)
    if username in ['正心', '丸子', '清风']:
        return jsonify({'message': '用户名已经存在，请更换用户名'}), 400
    else:
        return jsonify({'message': '恭喜, 用户名可以使用'}), 200


@app.route('/verify_email')
def ajax_verify_email():
    email = request.args.get('email')
    if email == 'qingdeng@zhengxin.cn':
        return jsonify({'message': '邮箱地址已经注册过了, 请更换其他邮箱地址'}), 400
    else:
        return jsonify({'message': '恭喜, 邮箱地址可用'}), 200


@app.route('/register', methods=['POST'])
def register():
    return jsonify({'message': '恭喜, 注册账户成功'})


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
