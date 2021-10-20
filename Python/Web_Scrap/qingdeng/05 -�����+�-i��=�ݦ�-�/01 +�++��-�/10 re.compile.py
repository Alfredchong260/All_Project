import re


str1 = "540775360@qq.com"
str2 = "python = 9999， c = 7890， c++ = 12345"
str3 = "python = 997"


# re.compile()   将正则表达式编译成一个对象
pattern = re.compile('\d+')
print(pattern)


result1 = re.findall(pattern, str1)
print(result1)

result2 = re.findall(pattern, str2)
print(result2)

result3 = re.findall(pattern, str3)
print(result3)
