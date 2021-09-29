arr1 = [1, 2, 3, 4, 5]

arr2 = arr1

# 对象的引用
# id 查询对象在内存地址中的位置
print(id(arr1))
print(id(arr2))


# 对象引用, 操作的是统一个对象
arr1[0] = 'a'
print(arr1)
print(arr2)
