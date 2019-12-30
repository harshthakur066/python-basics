# both isdigit() and isdecimal() are same

num1 = input('Enter a number ')
print()
num2 = input('Enter another number ')

if(num1.isdigit()):
    print()
    print(num1)
else:
    print()
    print('please enter a valid number')

if(num2.isdecimal()):
    print()
    print(num2)
else:
    print()
    print('please enter a valid number')

# to check the input is float or not
