"""
    定义一个等腰直角三角形的模型，求第三边（勾股定理：两直角边的平方和等于斜边的平方a²+b²＝c²）
    模型：Distance
        属性：侧边（side）
        行为：
            四则运算：两个三角形面积相加，返回一个新的等腰直角三角形
            逻辑运算：两个三角形能进行面积比较
        特性：
            面积（area）
            可以给设置面积，然后重新求侧边
"""
import math


class Triangle:
    def __init__(self, side):
        self.side = side
        # self.area = self.side * self.side / 2

    def __add__(self, other):
        new_area = self.area() + other.area()
        new_side = math.sqrt(new_area * 2)
        return Triangle(new_side)

    def area(self):
        return self.side * self.side / 2

    def __str__(self):
        return f'<Triangle side:{self.side}>'

    def __gt__(self, other):
        return self.area() > other.area()

    @property  # 特性,计算属性
    def area2(self):
        return self.side * self.side / 2

    @property  # 特性,计算属性
    def length(self):
        x = self.side * self.side + self.side * self.side
        return self.side + self.side + math.sqrt(x)  # math.sqrt 开根号


t1 = Triangle(5)
# t2 = Triangle(6)
# t3 = t1 + t2
# print(t3)
# print(t1 > t2)
# print(t1.area2())
t1.side = t1.side
print(t1.area2)
print(t1.length)
