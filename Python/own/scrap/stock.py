from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker
import pandas as pd
import requests
import parsel
import csv

url = 'https://cn.investing.com/equities/malaysia'

headers = {
    "user-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36"
}


response = requests.get(url, headers=headers)
selector = parsel.Selector(response.text)

csv_head = ['名称', '最新价', '最高', '最低', '涨跌', '涨跌幅', '交易量', '时间']

tr_lst = selector.css('#cross_rate_markets_stocks_1 tbody tr')
with open('马来西亚股票.csv', 'w', encoding='utf-8') as f:
    csv_writer = csv.DictWriter(f, fieldnames=csv_head)
    csv_writer.writeheader()

    for tr in tr_lst:
        name = tr.css('td:nth-child(2) a::text').get()
        latest = tr.css('td:nth-child(3)::text').get()
        high = tr.css('td:nth-child(4)::text').get()
        low = tr.css('td:nth-child(5)::text').get()
        changes = tr.css('td:nth-child(6)::text').get()
        per = tr.css('td:nth-child(7)::text').get()
        exchange = tr.css('td:nth-child(8)::text').get()
        if exchange.endswith('K'):
            exchg = exchange.split('.')[0]
        else:
            exchg = int(float(exchange.split('M')[0]) * 1000)
        time = tr.css('td:nth-child(9)::text').get()
        data_dict = {
            '名称': name, 
            '最新价': latest,
            '最高': high,
            '最低': low,
            '涨跌': changes,
            '涨跌幅': per,
            '交易量': exchg,
            '时间': time
        }
        csv_writer.writerow(data_dict)

data_df = pd.read_csv('./马来西亚股票.csv')
df = data_df.dropna()
df1 = df[['名称', '交易量']]
df2 = df1.iloc[:20]
x_axis = df['名称'].values
y_axis = df['交易量'].values

c = (
    Bar()
    .add_xaxis(x_axis)
    .add_yaxis('股票交易状况', y_axis)
    .set_global_opts(
        title_opts=opts.TitleOpts(title='交易量图表 - Volume Chart'),
        datazoom_opts=opts.DataZoomOpts(),
    )
    .render('data.html')
)
print(x_axis)
print(y_axis)
