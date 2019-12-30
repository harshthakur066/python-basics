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

def get_initial(name, force_uppercase=True):  # parameter can be defaulted
    if(force_uppercase):
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial


first_name = input('What is your first name? ')
last_name = input('What is your last name? ')

if(first_name.isdigit() or last_name.isdigit()):
    print('Please enter a valid string')
else:
    print('Initials of your name are ' + get_initial(name=first_name) +
          ' ' + get_initial(last_name, False))
    # not necessary to pass second paramete since defaulted as True
