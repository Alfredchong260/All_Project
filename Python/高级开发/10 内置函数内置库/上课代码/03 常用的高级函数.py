arr = [(1, 2), (4, 1), (9, 10), (13, -3)]


def sort_order(temp):
    print('排序规则:\t', temp)
    return temp[1]


# sort_order = lambda temp: temp[1]
arr.sort(key=sort_order)
print(arr)

# def add(x, y):
#     return x + y

# 匿名函数,一次性用品
add = lambda x, y: x + y

print(add(4, 5))
