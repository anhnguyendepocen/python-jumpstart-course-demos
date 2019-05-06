import random

print('-------------------------------')
print('    GUESS THAT NUMBER GAME')
print('-------------------------------')
print('Welcome to Guess That Number!')
print()

name = input('What is your name? ')
print()
print("Hey Brad! I'm going to draw a random number between 0 and 100 and you need to guess it.")

the_number = random.randint(0, 100)

guess_num = -1

while guess_num != the_number:
    guess_text = input("What's your guess? ")
    guess_num = int(guess_text)

    if guess_num < the_number:
        print('Sorry {0}, your guess of {1} is too low'.format(name, guess_num))
    elif guess_num > the_number:
        print('Sorry {0}, your guess of {1} is too high'.format(name, guess_num))
    else:
        print("That's right {0}, {1} is spot on! Thanks for playing.".format(name, guess_num))

