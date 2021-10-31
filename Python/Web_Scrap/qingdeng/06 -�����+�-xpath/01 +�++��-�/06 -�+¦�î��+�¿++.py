html_str = """
        <div> 
            <ul> 
                <li class="item-1">
                    <a href="link1.html">第一个</a>
                </li> 

                <li class="item-2">
                    <a href="link2.html">第二个</a>
                </li> 

                <li class="item-3">
                    <a href="link3.html">第三个</a>
                </li> 

                <li class="item-4">
                    <a href="link4.html">第四个</a>
                </li> 

                <li class="item-5">
                    <a href="link5.html">第五个</a> 
                </li>
            </ul>
        </div>
"""

import parsel  # css xpath

selector = parsel.Selector(html_str)

# 获取第三个 li 标签(不能用属性精确定位)
result = selector.xpath('//li').getall()[2]
print(result)

result = selector.xpath('//li[3]').getall()
print(result)


"""
    xpath语法中
    []       1. 对于获取多个同级标签, 可以用 [] 精确定位获取标签的第几个
                [] 里面的数字填你想要的统计标签的顺序, 类似索引值, 索引从1开始
                
             2. [] 可以用于属性的精确定位
"""
