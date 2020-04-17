# Error handling  --> try, except, else, finnaly, raise

while True:
    try:                                            # runs if there is no error
        point = int(input('What\'s your point? '))
        if point > 0:
            print(f'Your Score is {10/point}')
            break
        raise ValueError                            # to raise the error in valid too
    except (ValueError, ZeroDivisionError) as err:  # runs in an error given
        print(f'Please enter a valid point {err} ')
    else:                                           # runs if there is no error after try block
        print('Thank you!')
        break
    finally:                                        # runs every time
        print('No matter what this will be printed')
