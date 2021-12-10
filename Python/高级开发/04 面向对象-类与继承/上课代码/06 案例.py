""""""
"""
炼体 PracticeBody
    属性：
        血量(blood)
        体力(power)
    行为：
        挑水（carry_water）
            挑水消耗2点体力
        砍柴（chop_wood）
            砍柴消耗3点体力

练气 PracticeMagic
    属性：
        血量
        体力
      + 灵力（magical_power）
    行为：
        挑水
            挑水消耗0.2点灵力
        砍柴
            砍柴消耗0.3点灵力
      + 御风(fly)
            御风消耗2点灵力
      + 喷火(spurt_fire)
            喷火消耗2点灵力

练神 PracticeDivine
    属性：
        血量
        体力
        灵力
      + 神力(super_power)
    行为：
      - 挑水
      - 砍柴
        御风
            御风消耗0.2点神力
        喷火
            喷火消耗0.2点神力
      + 御剑(flying_sword)
            御剑飞行消耗 2 点神力
"""


class PracticeBody(object):
    def __init__(self, blood, power):
        self.blood = blood
        self.power = power

    def carry_water(self):
        self.power -= 2

    def chop_wood(self):
        self.power -= 3


class PracticeMagic(PracticeBody):
    def __init__(self, blood, power, magical_power):
        super().__init__(blood, power)
        self.magical_power = magical_power

    def carry_water(self):
        self.magical_power -= 0.2

    def chop_wood(self):
        self.magical_power -= 0.3

    def fly(self):
        self.magical_power -= 2

    def spurt_fire(self):
        self.magical_power -= 3


class PracticeDivine(PracticeMagic):
    def __init__(self, name, blood, power, magical_power, super_power):
        super().__init__(blood, power, magical_power)
        self.super_power = super_power
        self.name = name

    def carry_water(self):
        raise Exception('炼神器不会挑水低级技能')  # 主动抛出错误
        # pass  # 有但是不能用

    def chop_wood(self):
        self.magical_power -= 0.3

    def fly(self):
        self.super_power -= 0.2

    def spurt_fire(self):
        self.super_power -= 0.3

    def flying_sword(self):
        self.super_power -= 2
        return f'{self.name} 正在御剑飞行'


zs = PracticeDivine('张三', 1000, 1000, 1000, 100)
print(zs.flying_sword())
print(zs.carry_water())
