"""
创建一个游戏英雄类，

分别有以下属性
    名字（name），武器（weapon），装备（equipment），血量（blood）

每个英雄类都有游戏技能，分别为（行为）
  攻击（attack）,对被攻击人造成对等的攻击力伤害

创建两个英雄
    '黄忠', '弓箭', ['头盔', '靴子'], 100
    '刘备', '剑', ['头盔', '盔甲'], 100
"""


class Person:
    # 人类 这个对象有没有自己的特征 ?
    hand = 2  # 每一个人都有两只手
    head = 1
    class_name = '人类'

    # 人类 这一个概念拥有的属性 叫做类属性

    def __init__(self, name, weapon, equipment, blood):
        # 初始化方法里面的属性都是实例属性(实例对象的属性)
        # 具体某一个人拥有的属性
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood

    # 方法中第一个参数接收的是 self 就都是实例方法
    def attack(self, other_hero):
        # 具体某一个人拥有的方法
        return f'{self.name} 发动了攻击, 攻击了{other_hero.name}'

    # 类方法
    @classmethod  # java 注解 python 装饰器
    def boast(cls):
        return cls.class_name + ' 会吹牛'

    # 静态方法 不需要使用类对象与实例对象
    @staticmethod
    def info():
        # 在这个方法里面不需要使用到实例对象,也不需要用到类对象
        return '人类生活在地球'



# 牛 耕地
hero1 = Person('黄忠', '弓箭', ['头盔', '靴子'], 100)
hero2 = Person('刘备', '剑', ['头盔', '盔甲'], 100)
# 新增了一个实例属性
hero1.hand = 6  # 修改手的属性为 6 基因突变
print('黄忠的手有', hero1.hand, '只')

print('刘备的手有', hero2.hand, '只')

# python 是一门动态语言,一切皆可变
# 类对象可以直接调用类属性类方法静态方法
print(Person.class_name)
print(Person.info())
# 类对象无法调用实例对方与方法
# print(Person.attack(hero2))

"""
    类对象
        hand = 4
        实例对象
            实例属性
    
    黄忠 身高 体重 爱好
    刘备 身高 体重 爱好
    关羽 身高 体重 爱好 hand = 6
"""