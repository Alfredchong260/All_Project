text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com  你好 
Super劫Zed: 540775360@qq.com  我好
Super劫Zed: 540775360@qq.com  大家好
2018-8-8 16:00回复
我也说一句
"""

import re

"""
贪婪匹配: 正则的默认匹配模式, 你的字符串只要满足正则表达式规则, 尽可能多的匹配数据

.*   匹配除了换行符以外的任意字符, 默认情况下是贪婪模式
.*?  非贪婪模式, 匹配一次返回一次
?    匹配1次或者0次
"""

result = re.findall('Super劫Zed: .*@qq.com', text, re.S)
print(result)

result = re.findall('Super劫Zed: .*?@qq.com\n', text, re.S)
print(result)
print(len(result))
