arr = [
    [1,    2,   3,   4],
    ['a', 'b', 'c', 'd']
]

# 多维列表的取值, 要看清楚嵌套关系
# print(arr[1][3])

# for row in arr:  #
#     for col in row:
#         print(col)


row = len(arr)  # 2

for i in range(row):  # 0 1   行索引
    for j in range(len(arr[i])):  # 列索引
        print(arr[i][j])
        if j == 1:
            arr[i][j] = 0

print(arr)
