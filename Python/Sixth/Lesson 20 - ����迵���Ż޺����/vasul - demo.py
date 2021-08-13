'''
python中的可视化
    1. 将大量的数据更直观的展示
    2. 传递数据高效，信息更加立体
    3. python 这门语言:
        matplotlib, matlab, pyecharts-- (echarts) ;
    pyecharts   pyecharts.org
    echarts     echarts.apache.org

python的常用框架:
    小全栈:
    web: django --> 精装修 --> 集成了很多功能(重量级框架)
        flask --> 简单 --> 手动去配置，添加对应的代码(轻量级框架framework)
    前端:
        bootstap; vue.js; layui(模板)
    服务器:
        部署; sql 语句:

    爬虫:
        scrapy: (重量级的爬虫框架)
        requests : 模块;
'''
from pyecharts.charts import Bar
from random import randrange

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

bar.render('Merchant\'s sales data.html')
