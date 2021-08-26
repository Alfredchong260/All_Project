'''
    类 即面向对象
'''

class User:
    # Constructor
    # 初始化
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        return f"My name is {self.name} and i am {self.age} years old"

    def birthday(self):
        self.age += 1

# Extend Class

