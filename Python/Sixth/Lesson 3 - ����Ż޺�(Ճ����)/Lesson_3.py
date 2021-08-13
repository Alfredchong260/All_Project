from pyecharts.charts import Pie

goods = ['cupcake', 'shampoo', 'shower', 'towel']
sale = [10, 30, 60, 100]
Pie().add(series_name='sale ranking', data_pair=[data for data in list(zip(goods, sale))]).render('sale ranking.html')
