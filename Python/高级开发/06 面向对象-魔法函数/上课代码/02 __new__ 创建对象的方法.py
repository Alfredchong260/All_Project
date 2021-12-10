class Son(object):
    def __new__(cls, *args, **kwargs):
        """
            从哪里来
        """
        print('__new__ 方法被调用了')
        # instance 创建的实例对象
        instance = object.__new__(cls)  # object 是顶级父类
        print('__new__', instance)
        return instance  # __new__ 必须返回一个实例对象

    def __init__(self, name):
        """ 我是谁
            初始化方法 --> 魔法函数,是背后自动进行调用的
        """
        print('__init__', self)
        self.name = name
        print(f'Son {self.name} __init__')


# Son('大儿子')
son1 = Son('大儿子')
print(son1)
# 1. __new__ 使用类对象创建一个实例对象
# 2. __init__ 给实例对象绑定属性
"""
    魔法方法 内置的特殊功能
"""
