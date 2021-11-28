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


class Hero:
    def __init__(self, name, weapon, equipment, blood):
        # self 是实例对象
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood

    # 如果类对象里面的方法接受的第一个参数是 self , 那就是实例对象
    def attack(self, other_hero):
        # other_hero 是什么? other_hero --> hero1 --> 黄忠
        return f'{self.name} 发动了攻击, 攻击了{other_hero.name}'


# hero1 是有 Hero 英雄类对象创建出来的实例对象, 拥有 Hero 对象的所有方法与属性
hero1 = Hero('黄忠', '弓箭', ['头盔', '靴子'], 100)
hero2 = Hero('刘备', '剑', ['头盔', '盔甲'], 100)
hero3 = Hero('关羽', '青龙映月刀', ['靴子'], 1000)

# 最终返回的结果是什么 ?
print(hero3.attack(hero1))
