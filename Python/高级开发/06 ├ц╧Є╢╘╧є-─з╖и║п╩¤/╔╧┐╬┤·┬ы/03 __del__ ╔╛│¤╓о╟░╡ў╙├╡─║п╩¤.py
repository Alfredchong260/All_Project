class Son(object):
    def __new__(cls, *args, **kwargs):
        """
            从哪里来
        """
        print('__new__ 方法被调用了')
        instance = object.__new__(cls)
        return instance

    def __init__(self, name):
        print('__init__ 被调用了')
        self.name = name

    def __del__(self):
        # 对象被从内存中删除之前会调用的函数
        print(f'__del__ {self.name} 即将被删除')


son1 = Son('大儿子')
son2 = Son('二儿子')
son3 = Son('小儿子')

del son1  # 手动删除大儿子,删除之前会调用大儿子的 __del__
del son2  # 手动删除大儿子,删除之前会调用大儿子的 __del__
input('随便输入一点什么')
# 1. __new__ 使用类对象创建一个实例对象
# 2. __init__ 给实例对象绑定属性
# GC 垃圾回收机制,引用计数原理
