


# for 遍历

# for i in 'hello':
#     print(i)

# for i in range(10):
#     print(i)

"""range() 函数"""
# 范围 默认从零开始 到指定数字之间的范围, 不能取到指定的数字
print(list(range(10)))  # 0123456789  10取不到
print(list(range(2, 10)))  # 23456789  范围是一个左闭右开的区间, 顾首不顾尾
print(list(range(2, 10, 1)))  # range函数默认的区间内, 步长为 1, 如果步长为 1 , 那么可以省略
print(list(range(2, 10, 3)))  # 步长可指定2及以上, 代表数据取值怎么取
print(list(range(-10, -20, -2)))  # 如果步长为负数, 代表倒着取, 那么我们的范围也要倒着指定


for i in range(10):
    # 遍历出来的结果都会用 i 接收
    print(i * 10)