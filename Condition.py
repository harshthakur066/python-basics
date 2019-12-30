# elif (python syntex) ===else if
points = 0

pool = input('Do you play? ')

if pool.lower() == 'yes':
    score = input("What is your score? ")

    if score in('100', '90'):
        points = 10
    elif score == '80':
        points = 8
    else:
        points = 5

    print(points)
elif pool.lower() == 'no' or pool.lower() == 'nope':
    print(str(points) + ' Sorry')
else:
    print('Wrong Input')
