"""
*
**
***
****
*****

要打印的效果:正右三角形
    *
   **
  ***
 ****
*****
"""

print(list(range(1)))
print('-------------正左三角形--------------')
for i in range(1, 6): # 12345
    for j in range(i):
        print('*', end='')
    print()

print('-------------正右三角形--------------')
for i in range(1, 6):  # 打印行数  12345
    # 先打印空格
    space_num = 5 - i
    for k in range(space_num):
        print(' ', end='')
    # 再打印小星星
    for j in range(i):
        print('*', end='')

    print()

