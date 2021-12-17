class ReverseRange(object):
    def __init__(self, start, stop, step=1):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = stop

    def __iter__(self):
        # 声明是一个迭代对象
        return self

    def __next__(self):
        # 迭代的规则
        self.current -= self.step
        if self.current >= self.start:
            return self.current
        else:
            raise StopIteration  # 结束迭代


"""
自定义一个 ReverseRange 生成器,实现逆序输出range的内容

>>> list(range(1, 9))
>>> [1, 2, 3, 4, 5, 6, 7, 8]
>>> list(ReverseRange(1, 9))
>>> [8, 7, 6, 5, 4, 3, 2, 1]
"""
g = ReverseRange(1, 9)
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# print(list(ReverseRange(1, 9)))
# for i in g:
#     print(i)
