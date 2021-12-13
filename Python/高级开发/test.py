class MyRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start

    def __iter__(self):
        # 可迭代对象的声明
        return self

    def __next__(self):
        # 迭代的规则
        self.current += self.step
        if self.current < self.stop:
            return self.current

        raise StopIteration

# # my_range 是一个生成器
# my_range = MyRange(0, 10, 1)

# print(list(my_range))

# for item in my_range:
#     print(item)

def my_range(start, stop, step):
    current = start
    while current < stop:
        yield current
        current += step

r = my_range(0, 10, 1)
for i in r:
    print(i)
