arr = [1, 2, 3, 4, 5, 6]

"""增加数据"""
# append  添加数据到列表的末尾
# arr.append(7)

# insert  指定位置插入数据
# arr.insert(0, 'a')  # 第一个参数是代表你要在列表的哪里插入数据(索引), 第二个参数是你需要插入的数据
# arr.insert(3, 'b')
# print(arr)

# 列表修改,操作, 都是基于列表本身操作的


"""删除数据"""
# pop()     默认是删除列表的最后一个数据, 也可以指定索引的位置删除
# arr.pop()
# arr.pop(0)

# remove()  指定元素删除, 不是索引
# arr.remove(3)
#
# print(arr)


"""查找数据"""
# index(), 传入一个列表中的元素, 就会得到在列表中的索引, 如果元素不存在, 会报错<可以判断解决>
# if 7 in arr:
#     print(arr.index(7))


"""拓展列表<合并>"""
# a = [1, 2, 3]
# b = [4, 5, 6]
# # 把b列表合并到a列表里面
# a.extend(b)  # [1, 2, 3, 4, 5, 6]
# # 把a列表合并到b列表里面
# b.extend(a)
# print(a)
# print(b)


a = [1, 2, 3, 3, 5, 1]

a.sort(reverse=True)  # False  升序   True  降序

print(a)

