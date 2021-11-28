class Animal(object):
    """动物类"""

    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        # return self.name + ' 正在慢吞吞吃东西'
        return self.name + ' 正在吃东西'


class Tiger(Animal):
    def __init__(self, name, high, weight):
        super().__init__(name, high, weight)

    def bark(self):
        return f'{self.name} 正在嗷呜~~~叫'

    # def eat(self):  # 重写,子类的函数名覆盖父类
    #     # 彻底重写,会将父类的方法完全覆盖
    #     return self.name + ' 正在吃东西' + ' 发出咔咔咔的声音'

    def eat(self):
        # 重写,拓展父类函数的功能
        return super().eat() + ' 发出咔咔咔的声音'


a = Animal('普通动物', '0 cm', '0 kg')
tiger = Tiger('虎大', '250 cm', '360 kg')
print(a.eat())
print(tiger.eat())
