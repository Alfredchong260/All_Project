# If/Else statements are used to decide to do something

# Compare

# if x < y:
#     print(f'{x} is greater than {y}')

# else:
#     print(f"{y} is greater than {x}")

# Can do more than one comparison

'''
= : setup variable
== : equal
'''

# if x > y:
#     print(f'{x} is greater than {y}')

# elif x == y:
#     print(f"{x} is equal to {y}")

# else:
#     print(f"{y} is greater than {x}")

# Nested if statements

'''
    Nested for loop
    Nested while loop
'''

x = 9
y = 6

# if x > y:
#     if x >= 10:
#         print(f"{x} more than {y} and equal or more than 10")
#     else:
#         print(f"{x} is more than {y} but less than 10")
    
# Statements with logical operators
"""
    ==
    !=
    <=
    <
    >=
    >
    in
    not in
    is
    is not

Comparing
"""

a = [1,2,3,4,5]
b = 6

# if b == a[0]:
#     print(b)

# elif b == a[1]:
#     print(f"{b} is index 1")

# elif b == a[3]:
#     print(f"{b} is index 3")

# else:
#     print(f"{b} is not stored in {a}")

if b not in a:
    print(f"{b} not store in {a}")
else:
    print(f'{b} stored in {a}')
