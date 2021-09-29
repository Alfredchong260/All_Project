# 元组是一种不可变的序列类型

tuple1 = (1, 2, 3, 4, 5)
print(tuple1)
print(type(tuple1))

# 可以使用 tuple 关键字强制转换
tuple2 = tuple('123456')
print(tuple2)


# 元组是一种有顺序的数据容器, 支持索引取值, 支持切片
print(tuple1[0])
print(tuple1[-1])
print(tuple1[1::2])


# 元组是一种不可变的数据容器, 安全性高
# tuple1[0] = 'a'

"""创建只有一个数据的元组"""
# 在该数据后面加一个逗号, 爬虫
tuple3 = ('a',)
print(tuple3)
print(type(tuple3))
