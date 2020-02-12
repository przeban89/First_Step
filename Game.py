from enum import IntEnum
from random import randint

# list with selected option
# choice = IntEnum('choice', 'Rock, Paper, Scissors')
choice = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
# computer choice
computer = choice.get(randint(1, 3))

player = False
while not player:
    print(computer)
    userInput = int(input('1. Rock, 2. Paper, 3. Scissors? '))
    player = choice.get(userInput)
    try:
        if player == computer:
            print("Tie!")
        elif player == 'Rock':
            if computer == 'Paper':
                print('You lose ', computer, 'covers', player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == 'Scissors':
            if computer == 'Rock':
                print('You lose', computer, 'smashes', player)
            else:
                print('You win!', player, 'cut', computer)
        elif player == 'Paper':
            if computer == 'Scissors':
                print('You lose ', computer, 'smashes', player)
            else:
                print("You win!", player, 'covers', computer)
        else:
            print('Something goes wrong, try again! ')
    except ValueError:
        print('Non-numeric data found in the file.')

    player = False
    computer = choice.get(randint(1, 3))
