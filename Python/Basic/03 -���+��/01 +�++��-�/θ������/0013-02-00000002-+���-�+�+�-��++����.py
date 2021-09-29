"""
用for语句实现九九乘法表
"""

for i in range(1, 10):  # 123456789   行数
    for j in range(1, i + 1):  # range  左闭右开  列数
        print(f'{j} * {i} = {i * j}', end='\t')
    print()  # 控制换行



