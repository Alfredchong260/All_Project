import math


class Circle:
    def __init__(self, r):
        self.r = r

    def c(self):
        return 2 * math.pi * self.r

    @property
    def area(self):
        return math.pi * self.r * self.r


c1 = Circle(5.5)
print(c1.c())
print(c1.area)

# response.text  response.content
# response.json()
