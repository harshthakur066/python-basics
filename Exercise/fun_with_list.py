lst = []

n = int(input('Enter number of elemets '))

for i in range(0, n):
    ele = int(input('Enter the element '))
    lst.append(ele)


def fun_69(lst):
    total = 0
    to_add = True

    for i in lst:
        while to_add:
            if i != 6:
                total += i
                break
            else:
                to_add = False
        while not to_add:
            if i != 9:
                break
            else:
                to_add = True

    return total


print('Answer:', fun_69(lst))
