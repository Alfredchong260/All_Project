"""
Dictionary is a collection which is unordered, changeable and indexed but no duplicate
"""

'''
Casting:
    int()
    str()
    float()

Constructor:
    list()
    tuple()
    set()
    dict()
'''

'''
All data types:
    string
    integer
    float
    list
    tuple
    set
    dict
'''
# Dict
person = {
    # key         value
    'first name': 'Chong',
    'surname' : 'Alfred',
    "age": 18,
    'sleep time': '5 hours'
}


# Use constructor
person2 = dict(first_name='Sara', last_name='Williams', age=18)

# Get key
# print(person.keys())

# Get value
# print(person.values())

# Add key/value
# person.setdefault('hobby', 'play badminton')
# person['sleep time'] = "10 hours"
# person['hobby'] = 'sleep'
# print(person)

# Get dict keys

# Get dict items
# print(person.items())

# Copy dict
# person3 = person
# print(person3)

# Remove item (del/pop)
# person.pop('first name')
# print(person)

# Clear
# person.clear()
# print(person)

# Get length
# print(len(person))

# List of dict
people = [
    {'name': 'Martha', 'age': 30},
    {'name': 'Kelvin', 'age': 20},
    [10, "opps"],
    'HAHAHAHA',
    ('Apples', 'Mango')
]



'''
Constructor:
    4 
'''
