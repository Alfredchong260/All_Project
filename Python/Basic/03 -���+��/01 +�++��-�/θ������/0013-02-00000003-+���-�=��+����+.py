"""
根据正左角形,倒左三角形 打印正右三角形，倒右三角形

要打印的效果:正右角形
    *
   **
  ***
 ****
*****
"""

print('-------打印正左角形--------')
for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end='')
    print()

print('-------打印倒左三角形--------')
for i in range(6, 0, -1):
    for j in range(1, i + 1):
        print('*', end='')
    print()
"""请在下方实现代码逻辑"""
print('-------打印正右角形--------')
"""
    *  
   **
  ***
 ****
*****
"""

for i in range(1, 6):  # 控制行数
    # 先打印空格
    for k in range(1, 6 - i):
        print(' ', end='')
    # 打印小星星
    for j in range(1, i + 1):
        print('*', end='')
    print()  # 换行

print('-------打印倒右角形--------')
"""
*****
 ****
  ***
   **
    *
"""

for i in range(5, 0, -1):  # 54321
    for k in range(5 - i):
        print(' ', end='')
    for j in range(1, i + 1):
        print('*', end='')
    print()
