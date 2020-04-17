# list
li = [item for item in 'hello']
print(li)

li2 = [num for num in range(0, 100)]  # as variable
print(li2)

li3 = [num*2 for num in range(0, 100)]  # as expression
print(li3)

li4 = [num**2 for num in range(1, 100)
       if num % 2 == 0]  # as expression with condition
print(li4)

# comprehension can also be applied on sets same as list but to remember sets gives unique values

# dictionary
simple_dict = {
    'a': 1,
    'b': 2
}

my_dict = {k: v**2 for k, v in simple_dict.items() if v % 2 == 0}

print(my_dict)

my_dict2 = {num: num*2 for num in [1, 2, 3]}

print(my_dict2)
