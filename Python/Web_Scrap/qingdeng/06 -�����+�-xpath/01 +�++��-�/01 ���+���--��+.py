

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

import parsel   # css xpath


# 转换数据类型, 能够把HTML标签补充完整
selector = parsel.Selector(html_str)
# print(selector.get())

# 从根节点开始, 获取所有的 <a> 标签
result = selector.xpath('/html/body/div/ul/li/a').getall()
print(result)

"""
    xpath语法中
    /       表示从根节点开始提取(用的很少), 还表示取下一级标签
    如果打算从根节点开始提取的话, 那么必须从html这个节点开始
"""


