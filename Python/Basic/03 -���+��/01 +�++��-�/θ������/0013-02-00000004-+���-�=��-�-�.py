"""（选做题）
打印一百以内的素数
素数定义为在大于1的自然数（到无穷大的整数）中，除了1和它本身以外不再有其他因数。

1. 打印0-100的所有数字
2. 判断当数字是否是素数
    如果是素数就打印
    如果不是素数就什么都不做
"""
"""自己在下方编写代码实现功能"""
for i in range(2, 100):  # 9
    for j in range(2, i):  # 2345678
        if i % j == 0:  # 代表除了 1 和 数字本身外 还有其他因数
            break  # 如果循环嵌套了, 使用到了 break 或者 continue 满足就近原则
                   # 如果break掉了, 那么代表这个循环不是正常结束的
    else:
        print(i)  # 打印的就是素数




