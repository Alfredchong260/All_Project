import re


string = '00PythonahsdgjasghPythonasdjajsk'


# re.search()  从字符串中的任意位置匹配符合要求的字符串, 有且仅返回一次结果
# result 得到的结果是一个对象, group() 可以在对象里面提取匹配到的数据
result = re.search('Python', string)
print(result.group())
