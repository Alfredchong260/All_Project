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
