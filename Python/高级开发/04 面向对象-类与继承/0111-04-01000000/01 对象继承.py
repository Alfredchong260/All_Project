"""
作业1
在Hero的基础上，新增了两种游戏英雄，多了下面内容

法师（Mage）
    增加属性：魔法值（magical 默认0，最大100）

    - 攻击：
        调用一次 怒气 `+2`
        调用一次 魔法值 `+5`

    - 放大招
      魔法值满时自动放大招

    - 第二形态
      当怒气值满时 自动切换第二形态（魔法值最大值修改为50）

坦克（Tank）

    - 修改方法：
        调用一次 怒气 `+5` （修改anger值）

    - 放大招
      怒气值满值，当前剩余血量翻倍
"""

"""自己在下方编写代码实现功能"""


class Hero(object):
    def __init__(self, name, high, width, blood, anger):
        self.name = name
        self.high = high
        self.width = width
        self.blood = blood
        self.anger = anger

    # 怒气值满时自动放大招
    def nirvana(self):
        if self.anger >= 100:
            print(self.name, '释放了大招')
        else:
            print('怒气值没有充满')

    # 调用一次 怒气 `+2` （修改anger值）
    def attack(self):
        print(self.name + '发起攻击')
        self.anger += 2
        if self.anger == 100:
            return self.nirvana()

class Mage(Hero):
    def __init__(self, name, high, width, blood, anger):
        super().__init__(name, high, width, blood, anger)
        self.magical = 0
        self.stage = 1
        self.max = 100

    def attack(self):
        self.magical += 5
        super().attack()

        if self.magical >= self.max:
            self.magical -= self.max
            self.nirvana()

        if self.anger >= 100:
            self.stage_two()

    def stage_two(self):
        self.max = 50
        self.stage = 2
        self.anger = 0
        print(f"{self.name} 切换成第二形态")

class Tank(Hero):
    def attack(self):
        super().attack()
        self.anger += 3

    def nirvana(self):
        super().nirvana()
        self.blood *= 2


# mage = Mage('法师', 100, 100, 100, 0)
# mage.attack()
# mage.attack()
# print(mage.anger)
# print(mage.magical)
# print(mage.max)

# tank = Tank('坦克', 100, 100, 200, 0)
# tank.attack()
# print(tank.anger)
# print(tank.blood)
