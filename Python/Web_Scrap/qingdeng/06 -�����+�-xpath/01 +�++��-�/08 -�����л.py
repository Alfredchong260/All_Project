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

# 了解, 模糊查询
result = selector.xpath('//li[contains(@class,"it")]').getall()
print(result)


"""
    xpath语法中(了解)
        contains(@class,"it")  表示模糊查询
        @class      表示模糊查询属性的名字
        it          表示标签属性模糊查询的关键字, 包含此关键字的标签都会被查询到
"""
