"""
球球大作战

球的属性
    半径
    周长
    面积

需要实现的行为：
    大球吃小球，面积相加，返回一个新的球


r 为半径，D 为直径
面积：S=πr²; S=π(d/2）^2
周长：C=πD=2πR
"""
import math


class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def c(self):
        return 2 * math.pi * self.r

    @property
    def area(self):
        return math.pi * self.r * self.r

    def __add__(self, other):
        new_area = self.area + other.area
        new_r = math.sqrt(new_area / math.pi)
        return Circle(new_r)

    def __str__(self):
        return f'<Circle r:{self.r}>'


c1 = Circle(5.5)
c2 = Circle(5.6)
c3 = c1 + c2
print(c3)
