class Animal(object):
    """动物类"""

    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        return self.name + ' 正在吃东西'


# class Tiger(object):
#     """老虎类"""
#
#     def __init__(self, name, high, weight):
#         self.name = name
#         self.high = high
#         self.weight = weight
#
#     def eat(self):
#         return self.name + ' 正在吃东西'

# 子承父业: Tiger 继承 Animal 类,会享受 Animal 封装好的一切属性与方法
# 一代更比一代强:
class Tiger(Animal):
    def __init__(self, name, high, weight):
        # 子承父业 需要承担对应的责任,就需要进行重写
        # Animal.__init__(self, name, high, weight)
        # super(Tiger, self).__init__(name, high, weight)

        # Animal.__init__(self, name, high, weight)
        super().__init__(name, high, weight)  # 
        # 调用父类的 init 方法,绑定实例对象


tiger = Tiger('虎大', '250 cm', '360 kg')
print(tiger.eat())
print(tiger.name)
print(tiger.high)
print(tiger.weight)
