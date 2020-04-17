def generator_func(num):
    for i in range(num):
        yield i


g = generator_func(10)

while True:
    try:
        print(next(g))
    except StopIteration:
        print('Done')
        break
