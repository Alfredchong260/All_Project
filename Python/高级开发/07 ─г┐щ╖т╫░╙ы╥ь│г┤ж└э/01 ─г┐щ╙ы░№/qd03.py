"""
    模块: 所有的 py 都是一个模块

"""
# 2. 从文件里面导入对象
from qd01 import pi, Circle, add

print(pi)
print(Circle)
c1 = Circle(4)
c2 = Circle(5)
c3 = add(c1, c2)
print(c3)

"""

import tkinter  
    导入简单,但是会占用相对较多的内存


from tkinter import Tk, Label, Text, LEFT, CENTER
    导入的时候会稍微麻烦,但是占用的内存更少

"""
