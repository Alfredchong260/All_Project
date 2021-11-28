"""
    人:
        属性: 名字,身高,体重 ....
        行为: 吃饭/喝酒/打招呼 ...
"""


def eat():
    print('正在吃饭')


def say_hello(name):
    print(f'{name} 正在打招呼')

person = {'name': '正心', 'high': '240 cm', 'weight': '120 kg', 'eat': eat, 'say_hello': say_hello}

print('名字:', person['name'])
print('身高:', person['high'])
# 行为 --> 方法 理解敲 1 不理解敲2
# person -> 字典对象
# person['say_hello'] --> say_hello 方法
# person['say_hello'] --> say_hello 方法
# person['name'] --> '正心'
# person['say_hello'](person['name'])
person['say_hello'](person['name'])

# 面向对象写法
# 1. 将 人 这个类的概念全部抽象出来
