
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
<p class="top">标签选择器、类选择器、ID选择器</p>
<a href="https://www.baidu.com" src="www.taobao.com">百度一下</a>
<span id="contend"> 我是一个span标签</span>
</body>
</html>
"""


import parsel


selector = parsel.Selector(html)

# : 表示伪类选择器: 想取满足条件的第几个
# nth-child 满足条件的第几个元素
# (2) 表示选择满足标签的第二个元素, 类似索引, 从1开始
# 伪类选择器, 只能选一个, 想取一个区间的标签, 可以用列表的<切片>
result = selector.css('p:nth-child(2)::text').getall()
print(result)


"""
# 在elements元素面板复制的css语法只能定位到一个标签
# 如果想要定位多个标签, 只能自己手写


#list > dl > dd:nth-child(451)

>       在css语法中, 表示仅取子标签
空格     可以取想要的标签下所有的标签(不管是子标签还是孙子标签....)
"""



