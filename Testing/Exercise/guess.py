import random


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print('You cracked it!')
            return True
    else:
        print('Hey, I said from 1~10')
        return False


if __name__ == '__main__':
    answer = random.randint(1, 10)

    while True:
        try:
            guess = int(input('Guess a number from 1~10 '))
            if(run_guess(guess, answer)):
                break
        except ValueError:
            print('Please enter a number')
            continue
