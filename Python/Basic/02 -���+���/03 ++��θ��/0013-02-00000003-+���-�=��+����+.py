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

for i in range(1, 6):
    space_num = 5 - i
    for j in range(space_num):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()

print('-------打印倒右角形--------')
for i in range(1, 6):
    star = 5 - i
    for j in range(1, i + 1):
        print(' ', end='')
    for k in range(star + 1):
        print('*', end='')
    print()
