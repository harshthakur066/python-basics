# Dictionary : dict(key: 'value') == {'key': 'value'}

user = {
    'name': 'Harsh',
    'age': 20,
    'knowledge': ['Python', 'JavaScript', 'C++', 'C'],
    'numbers': [1, 2, 3, 5]
}

print(user.items())  # returns a tupple
print(user.get('knowledge'))  # return the value if exists otherwise None
print(user.values())
print(user.keys())
print(user.pop('numbers'))
user.update({'age': 30})  # updates the value of the key
user.update({'year': 2000})  # adds on the key with the value if not find
print(user)
