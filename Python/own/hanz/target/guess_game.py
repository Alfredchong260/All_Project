import random

# random number
number = random.randint(1, 10)
"""
    Difference datatype cannot compare
"""

# 死循环
# check answer
while True:
    num1 = input('Please enter a value : ')

    if int(num1) == number :
        print('You Win')
        break
    else:
        # print('You Lose')
        if int(num1) > number:
            print('Too big')
        elif int(num1) < number:
            print('Too small')

# 6

'''
电脑也需要知道它猜的号码 太大 太小
'''

'''
casting:
    float()
    str()
    int()
'''

# Case sensitive

highest = int(input('Please enter the maximum value : '))
lowest = int(input('Please enter the minimum value : '))

while True:
    number = random.randint(lowest, highest)

    print(number)

    judge = input('Correct(C), Too Small(S), Too Big(B) : ')
    if judge.upper() == 'C':
        print('Yea Computer Win')
        break
    elif judge.upper() == 'S':
        lowest = number + 1
    elif judge.upper() == 'B':
        highest = number - 1
