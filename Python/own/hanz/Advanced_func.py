# Received multiple params

# Advanced (Recursive Function)
'''         递归函数(第一种方法)            '''
# 阶乘
# 求5 的阶乘
# 5的阶乘 = 5*4*3*2*1 = 120

def factorial(num):
    if num ==1:
        return 1*1
    return num * factorial(num-1)
print(factorial(7))

'''         第二种方法           '''
def recursion(num):
    counts=1
    for i in range(1,num+1):
        counts*=i
    return counts
print(recursion(7))
