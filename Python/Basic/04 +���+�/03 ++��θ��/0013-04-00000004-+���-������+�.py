"""
作业3：
    请把下面代码可能出现错误的地方全部捕捉（try-except）
    忽略报错部分，让能正确运行的地方运行

1. 输入一个正常数字
2. 输入 0
3. 输入 s
"""
my_list = [1, 2, 3, 4, "5"]

number = input("请输入一个number:")

try:
    for i in my_list:
        number = int(number)
        print(f"{i}/{number}={i/number}")
except:
    pass
