
"""
    根据下方出现的电话号码进行加密
    
    需求:
        最终效果: 181****5458
"""

tel = "18123115458"

import re

# def change(tel):
#     tel = str(tel)
#     length = len(tel)
#     if length >= 11:
#         front = tel[0:3]
#         middle = tel[3:6]
#         back = tel[-4:-1]
#         changed = re.sub(middle, '*'*len(middle), middle)
#         return front + changed + back
#     else:
#         front = tel[0:3]
#         middle = tel[3:]
#         changed = re.sub(middle, '***', middle)
#         return front + changed


# new = change(tel)
# print(new)

def func(temp):
    # temp是正则匹配的对象 re.match
    str = temp.group()
    return str[:3] + '****' + str[-4:]

# result = re.sub('\d{11}', func, tel)
# print(result)

pattern = re.compile('\d{3}\d{4}\d{4}')
result = re.sub(pattern, '\\1****\\3', tel)
print(result)
