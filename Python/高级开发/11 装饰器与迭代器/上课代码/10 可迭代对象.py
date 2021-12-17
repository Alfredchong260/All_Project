class MyRange:
    def __init__(self, start, stop, step):
        self.start = start
        self.stop = stop
        self.step = step
        self.current = start  # 记录当前生成的数据到了那一个

    def __iter__(self):
        # 1. 可迭代对象的声明
        return self

    def __next__(self):
        # 2. 迭代规则
        self.current += self.step
        if self.current < self.stop:
            return self.current
        # 3. 迭代结束之后需要停止迭代
        raise StopIteration  # 迭代结束之后,主动报错


my_arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_range = MyRange(0, 10, 1)
# my_range 是什么东西 ? 可以当做列表使用,里面存储了需要用的数据
for item in my_range:
    print(item)
# my_range.current = 0  # 重置数据生成
print(list(my_arr))
"""
    100万个数据
    列表  : 列表里面存储的是数据,有多少的数据,占用多少的空间
    生成器 : 生成器存储的是数据生产的规则,只会生成一次 (速度快,节约内存)
    
    yield 
"""
