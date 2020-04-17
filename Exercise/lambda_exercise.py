# square

li = [5, 3, 6]

print(list(map(lambda item: item**2, li)))

# sorting

a = [(0, 2), (4, 3), (9, 9), (10, -1)]

a.sort(key=lambda x: x[1])

print(a)
