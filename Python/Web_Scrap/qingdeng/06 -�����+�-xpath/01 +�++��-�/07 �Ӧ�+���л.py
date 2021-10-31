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

# 获取所有 li 标签的类属性值, 并且获取 a 标签包含的文本内容. 只能使用一行xpath解决
result = selector.xpath('//li/@class|//a/text()').getall()
print(result)


"""
    xpath语法中
    |   表示多条件查询, 所有俩边分别是两个条件, 满足其中一个条件就会被提取到(逻辑或)
    用的不多
    
    多条件查询到以后, 很有可能需要分组
"""
