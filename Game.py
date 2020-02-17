from enum import IntEnum
from random import randint

# dict with selected option

choice = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
# computer choice
computer = choice.get(randint(1, 3))
player_point = 0
computer_point = 0
#player = False
while (player_point < 3) and (computer_point < 3):
    userInput = int(input('1. Rock, 2. Paper, 3. Scissors? You play to 3 points: '))
    player = choice.get(userInput)
    try:
        if player == computer:
            print("Tie!, no one gat point")
        elif player == 'Rock':
            if computer == 'Paper':
                computer_point += 1
                print('You lose ', computer, 'covers', player, "and get's point")
            else:
                player_point += 1
                print("You win!", player, "smashes", computer, "and you get a point")
        elif player == 'Scissors':
            if computer == 'Rock':
                computer_point += 1
                print('You lose', computer, 'smashes', player, "and get's point")
            else:
                player_point += 1
                print('You win!', player, 'cuts', computer, "and you get a point")
        elif player == 'Paper':
            if computer == 'Scissors':
                computer_point += 1
                print('You lose ', computer, 'cuts', player, "and get's point")
            else:
                player_point += 1
                print("You win!", player, 'covers', computer, "and you get a point")
        else:
            print('Something goes wrong, try again! ')
        print("Player's points:", player_point, "Computer points: ", computer_point)
    except ValueError:
        print('Non-numeric data found in the file.')

    #player = False
    computer = choice.get(randint(1, 3))
