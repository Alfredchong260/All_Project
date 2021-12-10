class Animal(object):
    """动物类"""

    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        return self.name + ' 正在吃东西'


# 子承父业: Tiger 继承 Animal 类,会享受 Animal 封装好的一切属性与方法
# 一代更比一代强:
class Tiger(Animal):
    def __init__(self, name, high, weight, color):
        # tiger -> self
        super().__init__(name, high, weight)  # 虎大 调用父类的初始化方法绑定 名字 身高 体重
        self.color = color
        # 老虎相比普通的动物多了毛发的颜色

    def bark(self):
        return f'{self.name} 正在嗷呜~~~叫'


a = Animal('1', '0 cm', '0 kg')
tiger = Tiger('虎大', '250 cm', '360 kg', '黄色')
print(tiger.eat())
print(tiger.name)
print(tiger.high)
print(tiger.weight)
print(tiger.bark())
print(tiger.color)
