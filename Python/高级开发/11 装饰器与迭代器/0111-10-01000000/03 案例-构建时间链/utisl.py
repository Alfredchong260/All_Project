"""

爬取东北三省包括黑龙江，吉林，辽宁三个省所有市县历史2014年01月至2019年12月的空气质量指数包括
（AQI指数，空气质量状况，PM10，PM2.5，Co，No2，So2，O3）（http://www.tianqihoubao.com/）
分析：http://www.tianqihoubao.com/lishi/beijing.html

需求
构建一个2018年到2020年所有月份的列表: ['201802', '201803', '201804', ...,  '202001']
"""
import time
import datetime
from dateutil.relativedelta import relativedelta

mouth = relativedelta(months=1)
print('月份时间差对象:', mouth)
mouth_list = []
old_day = datetime.datetime(2018, 1, 1, 0, 0, 0)
target_day = datetime.datetime(2020, 12, 31, 0, 0, 0)
while old_day < target_day:
    # print(old_day.strftime('%Y%m'))
    mouth_list.append(old_day.strftime('%Y%m'))
    old_day += mouth

print(mouth_list)