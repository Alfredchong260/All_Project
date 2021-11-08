# A function is a block of code which only runs when it is called

'''
    1.无参数，无返回值
    2.无参数，有返回值
    3.有参数，无返回值
    4.有参数，有返回值
'''
# Create function
def saysomthing(str):
    return (f"Hello {str}")

# Return value
def Sum(num1, num2):
    total = num1 + num2
    return total


total = Sum(1, 2)
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

keywordargument(k='Hello', w='Word')










# Another usage of function
# getSum = lambda num1, num2: num1 + num2

