def reverse_range(start, stop, step=1):
    current = stop
    while current > start:
        current -= step
        yield current


"""
自定义一个 reverse_range 函数,实现逆序输出range的内容

>>> list(range(1, 9))
>>> [1, 2, 3, 4, 5, 6, 7, 8]
>>> list(reverse_range(1, 9))
>>> [8, 7, 6, 5, 4, 3, 2, 1]
"""
g = reverse_range(1, 9)
print(list(g))
print(list(g))
