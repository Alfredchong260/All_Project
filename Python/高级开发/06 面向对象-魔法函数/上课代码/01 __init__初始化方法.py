class Son(object):
    def __init__(self, name):
        """
            我是谁
            初始化方法 --> 魔法函数,是背后自动进行调用的
            创建实例对象的时候会自动调用
            可以在给实例对象初始化一些属性
        """
        self.name = name
        print(f'Son {self.name} __init__')


# Son('大儿子')
son1 = Son('大儿子')
son2 = Son('二儿子')
son3 = Son('小儿子')

# print(son1.name, son2.name, son3.name)
