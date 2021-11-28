"""
    人:
        属性: 名字,身高,体重 ....
        行为: 吃饭/喝酒/打招呼 ...
"""


# def eat():
#     print('正在吃饭')
#
#
# def say_hello(name):
#     print(f'{name} 正在打招呼')
#
#
# person = {'name': '正心', 'high': '240 cm', 'weight': '120 kg', 'eat': eat, 'say_hello': say_hello}
#
# print('名字:', person['name'])
# print('身高:', person['high'])
# person['say_hello'](person['name'])


# 面向对象写法
# 1. 将 人 这个类的概念全部抽象出来
class Person:  # 类的名字用大驼峰命名法
    def __init__(self, name, high):
        # 初始化函数 也是一个普通函数,只是有特殊的功能
        self.name = name
        self.high = high

    def eat(self):
        print('正在吃饭')

    def say_hello(self):
        print(f'{self.name} 正在打招呼')


print(Person)
# 类对象名字 + () 调用类对象创建实例对象 --> __init__
person = Person(name='正心', high='240 cm')
print('person:\t', person)
print('姓名:\t', person.name)
print('身高:\t', person.high)
# 实例对象.方法 + () 调用类对象里面的方法
person.eat()
person.say_hello()
