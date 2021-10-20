
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
<p class="top abc">css标签选择器的介绍</p>
<a href="https://www.baidu.com">百度一下</a>
<span> 我是一个span标签</span>
<p class="top">标签选择器、类选择器、ID选择器</p>
</body>
</html>
"""


import parsel  # 第三方模块  pip install parsel  数据解析的模块(css选择器, xpath, re)


selector = parsel.Selector(html)

# 只有标签具有 class 属性才可以用类选择器提取对应的标签
# .  代表提取标签的类型(class)
# 具有相同类属性的标签都会被提取
# 类选择器就是通过标签的类属性精确定位
# result = selector.css('.top').getall()
# print(result)


"""
1. 类属性中有空格
    空格在css语法中表示取嵌套标签里面的数据
    如果在class类属性中包含了空格, 那么空格需要用 . 代替
    
2. 使用类选择器, 有可能解析出来的数据量不对:
    可以往上级标签定位, 然后向下取
"""
result = selector.css('.top.abc').getall()
print(result)

