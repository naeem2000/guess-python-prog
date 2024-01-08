import random

# variables
print('Welcome, just a simple program to put my python basics in action!')

guessValue = random.randint(1, 10)

running = True

rounds = 5

# guess
def guesser():
    global running
    global rounds
    guess_str = input(f'Guess any number from 1 to 10, you have {rounds} rounds left: ')
    guess = int(guess_str)
    if guess == guessValue:
        print('Correct!')
        rounds = rounds - 1
        random.randint(1, 10)
    else:
        print('Try again...')
    if rounds < 1:
       running = False
       print('Good Job! Re-run the program to start over')

# execute
while running:
    guesser()

# condition
while not running:
    restart_prompt = input('Start over? y/n ')
    answer = restart_prompt
    if restart_prompt == 'y':
        running = True
        rounds = 5
        guesser()
        break
    elif restart_prompt == 'n':
        running = False
        break

