from pyecharts import options as opts
from pyecharts.charts import Bar
import requests
import pandas
import csv
import re


class Crawler:
    def __init__(self):
        self.url = 'https://weather.my/weather/ipoh/history/daily-history/?gid=1734634&station=11331&date=2021-12-04&language=chinese&country=malaysia'
        self.fieldnames = ['时间', '温度', '气压', '详情']

    def scrap(self):
        response = requests.get(self.url)

        times = re.findall('<td class="white no-top">(.*?)</td>', response.text, re.S)
        degree = re.findall('<td><b>(.*?)</b></td>', response.text, re.S)
        pressure = re.findall('<td class="nw">(.*?mb)</td>', response.text)
        details = re.findall('<span class="details">(.*?)</span>', response.text, re.S)

        with open('weather.csv', 'w', encoding='utf-8') as w:
            csv_writer = csv.writer(w)
            w.writelines(self.fieldnames)
            for t, d, p, ds in zip(times, degree, pressure, details):
                print(t, d, p, ds)
                csv_writer.writerow((t, d, p, ds))

class Visualization:
    def __init__(self):
        self.csv_data = pandas.read_csv('./weather.csv')
        self.data = self.csv_data.iloc[:, [True, True, False, False]]

        self.show_chart()

    def show_chart(self):
        x_axis = list(self.data['时间'])
        y_axis = []
        y = list(self.data['温度'])

        for i in y:
            a = i.split('°C')
            y_axis.append(a[0])
            
        c = (
            Bar()
            .add_xaxis(x_axis)
            .add_yaxis('温度', y_axis)

            .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=-15)),
            title_opts=opts.TitleOpts(title='马来西亚温度'),
            datazoom_opts=opts.DataZoomOpts(),
            )
            .render('chart.html')
        )

Visualization()
