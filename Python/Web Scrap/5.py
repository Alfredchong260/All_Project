# xpath

# 了解如何自己写xpath
# / 从当前节点选取直接子节点
# // 从当前节点选取直接子孙节点
# . 选取当前节点
# .. 选取当前节点的父节点
# @ 选取属性
# [] 选取第几个节点 传入属性

'''
    xpath是一门XML文档中找到的信息的语言，HTML文档的搜索
    功能强大，路径选择表达式
'''

import requests
from lxml import etree

url = 'https://www.bilibili.com/'
headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

response = requests.get(url, headers=headers)

# 这步是将网页源代码转换为html格式
html = etree.HTML(response.text)
# print(type(html))

# 将html格式转换为str格式
# result = etree.tostring(html)
# print(result)

# 只有text用text(),其他大部分元素都是@+元素名
results = html.xpath('//div[@id="primaryChannelMenu"]/span')

for result in results:
    text = result.xpath('./div/a/span/text()')
    print(text)
