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

rect1 = RectAngle(4, 5)
rect2 = RectAngle(8, 10)
# 默认打印出来的是对象的内容存地址信息
print(rect1)
print('rect1:\t', rect1, type(rect1))
print('str(rect1):\t', str(rect1), type(str(rect1)))
print('----------华丽的分割线-------------')
print(rect1, rect2)  # 打印输出对象的信息 --> 输出对象的信息会进行转化 --> __str__
print([rect1, rect2])  # 打印输出列表对象的信息 -->
