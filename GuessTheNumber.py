import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess == random_number:
            print(f"wow, good job! The number was {random_number}")
        elif guess > random_number:
            print("try lower buddy")
        else:   
            print("a little higher there pal")

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    attempts = 0
    print('Think of a number 1-1000')
    input('Press enter when ready')
    print('')
    try:
        while feedback != 'c':
            feedback = ''
            if low != high:
                guess = random.randint(low,high)
            else:
                guess = low # debugs the situation where randint throws an error when low == high
            guess = random.randint(low,high)
            while feedback != 'h' and feedback != 'l' and feedback != 'c':
                print(f'Is your number higher(H) or lower(L), or is {guess} correct(C)??')
                feedback = input().lower()
            if feedback == 'h':
                low = guess + 1
            elif feedback == 'l':
                high = guess - 1
            attempts += 1
        print(f'Yay! The computer guessed your number, {guess}, correctly!')
        print(f'It took {attempts} attempts today. ')
    except:
        print("Hey recheck your inputs because you tricked me at some point!") #debugs an user error if they put an input incorrectly
 

computer_guess(1000)

#guess(10)
