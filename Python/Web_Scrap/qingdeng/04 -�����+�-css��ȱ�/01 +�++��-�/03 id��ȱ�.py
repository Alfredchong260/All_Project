
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
<p id="contend">css标签选择器的介绍</p>
<a href="https://www.baidu.com">百度一下</a>
<span id="contend"> 我是一个span标签</span>
<p class="top">标签选择器、类选择器、ID选择器</p>
</body>
</html>
"""


import parsel  # 第三方模块  pip install parsel  数据解析的模块(css选择器, xpath, re)


selector = parsel.Selector(html)

# id  一般标签的id属性在 html 中是唯一
# "#"  是用id选择器提取数据
# 只要标签具有 id 属性, 都会被提取
# contend 代表要提取的标签的 id 属性
result = selector.css('#contend').getall()
print(result)


