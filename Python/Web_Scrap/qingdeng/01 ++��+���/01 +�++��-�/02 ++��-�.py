import requests
import re  # 内置, 正则表达式模块(解析数据)

response = requests.get('https://www.biquwx.la/10_10582/5103238.html')

# encoding 表示设置对象的编码  apparent_encoding 自动识别响应体的编码
response.encoding = response.apparent_encoding

html_data = response.text
print(html_data)

"""
<div id="content"><!--go-->.*?(.*?)<!--over-->.*?</div>
"""

# re.findall返回列表
result = re.findall('<div id="content"><!--go-->.*?(.*?)<!--over-->.*?</div>', html_data, re.S)
# <br/> 是HTML中的换行符
contend = result[0].replace('&nbsp;', '').replace('<br/>', '\n')

# 数据保存
with open('a.txt', mode='w', encoding='utf-8') as f:
    f.write(contend)
