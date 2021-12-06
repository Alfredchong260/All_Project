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

class Ball:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f"<Circle {self.radius}>"

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def circum(self):
        return 2 * math.pi * self.radius

ball1 = Ball(3)
ball2 = Ball(5)
ball3 = Ball(2)
print(ball1)
print(ball2)
