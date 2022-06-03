# 1. 导入 Flask 对象
from flask import Flask

# 2. 创建一个 flask 应用程序
app = Flask(__name__)


# 3. 将函数视图 hello_world 与 / 路由绑定起来
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello Flask!'  # 访问路由时视图函数返回的结果
