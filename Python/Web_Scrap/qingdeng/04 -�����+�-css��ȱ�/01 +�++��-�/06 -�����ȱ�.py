
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
<p class="top" id="contend">css标签选择器的介绍</p>
<a href="https://www.baidu.com" src="www.taobao.com">百度一下</a>
<span id="contend"> 我是一个span标签</span>
<p class="top">标签选择器、类选择器、ID选择器</p>
</body>
</html>
"""


import parsel


selector = parsel.Selector(html)

# :: 表示属性选择器, 当我们提取到标签以后, 需要获取标签特定的值进行提取(标签包含的文本, 标签的属性值), 就可以使用属性选择器
# text  代表提取标签包含的文本(所有符号都是英文形势下的符号)
result = selector.css('p::text').getall()
print(result)


"""
::attr(href)    根据标签中包含的属性名字提取属性值
href            a 标签中需要提取属性值的属性名字
"""
result = selector.css('a::attr(src)').getall()
print(result)

