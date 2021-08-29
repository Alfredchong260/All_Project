from pyecharts.charts import Bar
from random import randrange
from flask import Flask, render_template

# 创建flask的app
data_app = Flask(__name__, static_folder='''/templates''')  # 如果访问不到html页面加上static_folder;自定义路径

bar = (
    Bar()
        # 为x轴添加数据
        .add_xaxis(['suit', 'sweater', 'shoe', 'treasure', 'hat'])
        # 添加商家的销售信息
        .add_yaxis('Merchant A', [randrange(10, 80) for _ in range(5)])
        .add_yaxis('Merchant B', [randrange(10, 80) for _ in range(5)])
        .add_yaxis('Merchant C', [randrange(10, 80) for _ in range(5)])
        .add_yaxis('Merchant D', [randrange(10, 80) for _ in range(5)])
        .add_yaxis('Merchant E', [randrange(10, 80) for _ in range(5)])
        .add_yaxis('Merchant F', [randrange(10, 80) for _ in range(5)])
        .add_yaxis('Merchant G', [randrange(10, 80) for _ in range(5)])
        .add_yaxis('Merchant H', [randrange(10, 80) for _ in range(5)])
)


# 配置路由
@data_app.route('/')
def index():
    # 通过render_template方法响应到页面
    print('刚才页面经过这个路由')
    return render_template('data_vasul.html')

@data_app.route('/data')
def return_data():
    print('响应了数据到页面上去')
    b = bar
    print(b.dump_options_with_quotes())
    # 将bar对象中的数据响应到页面上
    return b.dump_options_with_quotes()
# bar.render('Merchant\'s sales data.html')
data_app.run()
