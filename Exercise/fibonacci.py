def fibo(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fibo(10):
    print(x)
