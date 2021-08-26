'''         函数部分            '''
def say_hello():
    print('hello')
say_hello()

'''         利用函数对大量的数据进行求和          '''
'''
我们经常定义很多的函数，可能会与内置函数产生重叠
'''
# def sums(*num):
#     #声明一个变量 统计求和的数据
#     result = 0
#     for i in num:
#         result+=i
#     return result
# lst=[i for i in range(10)]
# sums(lst)

# *号的作用     添加多个参数
'''         第一个方法           '''
def a(*n):
    sum = 0
    for i in n:
        sum +=i
    return sum
lst=[1,2,3,4]
print(a(*lst))

'''         第二个方法           '''
def b(*n):
    sum = 0
    for j in n:
        sum+=j
    return sum
print(b(1, 2, 3))
'''         判断一个值是否大于5          '''
def more_than_five(num):
    return num > 5

'''         返回最大数           '''
def max_num(lst):
    '''
    取最大值
    :param num: 表示接收 列表
    :return: 最大的 数值
    '''
    if not lst:
        return None
    max_value = lst[0]
    for i in lst:
        if max_value<i:
            max_value = i
    return max_value
#定义生成随机数的函数列表
def random_num_list(count):
    lst=[]
    import random
    # for i in range(count):
        





print(more_than_five(7))
'''         在字典中拿最高的成绩          '''
# dc = {'python': 90, 'java': 80, 'html': 60 }
# def get_max_score(dc_score):
#     '''
#     用于取字典数据:
#     :param dc_score:
#     :return: 取最高值以及科目
#     '''
#     dc_score={}
#     max_course=''
#     max_course_score=''
#     for k,v in dc_score.items():
#         if max_course_score < v:
#             max_course_score = v
#             max_course = k
#     return max_course_score,max_course
# course,score = get_max_score(dc)
# print(course,score)

'''         递归函数(第一种方法)            '''
# 阶乘
# 求5 的阶乘
# 5的阶乘 = 5*4*3*2*1 = 120
# def jie_cheng():
#     for i in range(1,10000):

def factorial(num):
    if num ==1:
        return 1*1
    return num * factorial(num-1)


print(factorial(5))
'''         第二种方法           '''
def recursion(num):
    counts=1
    for i in range(1,num+1):
        counts*=i
    return counts
print(recursion(5))
