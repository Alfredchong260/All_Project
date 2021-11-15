from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    # 登陆到服务器 获取用户名以及密码 然后进行校验 在记录信息 在返回后台页面
    # print(request.form)
    username = request.form.get('username')
    password = request.form.get('password')
    print(username, password)
    # 获取用户名与密码 然后校验 再记录信息
    
    return render_template('admin.html')

if __name__ == '__main__':
    app.run(debug=True)
