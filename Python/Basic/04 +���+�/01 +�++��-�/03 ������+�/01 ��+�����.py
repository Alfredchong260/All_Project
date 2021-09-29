"""
NameError: name 'name' is not defined
    名称错误: name 没有被定义
"""
# print(name)

"""
ZeroDivisionError: division by zero
除零错误: 被除数不能为0
"""
# print(10 / 0)

"""
SyntaxError: invalid syntax
语法错误: 需要检查语法
"""
# for

"""
IndexError: list index out of range
索引错误: 在索引取值的时候, 超出了取值的范围
"""
# a_list = [1, 2, 3, 4, 5]
# print(a_list[10])

"""
KeyError: 'age'
键错误: 改字典没有这个键
"""
dict_a = {'name': "山禾"}
# print(dict_a['age'])
print(dict_a.get('age'))


"""
AttributeError: 'list' object has no attribute 'split'
表示该对象没有相关的属性或者方法
"""
a_list = [1, 2, 3, 4, 5]
# a_list.split()  # split() 是字符串这个对象的方法
