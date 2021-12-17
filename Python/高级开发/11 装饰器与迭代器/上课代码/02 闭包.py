number = 10


def print_msg():
    # 局部作用域
    number = 20  # 能不能修改 number ?

    def printer():
        # 布局作用域里面的局部作用域
        msg = '我是函数里面的函数'
        return msg

    def change_number(value):
        nonlocal number  # 申明不是本地变量,就会向上查找
        number = value

    def get_number():
        return number

    class Person:  # 可以这样定义吗 ?
        def __init__(self):
            pass

    return number, printer, change_number, get_number  # 加括号之后得到的是什么东西 ?


# 函数对象 + () 就是调用函数
number, p_func, c_func, g_func = print_msg()
print('number:\t', number)
print('p_func:\t', p_func)  # 会打印一个什么东西
print('p_func():\t', p_func())  # 会打印一个什么东西
c_func(100)
print('g_func():\t', g_func())
"""
    正常情况,根据GC机制,函数被调用之后,里面的内容全部会被清空
    
    引用计数
"""
# print(num)
