# Scope is releted to function
x = 10


def func():
    total = 100
    print(x)


# print(total) won't work out of scope
func()

print()

a = 1


def confusion():
    a = 10
    print(f'confusion {a}')


confusion()
print(a)  # won't change to 10

print()

total = 0


def count():
    '''
    For global keyword
    '''
    # total = 0 will reset again whenever function called so we won;t define total here
    global total
    total += 1
    return total


count()
count()
print(count())

print()


def outer():
    y = "local"

    def inner():
        nonlocal y
        y = "nonlocal"
        print("inner:", y)
    inner()
    print("outer:", y)


outer()
