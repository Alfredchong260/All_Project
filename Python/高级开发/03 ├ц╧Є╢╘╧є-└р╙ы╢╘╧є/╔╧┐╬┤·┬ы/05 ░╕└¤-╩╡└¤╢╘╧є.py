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
import tkinter

# Hero 类对象
class Hero:
    def __init__(self, name, weapon, equipment, blood):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood

    def attack(self):
        return f'{self.name} 发动了攻击'


# 使用类对象创建一个实例对象
# 实例对象是具体到某一个人, 类对象是某一类事物的统称
hero1 = Hero('黄忠', '弓箭', ['头盔', '靴子'], 100)
hero2 = Hero('刘备', '剑', ['头盔', '盔甲'], 100)

print(hero1.name, hero1.weapon, hero1.equipment, hero1.attack())
print(hero1.equipment)
print(hero1.equipment[0])
print(hero1.equipment[1])
