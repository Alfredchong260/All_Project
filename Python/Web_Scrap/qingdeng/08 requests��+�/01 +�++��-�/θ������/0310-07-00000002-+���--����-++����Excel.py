"""
目标站点:https://news.163.com/

往下翻有 要闻 这个新闻类目

    需求:
        爬取网易新闻 要闻 类目第一页数据，将数据保存为 Excel 表格
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
import openpyxl

url = 'https://news.163.com/special/cm_yaowen20200213/?callback=data_callback'
response = requests.get(url=url)
json_str = response.text
# print(json_str)

# 正则
result = re.findall('data_callback\((.*?)\)', json_str, re.S)
# print(result)
# print(len(result))


json_data_str = result[0]  # 字符串 --> 对象

# 反序列化
json_list = json.loads(json_data_str)
pprint.pprint(json_list)
# print(type(json_list))

work_book = openpyxl.Workbook()
sheet = work_book.create_sheet('表1')


for data in json_list:
    title = data['title']
    channelname = data['channelname']
    docurl = data['docurl']
    imgurl = data['imgurl']
    source = data['source']
    tlink = data['tlink']

    print(title, channelname, docurl, imgurl, source, tlink, sep='|')

    sheet.append([title, channelname, docurl, imgurl, source, tlink])


work_book.save('网易新闻.xlsx')


