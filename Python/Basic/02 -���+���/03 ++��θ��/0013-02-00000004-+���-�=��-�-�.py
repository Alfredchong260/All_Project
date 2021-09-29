"""（选做题）
打印一百以内的素数
素数定义为在大于1的自然数（到无穷大的整数）中，除了1和它本身以外不再有其他因数。

1. 打印0-100的所有数字
2. 判断当数字是否是素数
    如果是素数就打印
    如果不是素数就什么都不做
"""
"""自己在下方编写代码实现功能"""

# num = 0

# for i in range(1, 101):
#     if 1 < i <= 3:
#         print(i)
#     if i % 2:
#         if i % 3:
#             if i % 5:
#                 print(f"{i} 是素数")

# print(num)

for i in range(2, 101):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)
