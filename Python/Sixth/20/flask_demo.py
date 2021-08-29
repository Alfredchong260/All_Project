from flask import Flask

app = Flask(__name__)


# 配置路由 --> 什么是路由    通过路径的形式访问某一个服务下面的文件

@app.route('/eat')
def eat():
    return 'I\'m eating'


@app.route('/')
def first():
    return 'Hello World'


@app.route('/sleep')
def sleep():
    return 'I\'m sleeping'


# 开启flask服务
'''
url = http://http://127.0.0.1:5000/
http: 是一种网络协议; https
127.0.0.1 : 本机 : localhost
:5000 表示端口;
'''
app.run()
