def higest_even(li):
    even = []
    for i in li:
        if not i % 2:
            even.append(i)
    print(even)
    return max(even)


print(higest_even([10, 2, 3, 4, 8, 11]))
