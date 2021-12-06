import datetime


class RectAngle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        # 修改默认的输出信息
        return f'<RectAngle {self.width}(w) x {self.height}(h)>'

    def __repr__(self):
        # 修改调试代码默认输出的信息
        return f'<RectAngle {self.width}(w) x {self.height}(h)>'

    def __bool__(self):
        # 改变默认布尔类型的转化形式
        return False if self.area() < 10 else True

    def __gt__(self, other):
        # 大于符号的运算规则
        return self.area() > other.area()


# 比较运算 大于 等于 小于
rect1 = RectAngle(4, 5)
rect2 = RectAngle(3, 6)
one = int('1')
two = int('2')

print('rect1 > rect2:\t', rect1.area() > rect2.area())
print('rect1 > rect2:\t', rect1 > rect2)
print('one > two:\t', one > two)
