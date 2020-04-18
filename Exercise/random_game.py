from random import randint
from sys import argv

print('Ready to play a game')
print()
try:
    # a = [int(input('Enter a number '))]
    # b = int(input('Enter second number '))
    a = int(argv[1])  # takes the input while runnig the file
    b = int(argv[2])
except ValueError:
    print('Enter valid numbers with run command')
else:
    y = randint(a, b)
    while True:
        try:
            x = int(input('your number '))
        except ValueError:
            print('Enter a valid number')
        else:
            if x == y:
                print('Hurray you guessed right one')
                break
            print('Oops! wrong guess try again')


# first = argv()
