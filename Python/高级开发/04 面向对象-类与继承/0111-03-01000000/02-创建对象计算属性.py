"""
### 作业2

备注: 因为计算属性没有讲,可以用函数代替. 如果看不懂这句话,能做多少就做多少

1、创建一个游戏英雄类，
+ 分别有以下属性
  名字（name），武器（weapon）,装备（equipment）， 攻击力（power），
  血量（blood），怒气（anger），防御力（defence）

+ 每个英雄类都有游戏技能，分别为（行为）
  攻击（attack） 可以攻击另外一个实例对象
  放大招（nirvana）

用游戏英雄类创建三个游戏人物，分别是（属性）：
    - '韩信'，'弓箭', ['头盔', '靴子'], 15, 100, 0
    - '刘备', '剑', ['头盔', '盔甲'], 20, 100, 0
    - '李白'，'长枪'，['盔甲', '马']， 30, 100, 0

每个人都有游戏技能，分别为（行为）：
- 攻击
  调用一次 怒气 `+2` （修改anger值）
- 放大招
  怒气值满时自动放大招

"""

"""自己在下方编写代码实现功能"""
equipment_defence = {
    '头盔': 5,
    '靴子': 3,
    '盔甲': 9,
    '马': 9
}


class Hero:
    def __init__(self, name, weapon, equipment, power, blood, anger):
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.power = power
        self.blood = blood
        self.anger = anger

        # 防御力是根据装备计算出来的
        self.defence = self.computed_defence()

    def computed_defence(self):
        total = 0
        for equip in self.equipment:
            total += equipment_defence[equip]
        return total

    def attack(self, other_hero):
        # 攻击的逻辑 攻击了-防御力=造成的伤害(需要减去的血量)
        print(f'{self.name} 发动了攻击')
        diff = self.power - other_hero.defence
        if diff >= 0:
            other_hero.blood -= diff

        self.anger += 2
        # 自动释放大招
        if self.anger >= 100:
            self.nirvana()
            self.anger = 0

    def nirvana(self):
        print(f'{self.name} 释放了大招')


hero1 = Hero('韩信', '弓箭', ['头盔', '靴子'], 15, 100, 0)
hero2 = Hero('刘备', '剑', ['头盔', '盔甲'], 20, 100, 0)
hero3 = Hero('李白', '长枪', ['盔甲', '马'], 30, 100, 0)
print(hero1.defence)
print(hero1.computed_defence())
print(hero3.defence)

hero2.attack(hero3)
print(hero3.blood)
