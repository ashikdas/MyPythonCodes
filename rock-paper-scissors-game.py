print('What do you want to choose? rock, paper, scissors')
p1 = input()
print('What do you want to choose? rock, paper, scissors')
p2 = input()


def game(a, b):
    if a == b:
        return "It's tie!"
    elif a == 'rock':
        if b == 'scissors':
            return "Rock beats Scissors!"
        elif b == 'paper':
            return "Paper beats Rocks!"
    elif a == 'scissors':
        if b == 'rock':
            return "Rock beats Scissors!"
        elif b == 'paper':
            return "Scissors beats Paper!"
    elif a == 'paper':
        if b == 'scissors':
            return "Scissors beats Papers!"
        elif b == 'rock':
            return "Paper beats Rocks!"
    else:
        return "You haven't entered rock, paper or scissors. "


print(game(p1, p2))
