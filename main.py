import random

guessValue = random.randint(1, 10)
print('Welcome, just a simple program to put my python basics in action!')

running = True

rounds = 5

while running:
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
