"""打印直角三角形
*
**
***
****
*****
"""

# print('*')
# print('**')
# print('***')
# print('****')
# print('*****')


# i = 1
# while i <= 5:
#     print('*' * i)  # 字符串相乘
#     i += 1

# 不能用字符串的乘法  打印的换行

# i = 3
# j = 1
# while j <= i:
#     print('*', end='')  # end 参数是 print打印的结束符号
#     j += 1


i = 1
while i <= 5:  # 1     2345
    j = 1  # 1
    while j <= i:  # 12345
        # end=''  嵌套循环中换行符是空字符串
        print('*', end='')
        j += 1
    i += 1
    print()  # print控制换行

# 层
# 1







