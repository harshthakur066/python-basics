# in python function is defined by the keyword def i.e. def===function

# 1

from datetime import datetime


def print_time(display):
    print(display)
    print('task completed')
    print(datetime.now())
    print()


name = 'Harsh'
# print(name)
print_time(name)

for x in range(0, 10):
    print(x)
print_time(x)  # here x won't be printed but need to pass as a parameter


# 2

def get_initial(name):
    initial = name[0:1].upper()
    return initial


first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

print('Initials of your name are ' +
      get_initial(first_name) + ' ' + get_initial(last_name))
