import math


class Circle:
    """球体对象"""

    def __init__(self, r):
        self.r = r

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


# 定义了常量
pi = 3.14


# 封住了方法
def add(c1, c2):
    return c1 + c2
