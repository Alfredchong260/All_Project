# n!  5 ! 5 x 4 x 3 x 2 x 1

n = 5
total = 1
while n > 0:
    total *= n
    n -= 1
print('循环:\t', total)

total2 = 1
for item in range(5, 0, -1):
    total2 *= item
print('遍历:\t', total)


def n_n(n):
    print('n_n: 当前的n为{}'.format(n))
    if n > 1:
        return n * n_n(n - 1)  # 递归的结果是怎么算出来的? 5 * 4 * 3 * 2 * 1
    else:
        return 1


print('递归:\t', n_n(5))
