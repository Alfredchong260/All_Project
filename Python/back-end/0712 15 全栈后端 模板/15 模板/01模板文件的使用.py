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


@app.route('/index2')
def index2():
    username = request.args.get('username')
    if username:
        user = {'username': username}
    else:
        user = {'username': '青灯教育'}
    # jinja2 模板
    return render_template('index.html', user=user)

