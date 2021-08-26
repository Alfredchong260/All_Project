"""
json is commonly used with data APIS
"""

import json

# Example of JSON
userJSON = '{"first_name": "John", "last_name": "Alfred", "age": 18}'

user = json.loads(userJSON)

print(user)
