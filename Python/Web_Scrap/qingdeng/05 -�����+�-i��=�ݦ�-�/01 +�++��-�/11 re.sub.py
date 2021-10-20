import re


str1 = "Pythonasdkjasd Java adhuiaghsdk Java akjsdhkashdkja"
"""
    sub(pattern, repl, string, count=0, flags=0)
        pattern:正则语法
        repl: 把匹配的数据替换成这个参数指定的内容, (也可以用函数返回需要替换的内容)
        count: 匹配次数
"""

# re.sub() 替换, 直接返回替换的结果
result3 = re.sub('Java', 'python', str1, count=1)
print(result3)
