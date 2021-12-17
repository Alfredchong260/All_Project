class ReverseRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.step = -1
        self.current = stop

    def __iter__(self):

        return self

    def __next__(self):
        self.current -= 1

        if self.current < self.stop and self.current >= self.start:
            return self.current

        raise StopIteration


"""
自定义一个 ReverseRange 生成器,实现逆序输出range的内容

>>> list(range(1, 9))
>>> [1, 2, 3, 4, 5, 6, 7, 8]
>>> list(ReverseRange(1, 9))
>>> [8, 7, 6, 5, 4, 3, 2, 1]
"""
reverse_range = ReverseRange(1, 9)
for i in reverse_range:
    print(i)
