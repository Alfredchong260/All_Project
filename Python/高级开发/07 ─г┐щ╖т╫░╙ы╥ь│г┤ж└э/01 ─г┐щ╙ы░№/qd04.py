"""
    模块: 所有的 py 都是一个模块

"""

from qd01 import pi as qi_pi, Circle, add, math
# 3. 从模块里面将所有的内容全部导入 (非常不推荐使用)
# math.pi
from math import *  # * 通配符,指代任意的内容
from tkinter import *

print(Label)
print(pi)
print(qi_pi)
print(math)  # math --> qd01.py --> built-in(内置模块)
