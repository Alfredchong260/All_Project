# A function is a block of code which only runs when it is called

'''
    1.无参数，无返回值
    2.无参数，有返回值
    3.有参数，无返回值
    4.有参数，有返回值
'''

# 1.无参数，无返回值
# def sum():
#     return 1 + 7, 5 + 4, 9 + 1, 10 * 10
    
# 2.无参数，有返回值
# def sum(name, age):
#     print(sum)
#     return 1 + 7

# 3.有参数，无返回值
# Recursive
# 递归
# 方法里面，inside the function
# 方法体
def sum(name, CheHin):
    print(sum)
    print(name, CheHin)
    return name, CheHin

sum('CheHin', 16)

# 4.有参数，有返回值





def Sum(num1, num2):
    total = num1 + num2
    return total

# print(Sum(1, 3))
# total = Sum(12, 12)
# print(total)

'''
1 为什么是total
    total是名字
2 可不可以是其他的东西
    只是一个名字，名字喜欢取什么就什么
'''

# total = Sum(1, 2)
# print(total)
# print(Sum(2,2))

# tuple
# Arguments


def sumofnumber(*args):
    num = 0
    for arg in args:
        num += arg
    return num

# total = sumofnumber(1,2,3,4,5,6,7,8,9,0)
# print(total)

# kwargs
# Keyword arguments
# 关键字参数


def something(k='Hello'):
    print(k)

# something(k='How are you')


def keywordargument(**kwargs):
    print(kwargs)


# keywordargument(k='Hello', w='Word')


# Another usage of function
# getSum = lambda num1, num2: num1 + num2
