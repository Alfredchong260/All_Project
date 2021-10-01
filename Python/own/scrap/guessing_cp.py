import random

def guess(num):
    random_num = random.randint(1, num)

    guess = 0
    while guess != random_num:
        guess = int(input(f'Guess a number between 1 and {num}:'))
        if guess > random_num:
            print('Sorry, guess again, too high')

        elif guess < random_num:
            print('Sorry, guess again, too low')

    print(f'Congratulations, you are correct, the answer is {random_num}')

def com_guess():
    highest = int(input('Please set your highest range:'))
    lowest = int(input('Please set your lowest range:'))

    feedback = ''
    while feedback != 'c':
        if lowest != highest:
            guess = random.randint(lowest, highest)

        else:
            guess = low

        feedback = input((f'My choose is {guess}. Am i correct, Is it too high(H), too low(L) or correct(C):'))

        if feedback.lower() == 'h':
            highest = guess - 1 

        elif feedback.lower() == 'l':
            lowest = guess + 1 

    print(f"Yes i am right and the correct answer is {guess}")

# guess(10)
com_guess()
