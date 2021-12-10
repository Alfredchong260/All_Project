""""""
"""
定义一个名为 arithmetic 的包名
    包里面分别有四个模块, 模块里面拥有方法
        plus.py
            def add(x, y):
                return x + y
        decrease.py
            def sub(x, y):
                return x - y
        divide.py
            def div(x, y):
                return x * y
        multiply.py
            def mul(x, y):
                return x / y
    将所有模块的内容暴露在 init 文件。
"""
from arithmetic import sub, add, mul ,div

a = sub(10, 5)
print(a)

b = add(10, 5)
print(b)

c = mul(10, 5)
print(c)

d = div(10, 5)
print(d)
