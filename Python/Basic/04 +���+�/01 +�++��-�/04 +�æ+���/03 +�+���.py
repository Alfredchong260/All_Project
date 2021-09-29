import copy  # 拷贝模块 , 内置

array2 = [
    1,
    ['a', 'b', 'c'],
    3
]

# 深拷贝, 把对象里面所有内容全部拷贝一份(包括所有维度的数据)
array3 = copy.deepcopy(array2)

array3[1][0] = 1

print(array2)
print(array3)

# 操做数据容器
