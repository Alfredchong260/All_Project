# object 顶级父类
# 对象与函数的区别 ?
# class Animal:  # 如果不写默认就继承 object
# 原始基类
class Animal(object):
    """动物类"""

    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        return self.name + ' 正在吃东西'


class Tiger(Animal):
    """这里是一个老虎类"""
    pass


tiger = Tiger('虎大', '250 cm', '360 kg')
tiger.nick_name = '虎'
print(tiger.name)
print(tiger.eat())
# print(tiger.bark())
print('__dict__', tiger.__dict__)
"""
    查找顺序
    tiger 自己本身(实例对象) --> Tiger(类对象)  --> Animal(父类对象) --> object(基类 不能继续向上找)
    向上查找机制
"""
