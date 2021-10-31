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

# 获取第四个 a 标签, 并且获取其包含的文本内容
result = selector.xpath('//a[@href="link4.html"]/text()').getall()
print(result)


"""
    xpath语法中
    text()       在获取到标签后, 可以用此语法取标签包含的文本  
"""
