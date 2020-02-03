# ------- Global Variables --------
# Game board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
#If game is still going
game_still_going = True
#Who won? Or tie?
winner = None
#Whos turn is it?
current_player = "X"

#Display board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | ")

#Play the game of "Tic tac toe"
def play_game():

    #Display initial board
    display_board()

    # While the game is still going
    while game_still_going:

        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # Check to the other player
        check_if_game_over()

        # Flip to the other player
        flip_player()
    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " Won. ")
    elif winner == None:
        print("Tie. ")

#Handle a single turn of an arbitary player
def handle_turn(player):
    print(player + "'s turn.")
    position = input(""" 
 1 | 2 | 3 
 4 | 5 | 6 
 7 | 8 | 9 
Chose a posution from 1-9: """)

    while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Invalid input. Choose a position 1-9:")


    position = int(position) - 1

    board[position] = player

    display_board()


def check_if_game_over():
    check_for_winner()
    check_if_tie()

def check_for_winner():
    # Set up global variables
    global winner

    # check rows
    row_winner = chcek_rows()
    # check columns
    column_winner = check_columns()
    #check diagnolas
    diagonal_winner = check_diagonals()
    if row_winner:
        #there was a win
        winner = row_winner
    elif column_winner:
        #there was a win
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
        #there was a win
    else:
        #there was a draw
        winner = None
    return

def chcek_rows():
    #Set up global variables
    global game_still_going
    #Check if any of the rows have all the same value(and is not empty)
    row_1 = board[0] == board[1] == board [2] != "-"
    row_2 = board[3] == board[4] == board [5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
# If any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    # Set up global variables
    global game_still_going
    # Check if any of the columns have all the same value(and is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # If any column does have a match, flag that there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # Set up global variables
    global game_still_going
    # Check if any of the diagonals have all the same value(and is not empty)
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[2] == board[4] == board[6] != "-"
    # If any diagonal does have a match, flag that there is a win
    if diagonals_1 or diagonals_2:
        game_still_going = False
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[2]
    return

def check_if_tie():
    global game_still_going
    if "-" not in board:
        game_still_going = False
    return

def flip_player():
    # global variables we need
    global current_player
    # if current player was X, the change it to O
    if current_player == "X":
        current_player = "O"
    # if the current player was O, the change it to X
    elif current_player == "O":
        current_player = "X"
    return
play_game()