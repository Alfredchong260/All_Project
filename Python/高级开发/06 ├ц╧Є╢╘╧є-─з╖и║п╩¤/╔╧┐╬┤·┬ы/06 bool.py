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


"""
    Python 默认的规则
    数字除了零之外都是 True
    对象除了空对象之外, 都是 True
"""

"""
    自定义的规则
    矩形对象面积小于 10 全部为 False,大于 10 为 True
"""
rect1 = RectAngle(4, 5)
print(bool(rect1))
print(bool(RectAngle(1, 5)))
# if rect1: # 会满足条件
