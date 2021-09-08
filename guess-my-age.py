# This is a game of guessing the age of a person that lives inside the game.
# User has limited attempts to guess the age or he fails is a loser.

import random as r

secret_age = r.randint(1, 10)
flag = False


def game_func(guessed_age, secret_age):
    if guessed_age < secret_age:
        return 'Too low'
    elif guessed_age > secret_age:
        return 'Too high'
    else:
        return 'CORRECT!'


for i in range(1, 6):
    print('Take a guess. You have ' + str(6 - i) + ' guess left.')
    guessed_age = input()
    return_value = game_func(int(guessed_age), secret_age)
    if return_value == 'CORRECT!':
        print('YOU WON THE GAME!')
        flag = True
        break
    else:
        print(return_value)
if not flag:
    print('YOU LOST THE GAME!')
