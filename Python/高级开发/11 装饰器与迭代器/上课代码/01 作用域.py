"""
表达不清楚自己意思 (无法沟通) --> 把问题描述清楚

装饰器 迭代器 生成器
"""
# 内置作用域
print(print, int)  # str def class bool .....



# 全局作用域
import tkinter as tk
from tkinter import *
number = 10


def print_msg():
    # 局部作用域
    number = 20
    return number


print('全局作用域:\t', number)  # 10
print('局部作用域:\t', print_msg())  # 20
print('全局作用域:\t', number)  # 10
