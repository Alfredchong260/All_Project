import requests
import re

response = requests.get('https://www.biquwx.la/10_10582/5103238.html')

# encoding 表示设置对象的编码  apparent_encoding 自动识别响应体的编码
response.encoding = response.apparent_encoding
response.encoding = 'utf-8'

html_data = response.text
print(html_data)

"""
utf-8   保存数据数据, 如果任然有乱码, 可以考虑是用 utf-8-sig

gbk  gb2312

"""

