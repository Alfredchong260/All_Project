import re


string = '00PythonahsdgjasghPythonasdjajsk'

"""
pattern  需要匹配的字符串(正则)
string   要在哪个字符串匹配
flags    模式匹配
"""

# re.match()  从匹配的字符串中只从头部开始, 根据正则语法匹配, 头部没有数据就匹配不到
# result 得到的结果是一个对象, group() 可以在对象里面提取匹配到的数据
result = re.match('Python', string)
print(result.group())
