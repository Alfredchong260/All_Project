import copy  # 拷贝模块 , 内置

arr1 = [1, 2, 3, 4, 5]

# 浅拷贝一个对象
# 浅拷贝会新建一个对象
arr2 = copy.copy(arr1)

print(id(arr1))
print(id(arr2))

arr1[0] = 'a'

print(arr1)
print(arr2)

print('=========================浅拷贝的作用域===========================')
array2 = [
    1,
    ['a', 'b', 'c'],
    3
]

array3 = copy.copy(array2)

array3[1][0] = 1

print(array2)
print(array3)

# 浅拷贝作用域是作用域一维数据