""""""
"""
动物类（Animal）：
    属性：name, high, weight
    行为：吃

老虎类（Tiger）：
    属性：name, high, weight
    行为：吃、老虎的技能

狮子类（Lion）：
    属性：name, high, weight
    行为：吃、狮子的技能

狮虎兽（Liger）：
    属性：name, high, weight
    行为：吃、老虎的技能、狮子的技能
"""


class Animal(object):
    def __init__(self, name, high, weight):
        self.name = name
        self.high = high
        self.weight = weight

    def eat(self):
        return f'{self.name} 正在吃东西'


class Tiger(Animal):
    def __init__(self, name, high, weight):
        super(Tiger, self).__init__(name, high, weight)

    def tiger_skill(self):
        return f' {self.name} 释放了 森林之王的怒火'

    def bark(self):
        return f'{self.name} 正在嗷呜~~~叫'


class Lion(Animal):
    def __init__(self, name, high, weight, color):
        Animal.__init__(self, name, high, weight)
        self.color = color
        # 狮子比老虎多出了一个输出

    def lion_skill(self):
        return f' {self.name} 释放了 草原之王的怒火'

    def bark(self):
        return f'{self.name} 正在吼吼~~~叫'


class Liger(Lion, Tiger):
    def __init__(self, name, high, weight, color):
        # 老虎是三个属性
        # 狮子是四个属性
        # super().__init__(name, high, weight, color)
        Lion.__init__(self, name, high, weight, color)
        Tiger.__init__(self, name, high, weight)

    def bark(self):
        # super 找父类,将找到的第一个父类直接返回
        return super().bark() + '(<Liger>)'


print(Liger.__mro__)
liger = Liger('狮虎兽', '175 cm', '360 kg', '黄色')
print(liger.bark())
