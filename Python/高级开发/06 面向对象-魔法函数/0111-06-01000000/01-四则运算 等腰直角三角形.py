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
        self.slide = 0

    def __str__(self):
        self.area = 1/2 * self.side ** 2
        return f"<Area> {self.area}\n<Side 1 & Side 2> {self.side}"

    def __gt__(self, other):
        return f"self.area > Area2 : {self.area > other.area}"

    def __add__(self, other):
        self.area += other.area
        return f"<New Area {self.area}>"

    @property
    def area2(self):
        return self.area

    @property
    def side2(self):
        return self.side

tri1 = Triangle(side=5)
tri2 = Triangle(side=3)
print(tri1)
print()
print(tri2)
print()
# print(tri1 > tri2)
# print()
# print()
# print(tri1)
# print()
# print(tri2)

