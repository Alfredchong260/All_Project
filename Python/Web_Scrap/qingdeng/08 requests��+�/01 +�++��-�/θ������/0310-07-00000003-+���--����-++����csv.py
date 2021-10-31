"""
目标站点:https://news.163.com/

往下翻有 要闻 这个新闻类目

    需求:
        爬取网易新闻 要闻 类目第一页数据，将数据保存为csv格式
        保存字段需要以下内容

            title  
            channelname  
            docurl  
            imgurl  
            source  
            tlink
"""

import pprint
import re
import requests
import json
import csv

url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'
response = requests.get(url=url)
json_str = response.text

result = re.findall('data_callback\((.*?)\)', json_str, re.S)

json_data_str = result[0]  # 字符串 --> 对象

json_list = json.loads(json_data_str)
pprint.pprint(json_list)

with open('网易新闻.csv', mode='a', encoding='utf-8', newline='') as f:
    f.write('字段1,字段2,字段3,字段4,字段5,字段6\n')

    # 把数据构建成字典, 就有直接写入表头的方法

    for data in json_list:
        title = data['title']
        channelname = data['channelname']
        docurl = data['docurl']
        imgurl = data['imgurl']
        source = data['source']
        tlink = data['tlink']

        print(title, channelname, docurl, imgurl, source, tlink, sep='|')

        csv_write = csv.writer(f)
        csv_write.writerow([title, channelname, docurl, imgurl, source, tlink])

