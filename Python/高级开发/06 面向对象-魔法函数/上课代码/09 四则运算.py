import datetime
import math


class RectAngle:
    """正方形 面积相加之后好求边长"""

    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width * self.width

    def __str__(self):
        return f'<RectAngle {self.width}>'

    def __gt__(self, other):
        # 大于符号的运算规则
        return self.area() > other.area()

    def __add__(self, other):
        # 1. 矩形相加之后,大的矩形把小的矩形吞掉
        new_area = self.area() + other.area()  # 面积+面积算出新的边长
        new_width = math.sqrt(new_area)
        # if self.area() > other.area():
        #     self.width = new_width
        #     other.width = 0
        # else:
        #     self.width = 0
        #     other.width = new_width
        return RectAngle(new_width)


# 比较运算 大于 等于 小于
rect1 = RectAngle(4.4)
rect2 = RectAngle(4.3)

# 可以实现四则运算的规则
# 1. 矩形相加之后,大的矩形把小的矩形吞掉
# 2. 矩形相加之后, 返回一个新的矩形, 原有的矩形不发送变化
print('rect1:\t', rect1)
print('rect2:\t', rect2)
print('rect1 + rect2:\t', rect1 + rect2)
print('rect1:\t', rect1)
print('rect2:\t', rect2)

# 魔法函数: 没有代码不能实现的,只是你目前技术不够

# 圆1 半径3   圆2 半径5
# 两个圆的面积相加之后新圆的半径是多少  3 + 5 = 8 ?
