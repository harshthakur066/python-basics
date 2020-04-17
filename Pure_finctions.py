# pure functions are functions which gives same output every time for same input
# and dosn't have any side effects like dependent on a variable declared outside the function

# lambda are funtions to run at a time no need to allocate memory
# lambda item: action_on_item

from functools import reduce

li = [1, 2, 3, 4]
li2 = [66, 33, 76]

# map
print(list(map(lambda item: item*2, li)))

# filter
print(list(filter(lambda item: item % 2 != 0, li)))

# zip
print(list(zip(li, li2)))

# reduce
print(reduce(lambda acc, item: acc + item, li, 0))
