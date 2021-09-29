'''
List is a collection which is ordered and changable
'''
#    01234567
s = 'asdfuiop'
num  = [9, 8, 7, 6, 5]
num1 = [1, 2, 3, 4, 5]
#       0  1  2  3  4

# num[1] = 5
# print(num)

# Get a value
# print(num[0:2])

# Get length
# print(len(num))

# Append new value
# num.append('Hello')
# print(num)

# 扩展
# num.extend(num1)
# print(num)

# Remove value from list
# num.remove(9)
# print(num)
# num.pop(1)
# print(num)

# Change values
# num[0] = 'hello' , 'world'
# print(num)

# Insert item 指定的地方插入想要的数据
# num.insert(1, 'hello')
# print(num)

# Reverse the list
# print(num[::-1])

# index  0              1           2
a = [
    ('x', 'y'),
    [1,2,3,4,5],
    {"name": 'Chong', "Age":18}
]
print(a[2].keys())
