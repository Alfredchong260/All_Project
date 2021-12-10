"""
### 作业2

备注: 因为计算属性没有讲,可以用函数代替. 如果看不懂这句话,能做多少就做多少

1、创建一个游戏英雄类，
+ 分别有以下属性
  名字（name），武器（weapon）,装备（equipment）， 攻击力（power），血量（blood），怒气（anger），防御力（defence）
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

        self.defence = 0
        self.defence = self.__count_defence()

    def attack(self, others_hero):

        self.anger += 2

        diff = self.power - others_hero.defence

        if diff >= 0:
            others_hero.blood -= diff

        if self.anger == 100:
            a = self.nirvana()
            return a

        return f"{self.name} 正在攻击 {others_hero.name}"

    def __count_defence(self):
        total = 0
        for equip in self.equipment:
            total += equipment_defence[equip]

        return total
    
    def nirvana(self):
        if self.anger == 100:
            return f"{self.name} 释放大招"
        return f"{self.name} 怒气值不足"

hero1 = Hero('韩信', '弓箭', ['头盔', '靴子'], 15, 100, 0)
hero2 = Hero('刘备', '剑', ['头盔', '盔甲'], 20, 100, 0)
hero3 = Hero('李白','长枪',['盔甲', '马'], 30, 100, 0)

print(hero1.attack(hero3))
print(hero3.blood)
