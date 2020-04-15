# tuples are like list but immutable(can't be modified)

tuple = (1, 2, 4, 5, 5, 6)
x = tuple[1:2]

print(x)
print(tuple.count(5))
print(len(tuple))
print(tuple.index(4))
