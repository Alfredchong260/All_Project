import random

def play():
    li = ['r', 's', 'p']
    user = input("'r' for Rock, 'p' for Paper, 's' for scissors :")
    computer = random.choice(li)

    if user == computer:
        print('Draw') 

    if win(player=user, opponent=computer):
        print('You Win')

    else:
        print('You Lose')

def win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):

        return True

play()
