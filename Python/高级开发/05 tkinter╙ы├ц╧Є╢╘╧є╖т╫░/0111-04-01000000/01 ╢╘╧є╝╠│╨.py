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
    def __init__(self, name, high, width, blood, anger, magical=0):
        super(Mage, self).__init__(name, high, width, blood, anger)
        self.magical = magical  # 默认为 0 最大为100
        self.max_magical = 100

    def attack(self):
        print(self.name + '发起攻击')
        self.anger += 2
        if self.anger == 100:
            self.second()
            self.anger = 0

        self.magical += 5
        # 默认魔法值到100的时候自动释放技能
        if self.magical >= self.max_magical:
            self.nirvana()
            self.magical = 0

    def second(self):
        print(f'{self.name} 切换到了第二形态')
        self.max_magical = 50  # 第二形态魔法最大值修改为 50
        # self.max_magical = self.max_magical * 0.5  # 100 50 25 12.5

    # 怒气值满时自动放大招
    def nirvana(self):
        print(self.name, '释放了大招(Mage职业)')
        self.magical = 0


class Tank(Hero):
    def attack(self):
        self.anger += 3
        super(Tank, self).attack()

    # 怒气值满时自动放大招
    def nirvana(self):
        print(self.name, '释放了大招(Tank职业)')
        self.blood = self.blood * 2
