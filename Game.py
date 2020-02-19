from random import randint

play = True
while play:
    # dict with selected option
    choice = {1: 'Rock', 2: 'Paper', 3: 'Scissors'}
    computer = choice.get(randint(1, 3))
    #count setup
    player_point = 0
    computer_point = 0

    while (player_point < 3) and (computer_point < 3):
        try:
            #Input with player decision (1-3)
            userInput = int(input('1. Rock, 2. Paper, 3. Scissors? You play to 3 points: '))
            player = choice.get(userInput)

            if player == computer:
                print("Tie!, no one get point")
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
                print("Wrong number, try again!")
            print("Player's points:", player_point, "Computer points: ", computer_point)

        except ValueError:
            print('Non-numeric data found in the file. Try again!')
        computer = choice.get(randint(1, 3))
    if player_point == 3:
        print(('Player WIN! Congratulatuon!'))
    else:
        print('Computers Win! You are loser!')
    again = str(input('Do you want try again?, tap anythink to restart or n = if you wont break the game?: '))
    try:
        if again == 'n':
            print("Thanks for playing the game :) ")
            break
        else:
            print("Let's try again")
    except ValueError:
        print('Non-numeric data found in the file.')