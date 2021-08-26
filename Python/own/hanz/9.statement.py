# If/Else statements are used to decide to do something

x = 10
y = 3

# Compare

if x > y:
    print(f'{x} is greater than {y}')

else:
    print(f"{y} is greater than {x}")

# Can do more than one comparison

if x > y:
    print(f'{x} is greater than {y}')

elif x == y:
    print(f"{x} is equal to {y}")

else:
    print(f"{y} is greater than {x}")

# Nested if statements

if x > y:
    if x <= 10:
        print(f"{x} more than {y} and equal to 10")
    
# Statements with logical operators
"""
    ==
    !=
    <=
    <
    =>
    >
    in
    not in
    is
    is not
"""
