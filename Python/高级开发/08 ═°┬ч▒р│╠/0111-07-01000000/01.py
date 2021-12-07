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
import arithmetic

print(arithmetic)
print(arithmetic.add(1, 3))
print(arithmetic.plus)
print(arithmetic.plus.add(1, 3))
