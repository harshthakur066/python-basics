# list unpacking
# *<variable> take items which are not assiged
# d has assigned to the last item

a, b, c, *left, d, e = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(a)
print(b)
print(c)
print(d)
print(e)
print(left)
