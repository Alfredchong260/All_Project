
text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
Super劫Zed: 5407753601563123456@qq.com
Super劫Zed: 54077536058@qq.com
Super劫Zed: 5407753789784864560@qq.com

我也说一句

假设QQ位数 6 到 11
"""

import re

result = re.findall('Super劫Zed: \d*@qq.com', text)
print(result)

# {start,stop}  表示数量词, 限制前一个元字符出现的次数 [] 闭区间
result = re.findall('Super劫Zed: \d{6,11}@qq.com', text)
print(result)


