class Father(object):
    def __init__(self, name):
        # print('Father init')
        self.name = name

    def say_hello(self):
        print('Father say hello ')

    def father_func(self):
        pass


class Son(Father):
    def __new__(cls, *args, **kwargs):
        print('当前类对象的方法  :\t', dir(cls), cls)
        instance = object.__new__(cls)  # 空壳实例对象
        print('当前实例对象的方法:\t', dir(instance), instance)
        return instance

    def __init__(self, name):
        # print('Son init')
        super(Son, self).__init__(name)  # 调用父类的 init 方法
        print('当前实例对象的方法:\t', dir(self), self)
        print('Son init2')

    def say_hello(self):
        print('Son say hello ')

    def son_func(self):
        pass

    def son_func2(self):
        pass


son1 = Son('大儿子')
son2 = Son('二儿子')
print(son1)
son1.say_hello()
