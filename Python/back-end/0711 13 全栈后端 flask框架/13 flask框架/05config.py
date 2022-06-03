from flask import Flask, Blueprint, render_template
import config

app = Flask(__name__)

# app.secret_key = '123465'
# app.config  flask配置文件存放的位置
app.config['SECRET_KEY'] = '123456'


class Config:
    SECRET_KEY = '123456'
    MYSQL_HOST = '127.0.0.1'
    MYSQL_PORT = 3306


# app.config.from_pyfile('config.py')  # 从文件里面添加配置
# app.config.from_object(config)
app.config.from_object(Config)


@app.route('/')
def index():
    print(app.config)
    print(app.secret_key)
    print(app.config['MYSQL_HOST'])
    return render_template('index.html')
