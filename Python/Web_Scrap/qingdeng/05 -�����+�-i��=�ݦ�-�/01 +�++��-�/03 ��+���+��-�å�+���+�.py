text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
Super劫Zed: 540775360@qq.com
Super劫Zed: 540775360@qq.com
2018-8-8 16:00回复
我也说一句
"""

import re

"""
精确匹配: 先根据正则的语法匹配字符串, 然后提取 () 里面数据
()      表示精确匹配
"""

"""
    一般用(.*?)精确匹配
    用.*?作为字符串的占位符
"""

result = re.findall('Super劫Zed: (.*?)@qq.com\n', text, re.S)
print(result)

result = re.findall('Su.*?: (.*?)@qq.com\n', text, re.S)
print(result)
