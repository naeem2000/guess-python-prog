import random

print('Welcome, just a simple program to put my python basics in action!')

# variables
guessValue = random.randint(1, 10)

running = True

rounds = 5

# main guess function
def guesser():
    global running
    global rounds
    guess_str = input(f'Guess any number from 1 to 10, you have {rounds} rounds left: ')
    guess = int(guess_str)
    if guess == guessValue:
        print('Correct!')
        rounds = rounds - 1
    else:
        print('Try again...')
    if rounds < 1:
       running = False
       print('Good Job! Re-run the program to start over')

# start over or exit
def guesser_again():
    global running
    global rounds
    restart_prompt = input('Start over? y/n ')
    answer = restart_prompt
    if answer == 'y':
        running = True
        rounds = 5
        while running:
            guesser()
    elif answer == 'n':
        print('Thank you for trying it out!')
        exit()

# execute
while running:
    guesser()

# condition
while not running:
    guesser_again()

