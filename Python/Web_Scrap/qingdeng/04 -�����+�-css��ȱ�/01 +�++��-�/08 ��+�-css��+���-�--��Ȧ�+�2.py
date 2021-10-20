import requests
import parsel

response = requests.get('https://www.biquwx.la/10_10582/')
response.encoding = response.apparent_encoding
html_data = response.text

# 数据解析
# 1. 转换数据类型
selector = parsel.Selector(html_data)

# 2. 使用css语法解析数据
a_s = selector.css('#list dl dd a')  # 提取所有的 a 标签
# print(a_s)
# print(len(a_s))

for a in a_s:  # 遍历出来的 a 指代的就是一个一个提取的标签对象
    title = a.css('a::text').get()   # 只要是 selector 对象就具有对象的方法和属性
    href = a.css('a::attr(href)').get()   # 只要是 selector 对象就具有对象的方法和属性
    print(title, href)

"""
数据的二次提取: (推荐)  
    1. 首先提取所有想要的标签
    2. 然后遍历每一个标签对象, 那么每一个标签对象都可以单独操作
    
优点:
    可以保证数据解析的顺序不会乱
    可以根据标签对象操作很多次
"""
