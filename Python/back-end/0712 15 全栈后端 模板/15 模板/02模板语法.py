from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/')
@app.route('/index')
def index():
    user = {'username': '青灯教育'}

    return f'''
    <html>
        <head>
            <title>个人主页-{user['username']}</title>
        </head>
        <body>
            <h1 style="color:red;">Hello, {user['username']}!</h1>
        </body>
    </html>'''


@app.route('/args')
def args():
    my_str = 'hello'
    my_int = 10
    my_arr = [1, 2, 3, 4, 5]
    my_dict = {
        "name": "正心",
        'age': 18
    }
    return render_template(
        '0201args.html',
        my_str=my_str,
        my_int=my_int,
        my_arr=my_arr,
        my_dict=my_dict,
    )


@app.route('/if')
def demo_if():
    # ?key=value&key2=value2&
    username = request.args.get('username')
    # if not username:
    #     username = '正心'
    return render_template(
        '0202if.html',
        username=username,
    )


@app.route('/loop')
def demo_loop():
    my_array = ['苹果', '橘子', '西瓜']
    return render_template('0203loop.html',
                           arr=my_array)


@app.route('/edit')
def demo_edit():
    student = {
        'name': '正心',
        'level': '二年级',
        'class': '2班',
        'math': 75,
        'chinese': 75,
        'english': 60,
    }
    level = [
        {'id': 1, 'name': '一年级'},
        {'id': 2, 'name': '二年级'},
        {'id': 3, 'name': '三年级'},
        {'id': 4, 'name': '四年级'},
        {'id': 5, 'name': '五年级'},
        {'id': 6, 'name': '六年级'},
    ]
    _class = [
        {'id': 1, 'name': '1班'},
        {'id': 2, 'name': '2班'},
        {'id': 3, 'name': '3班'},
    ]
    return render_template(
        '0204demo_edit.html',
        student=student,
        level=level,
        _class=_class
    )
