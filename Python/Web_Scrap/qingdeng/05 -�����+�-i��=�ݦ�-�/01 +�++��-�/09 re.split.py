import re


string = 'Pythonasdk123456jasdadhuiaghsdk564654akjsdhka333shdkja'

"""
pattern     正则语法
string      需要分割的字符串
maxsplit    指定分割的次数
"""

# re.split()    字符串的分割, 分割后返回列表, 可以通过maxsplit指定分割的次数
result = re.split('\d+', string, maxsplit=10)
print(result)
