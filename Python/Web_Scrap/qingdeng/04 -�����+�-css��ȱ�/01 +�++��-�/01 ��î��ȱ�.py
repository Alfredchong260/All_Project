
# 字符串类型的数据, 直接和python交互, 正则表达式
html = """  
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>标签选择器</title>
</head>
<style>
    p{
        color: #f00;
        font-size: 16px;
    }
</style>
<body>
<p>css标签选择器的介绍</p>
<p>标签选择器、类选择器、ID选择器</p>
<a href="https://www.baidu.com">百度一下</a>
<span> 我是一个span标签</span>
</body>
</html>
"""


import parsel  # 第三方模块  pip install parsel  数据解析的模块(css选择器, xpath, re)


# 1. 把 html 数据<str>转换成一个对象
# selector 就具有一系列数据解析的方法  css()/xpath()/re()
selector = parsel.Selector(html)
print(selector)

# 所有通过css选择器解析数来的数据都是对象(Selector)
# span 表示标签选择器, 直接给标签的名字
# p = selector.css('span')
# print(p)

"""
get()       从解析的数据中返回第一个数据, 直接把字符串数据返回给我们
getall()    从解析的数据中返回所有符合条件的数据, 返回的是列表
"""
# p = selector.css('p').get()
# p = selector.css('a').getall()
p = selector.css('a').get()
print(p)
print(type(p))


