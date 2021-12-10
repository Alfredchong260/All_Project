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
    def tiger_skill(self):
        return f' {self.name} 释放了 森林之王的怒火'

    def bark(self):
        return f'{self.name} 正在嗷呜~~~叫'


class Lion(Animal):

    def lion_skill(self):
        return f' {self.name} 释放了 草原之王的怒火'

    def bark(self):
        return f'{self.name} 正在吼吼~~~叫'


class Liger(Lion, Tiger):
    pass


liger = Liger('狮虎兽', '175 cm', '360 kg')
print(liger.lion_skill())
print(liger.tiger_skill())
print(liger.bark())
print(Liger.__mro__)
"""
    遵循向上查找的规则
    
    一脉单传,多继承
    
"""
