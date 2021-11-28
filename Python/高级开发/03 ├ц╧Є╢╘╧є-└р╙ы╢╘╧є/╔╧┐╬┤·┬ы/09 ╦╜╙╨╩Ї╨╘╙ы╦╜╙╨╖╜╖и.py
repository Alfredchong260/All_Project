class Women(object):

    def __init__(self, name, high, age):
        self.name = name
        self.high = high
        # 双下划线 私有属性 外部无法调用
        self.__age = age

    def __fly(self):
        return self.__age

    def __secret(self):
        print("我的年龄是 %d" % self.__age)


fang = Women("小芳", '180 cm', 18)
print(fang.name)
print(fang.high)
# print(fang.__age)
# print(fang.__fly())
