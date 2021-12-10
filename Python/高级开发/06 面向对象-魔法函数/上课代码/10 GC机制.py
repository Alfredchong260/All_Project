# 引用计数

class Son(object):
    def __init__(self, name):
        self.name = name

    def __del__(self):
        print(f'__del__ {self.name} 即将被删除')

    def __str__(self):
        return f'<Son {self.name}>'

    def say_hello(self):
        pass


def create_son():
    # 函数里面的变量只能存在于函数内部
    son = Son('小儿子（函数内部）')  # 2. 在函数内部创建一个对象,引用计数+1
    print('son', son)
    input('函数内部，请随便输入一个东西')
    # 函数运行之后，函数内部所有的变量都会被删除（GC机制）

# son1 = Son('大儿子')
# son1_copy = son1  # 对象引用
# son2 = son1  # 对象引用
# # 当一个对象在内存中被删除的时候, 就会调用 del 方法
# del son1
# del son1_copy
create_son()  # 1. 调用函数
# 当退出函数之后,函数内部变量的应用数就会变成0,所以会被删除
print(globals())  # python代码环境默认会进行引用
input("请输入任意内容")  # 3. 函数结束完之后,程序主要部分

"""
    模块与包的导入
    
    ctrl + 鼠标左键 点进源码
    对象被GC机制处理之前，会通知 __del__ 一下。
    日志：对象在被清理之前，记录一下
"""
