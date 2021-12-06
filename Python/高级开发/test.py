import math


class Father(object):
    def __init__(self, name):
        # print('Father init')
        self.name = name

    def say_hello(self):
        print('Father say hello')

    def father_fuc(self):
        pass


class Son(Father):
    def __new__(cls, *args, **kwargs):
        # print('当前类对象的方法', dir(cls), cls)
        instance = object.__new__(cls)  # 绑定当前对象的方法
        # print('当前实例对象的方法', dir(instance), instance)
        return instance

    def __init__(self, name):
        print('Son init')
        super(Son, self).__init__(name)     # 调用父类的init方法

    def say_hello(self):
        print("Son say hello")

    def __str__(self):
        return f"<Son> {self.name}"

    # 重写删除时会发生的事
    def __del__(self):
        print(f"__del__ {self.name}")

def create_son():
    son = Son('私生子')
    print(son)

create_son()

son1 = Son('大儿子')
input()
# print(son1)


class RectAngle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def __str__(self):
        # 改变默认的输出信息
        return f'<RectAngle {self.width} x {self.height}>'

    def __repr__(self):
        # 修改调试代码默认输出的信息
        return f'<RectAngle {self.width} x {self.height}>'

    def __bool__(self):
        # 转换默认布尔值的返回值
        return False if self.area() < 10 else True

    def __gt__(self, other):
        return f"rect1 > rect2:\t{self.area() > other.area()}"


# rect1 = RectAngle(10, 12)
# rect2 = RectAngle(8, 10)

# print('rect1:\t', rect1, type(rect1))
# print('str(rect1):\t', str(rect1), type(str(rect1)))
# print()
# print(rect1, rect2) # 打印输出对象的信息 --> 输出对象的信息会进行转换 --> __str__
# print([rect1, rect2]) # 打印输出列表的信息 -->

# print(bool(rect1))
# print(bool(RectAngle(1, 5)))
# print(rect1 > rect2)

# 扑克牌的大小比较

# 自定义一套比较规则
weights = {'3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6,
           '9': 7, '10': 8, 'J': 9, 'Q': 10, 'K': 11, 'A': 12, '2': 13}


class Hearts:
    def __init__(self, value):
        self.value = value

    def __gt__(self, other):
        return weights[self.value] > weights[other.value]

    def __str__(self):
        return f"<Hearts {self.value}>"

# A = Hearts('A')
# K = Hearts('K')
# print(A)
# print(K)
# print('A > K:\t', A > K)


class Square:
    def __init__(self, width):
        self.width = width

    def area(self):
        return self.width * self.width

    def __str__(self):
        # 改变默认的输出信息
        return f'<RectAngle {self.area()}>'

    def __repr__(self):
        # 修改调试代码默认输出的信息
        return f'<RectAngle {self.width} x {self.width}>'

    def __bool__(self):
        # 转换默认布尔值的返回值
        return False if self.area() < 10 else True

    def __gt__(self, other):
        return f"rect1 > rect2:\t{self.area() > other.area()}"

    def __add__(self, other):
        new_area = self.area() + other.area()
        new_width = math.sqrt(new_area)
        if self.area() > other.area():
            self.width = new_width
            other.width = 0

        else:
            self.width = 0
            other.width = new_width


# sq1 = Square(4)
# sq2 = Square(3)
# print(sq1)
# print(sq2)
# print(sq1 + sq2)
# print(sq1)
# print(sq2)
# print(globals())    # python代码环境默认会进行引用
