"""
    人:
        属性: 名字,身高,体重 ....
        行为: 吃饭/喝酒/打招呼 ...
"""


class Person:
    def __init__(self, name, high, color='yellow'):
        # 初始化方法就相当于人出生的时候
        self.name = name
        self.high = high
        self.color = color

    def say_hello(self):
        return f'{self.name} 问你吃了没?'

    def cry(self):
        return f'{self.name} 正在哇哇哇的大哭'


zx = Person('正心', '30 cm')
wz = Person(name='丸子', high='35 cm')

print(zx.high)
print(zx.say_hello())
print(zx.cry())
