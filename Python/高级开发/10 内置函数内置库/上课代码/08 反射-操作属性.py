import random


class Circle:
    def __init__(self, r):
        self.r = r


c = Circle(5)
attr = 'color'
# c.color = '黄色'
setattr(c, attr, '黄色')

# print(c.color)
print(getattr(c, 'color'))
# 能设置吗 ? 会报错吗 ?

# del c.color
f = random.random()
print(f)
if f > 0.5:
    delattr(c, 'color')

# 如果有 color 这个属性,就打印,没有就设置一个新的再打印
# 获取 color 之前就要判断有没有这个属性
if hasattr(c, attr):
    print(getattr(c, 'color'))
else:
    setattr(c, attr, '绿色')
    print(getattr(c, 'color'))
