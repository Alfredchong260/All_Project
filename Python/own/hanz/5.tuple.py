"""
Tuple is also a collection in ordered but unchangeable, allows duplicate members
"""

# Tuples
fruits = ('Apples', 'Oranges', 'Grapes')
fruits1 = ('Apples')
fruits2 = ('Apples',)

print(type(fruits1))
print(type(fruits2))

# Get a value
# print(fruits[1])

# Can't change any value from a tuple

# Add duplicate

# Delete tuple

# Get length


"""
Set is also a collection in ordered and changeable but don't allows duplicate members
"""

'''
    () : Tuple
    [] : List
    {} : Set, Dict
'''
# Set
fruits_set = {'Apples', 'Oranges', 'Grapes', 'Apples'}
#print(a)
# fruits_set.add('Mango')
print(fruits_set)

# Check if in set
# print('Apples' in fruits_set)

# Add value
# fruits_set.add('Mango')

# Remove value
# fruits_set.remove('Apples')
# print(fruits_set)

# Add duplicate

# Clear set

# Delete

"""
    List : in ordered, changeable, allows duplicate value
    Tuple : in ordered, unchangeable, allows duplicate value
    Set : not in ordered, changeable, not allows duplicate value
    Dict : not in ordered, changeable, not allows duplicate value
"""

a = '10'
b = [1, 2, 3]
# Casting
# print(str(b))
# Constructor
# print(list(a))
# print(set(b))


set1 = {'Apples', 'Grapes'}
dict1 = {'Apples': 'A fruit that can in red or green', 'Grapes': 3}
#           Key         Value                           Key    Value
dict1['Apples'] = 'This is just a fruit'
print(dict1['Apples'])

'''
    List : append, extend, clear, pop
    Tuple: 
    Set : add, remove, clear
    Dict : items, keys, values
'''
dict1['Apples'] = 'This a an apple'
dict1['Mango'] = 'This mango very fresh'
print(dict1)
