
text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 00775360@qq.com
Super劫Zed: 5407753601563123456@qq.com
Super劫Zed: 54077536058@qq.com
Super劫Zed: 5407753789784864560@qq.com

我也说一句

假设QQ位数 6 到 11
"""

import re


# [] 表示字符集, 字符集里面罗列的内容才可以匹配, 一个字符集只能匹配到一个字符
result = re.findall('Super劫Zed: [123456789]\d{6,11}@qq.com', text)
print(result)

result = re.findall('Super劫Zed: [123456789][0123456789]{5,10}@qq.com', text)
print(result)

result = re.findall('Super劫Zed: [1-9][0-9]{5,10}@qq.com', text)
print(result)

# result = re.findall('Super劫Zed: [a-zA-Z][0-9]{5,10}@qq.com', text)
# print(result)


