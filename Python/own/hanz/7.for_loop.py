"""
    for loop is used for iterating over a sequence, can be list, tuple, dict, set or string
"""

#           -4      -3     -2          -1
# index     0       1       2           3
people = ['John', 'Paul', 'Kelvin', 'Alfred', 1, 2, 3, 4, 5, 6 ,7, 8, 9, 0]
# print(people[::-1])

# for i in range(5):
#     print(i)

# for i in range(10):
#     print('*')

# for i in people:
#     print(i)

# for x in range(1, 10, 2): # Condition
#     print(x)        # Do something

# Break
# for c in people:
#     print(c)
#     break

# Continue
# for i in people:
#     print(i)

# Range
# for i in range(10):
#     print('hello')

'''
    range define do command how many times
    list (Collection of data) : how many elements inside the collection, do how many times
'''
# for i in range(len(people)):
#     print(people)

# for i in range(6):
#     print('Hello World')
'''
    list ,range
'''
# for i in range(1, 6):
#     print('*' * i)


'''
*
**
***
****
*****
'''

''''
*****
****
***
**
*
'''

'''
*****
 ****
  ***
   **
    *
'''

'''
    *
   **
  ***
 ****
*****
'''

# |5 4 3 2 1 |0 -1 -2 -3
# 0 1 2 3 4 5
# for i in range(5, 0, -1):
#     print('*' * i)


# for i in range(5, 0, -1):
#     # 5 4 3 2 1 
#     # 0 1 2 3 4
#     space_num = 5 - i
#     for j in range(space_num):
#         print(' ', end='')
#     for k in range(i):
#         print('*', end='')
#     print()
# for i in range(1, 6):
#     space_num = 5 - i
#     for j in range(space_num):
#         print(' ', end='')
#     for k in range(i):
#         print('*', end='')
#     print()

# for i in range(5, 0, -1):
#     print('*' * i)

'''
    嵌套式
    Nested for loop
'''

# for i in range(1, 10):
#     for j in range(1, i):
#         print(f"{j}X{i}={i*j}", end='  ')
#     print()


a = [[1,2,3,4,5,6], [0,9,8,7,6,5,4]]
# for i in a:
#     for j in i:
#         print(j)

