"""
    根据下方出现的电话号码进行加密
    
    需求:
        最终效果: 181****5458
        必须用正则实现

"""

tel = "18123115458"

# 切片

import re


def func(temp):
    # temp 是正则匹配的对象 re.match
    # print(temp)
    str_ = temp.group()
    # return 返回的是替换以后的数据内容
    return str_[:3] + '****' + str_[-4:]


# func 是 re.sub()  会默认调用的函数, return返回的结果就是 result 最终替换的结果
result = re.sub('\d{11}', func, tel)
# print(result)

"""分组匹配: 百度上可能看到的"""
# (\d{3}) 分组一   (\d{4})  分组二    (\d{4})  分组三
pattern = re.compile('(\d{3})(\d{4})(\d{4})')

#  \\1   取分组一
result = re.sub(pattern, '\\1****\\3', tel)
print(result)



