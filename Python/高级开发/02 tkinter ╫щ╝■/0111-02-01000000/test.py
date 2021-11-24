class HERO:
    def __init__(self, name, weapon, equipment, blood) -> None:
        self.name = name
        self.weapon = weapon
        self.equipment = equipment
        self.blood = blood

    def attack(self):
        return f"{self.name} 发动了攻击"


hero1 = HERO('刘备', '喷子', ['草帽', '靴子'], 3300)
hero2 = HERO('黄忠', '意大利大炮', ['大炮', '靴子'], 3100)

# print(hero1.attack())
# print(hero2.attack())

