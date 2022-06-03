from flask import Flask, Blueprint, render_template

app = Flask(
    __name__,  # 导入的包名,项目的根目录
    static_folder="static",  # 静态资源存放的目录 (js/css/img/font....)
    template_folder="templates",  # 模板文件存在的文件夹名(html)
)


@app.route('/')
def index():  # index 视图函数
    # view --> 视图函数
    return render_template('index.html')


@app.route('/name')
def index_name():  # index 视图函数
    # view --> 视图函数
    return render_template('index.html')
