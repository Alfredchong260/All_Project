# arr = [(1, 2), (4, 1), (9, 10), (13, -3)]
#
# # # 列表的排序方法,会直接修改列表本身
# # arr.sort(key=lambda temp: temp[0] + temp[1])
# # # key()
# # print(arr)
#
# # 想要看一下排序之后的结果,但是不想修改列表本身
# # sorted 会返回一个排序之后的结果
# print('tuple(arr):\t', tuple(arr))
# # key 是排序绘制,是一个函数
# print(sorted(tuple(arr), key=lambda temp: temp[0] + temp[1]))
# print('arr:\t', arr)


arr = [4, 3, 7, 1, 9]
# new_arr = []
# for item in arr:
#     new_arr.append(str(item))

# # map(映射规则,需要处理的可迭代对象)
# # f(x) -> y
# new_arr = map(str, arr)
# """
#  x = arr = [4, 3, 7, 1, 9]  -->
#  f --> str   f(x) --> str(x) -> ['4', '3', '7', '1', '9']
#
#
# """
# new_arr = map(lambda temp: str(temp), arr)
# # new_str = lambda temp: str(temp)
# # new_arr = map(new_str, arr)
# print([','.join(new_arr)])
# print(list(map(str, range(1, 10))))
# """
#     可迭代对象
# """

arr = ['a', 'b', 'c', 'd', 'e', 'f']
arr2 = [1, 2, 3, 4, 5]
# {'a':1, 'b':2...}
# d = {}
# for index in range(len(arr)):
#     d[arr[index]] = arr2[index]
# print(d)

print(list(zip(arr, arr2, arr2)))
print(dict(zip(arr, arr2)))
