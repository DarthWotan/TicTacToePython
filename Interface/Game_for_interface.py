# ------- Global Variables -------

# If game is still going
game_is_going = True

# position
position = "3"
position_bot = ""

# Who is the winner? Tie?
winner = ""
winner_name = ""
player_1 = ""
player_2 = ""

# playing alone or with friend
alone = ""

# Who's turn is it?
current_player = 1
current_player_name = None

# ------- Imports -------

import random
import time
import numpy as np


# Game Board
board = np.zeros((3,3))
board = [int(board[0][0]), int(board[0][1]), int(board[0,2]),
         int(board[1][0]), int(board[1][1]), int(board[1,2]),
         int(board[1][0]), int(board[1][1]), int(board[1,2])]




def display_board():
    print(str(board[0]) + " | " + str(board[1]) + " | " + str(board[2]))
    print(str(board[3]) + " | " + str(board[4]) + " | " + str(board[5]))
    print(str(board[6]) + " | " + str(board[7]) + " | " + str(board[8]) + "\n")


# Game function for TicTacToe
def game():
    global game_is_going
    global current_player
    global current_player_name
    global winner
    global winner_name
    global player_1
    global player_2
    global alone

    valid = False
    alone = input("Play alone: ")
    while not valid:
        if alone in ["yes", "no"]:
            valid = True
        else:
            print("Sorry, this is no option!")
            alone = input("Play alone: ")

    if alone == "no":
        player_1 = input("Player1: ")
        player_2 = input("Player2: ")
    else:
        player_1 = input("Player1: ")
        player_2 = str(picking_name())
    current_player_name = player_1

    display_board()

    if alone == "no":
        while game_is_going:
            handle_turn(current_player, current_player_name)

            check_game()

            flip_player()
    else:
        print("This time you are playing against " + player_2 + "\n")
        while game_is_going:
            handle_turn(current_player, player_1)

            check_game()

            if game_is_going == True:
                print(player_2 + "'s turn! Let him think, he needs his time!")
                time.sleep(random.randint(0, 2))
                bot("O")
                check_game()
    # The game has ended
    if winner == 1 or winner == 2:
        name_of_winner()
        print("Congratulations!\nThe winner is: " + str(winner_name))
    elif winner == None:
        print("Tie!")

def handle_turn(player, name):
    global position
    global alone

    if alone == "no":
        print(str(name) + "'s turn ('" + str(player) + "')")
    else:
        print("Now it's your turn, " + str(name) + " ^-^")
    position = input("Position from 1-9 or a1, b2, c3, etc.: ")

    # valid position?
    valid = False
    while not valid:
        # position isn't between 1-9?
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "a1", "a2", "a3", "b1", "b2", "b3", "c1",
                               "c2", "c3", "end"]:
            position = input("Choose a position from 1-9 or a1, b2, c3, etc: ")
        if position not in ["a1", "a2", "a3", "b1", "b2", "b3", "c1", "c2", "c3"]:
            position = int(position) - 1
        else:
            position = declare(position)

        # is position free?
        if board[position] == 0:
            valid = True
        else:
            print("You can't go there. Try again")

    board[position] = player

    display_board()

def check_game():
    win()
    tie()

def win():
    # set up for global winner
    global winner

    # check rows
    row_winner = check_rows()
    # check columns
    column_winner = check_columns()
    # check diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_rows():
    global game_is_going

    # check if there is any winner row
    row_1 = board[0] == board[1] == board[2] != 0
    row_2 = board[3] == board[4] == board[5] != 0
    row_3 = board[6] == board[7] == board[8] != 0
    if row_1 or row_2 or row_3:
        game_is_going = False
    # check the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    global game_is_going

    # check if there is any winner row
    column_1 = board[0] == board[3] == board[6] != 0
    column_2 = board[1] == board[4] == board[7] != 0
    column_3 = board[2] == board[5] == board[8] != 0
    if column_1 or column_2 or column_3:
        game_is_going = False
    # check the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_is_going

    # check if there is any winner row
    diagonal_1 = board[0] == board[4] == board[8] != 0
    diagonal_2 = board[2] == board[4] == board[6] != 0
    if diagonal_1 or diagonal_2:
        game_is_going = False
    # check the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]

    return

def tie():
    global game_is_going

    if 0 not in board:
        game_is_going = False
    return

def flip_player():
    global current_player
    global current_player_name

    # changes the current player
    if current_player == 1:
        current_player = 2
        current_player_name = player_2
    elif current_player == 2:
        current_player = 1
        current_player_name = player_1
    return

def name_of_winner():
    global winner
    global winner_name
    global player_1
    global player_2

    # set the name of the winner
    if winner == 1:
        winner_name = player_1
    elif winner == 2:
        winner_name = player_2

# function to check if someone gives up (not working yet)
def give_up():
    global current_player
    global position
    global game_is_going
    global winner

    # checks if the player gives up
    if position == "end":
        if current_player == 1:
            winner = 2
        elif current_player == 2:
            winner = 1
        game_is_going = False
        return True

    # function to make an algorithm, which places the mark

def bot(player):

    global position_bot
    valid = False
    while not valid:
        # check if there are 2 in a row
        two_in_row = check_rows_bot()
        # check if there are 2 in a check_columns
        two_in_columns = check_columns_bot()
        # check if there are 2 in a diagonal
        two_in_diagonals = check_diagonals_bot()

        if two_in_row:
            time.sleep(0.5)
            position_bot = two_in_row
        elif two_in_columns:
            time.sleep(0.5)
            position_bot = two_in_columns
        elif two_in_diagonals:
            time.sleep(0.5)
            position_bot = two_in_diagonals
        else:
            position_bot = random.randint(0, 8)
        if board[position_bot] == 0:
            valid = True
    board[position_bot] = player
    display_board()

def check_rows_bot():
    check_1 = board[0] == board[1] != 0
    pos_1 = 2
    check_2 = board[0] == board[2] != 0
    pos_2 = 1
    check_3 = board[1] == board[2] != 0
    pos_3 = 0

    check_4 = board[3] == board[4] != 0
    pos_4 = 5
    check_5 = board[3] == board[5] != 0
    pos_5 = 4
    check_6 = board[4] == board[5] != 0
    pos_6 = 3

    check_7 = board[6] == board[7] != 0
    pos_7 = 8
    check_8 = board[6] == board[8] != 0
    pos_8 = 7
    check_9 = board[7] == board[8] != 0
    pos_9 = 6

    if check_1 and board[pos_1] != 1 and board[pos_1] != 2:
        return pos_1
    elif check_2 and board[pos_2] != 1 and board[pos_2] != 2:
        return pos_2
    elif check_3 and board[pos_3] != 1 and board[pos_3] != 2:
        return pos_3

    elif check_4 and board[pos_4] != 1 and board[pos_4] != 2:
        return pos_4
    elif check_5 and board[pos_5] != 1 and board[pos_5] != 2:
        return pos_5
    elif check_6 and board[pos_6] != 1 and board[pos_6] != 2:
        return pos_6

    elif check_7 and board[pos_7] != 1 and board[pos_7] != 2:
        return pos_7
    elif check_8 and board[pos_8] != 1 and board[pos_8] != 2:
        return pos_8
    elif check_9 and board[pos_9] != 1 and board[pos_9] != 2:
        return pos_9

    return

def check_columns_bot():
    check_1 = board[0] == board[3] != 0
    pos_1 = 6
    check_2 = board[0] == board[6] != 0
    pos_2 = 3
    check_3 = board[3] == board[6] != 0
    pos_3 = 0

    check_4 = board[1] == board[4] != 0
    pos_4 = 7
    check_5 = board[1] == board[7] != 0
    pos_5 = 4
    check_6 = board[4] == board[7] != 0
    pos_6 = 1

    check_7 = board[2] == board[5] != 0
    pos_7 = 8
    check_8 = board[2] == board[8] != 0
    pos_8 = 5
    check_9 = board[5] == board[8] != 0
    pos_9 = 2

    if check_1 and board[pos_1] != 1 and board[pos_1] != 2:
        return pos_1
    elif check_2 and board[pos_2] != 1 and board[pos_2] != 2:
        return pos_2
    elif check_3 and board[pos_3] != 1 and board[pos_3] != 2:
        return pos_3

    elif check_4 and board[pos_4] != 1 and board[pos_4] != 2:
        return pos_4
    elif check_5 and board[pos_5] != 1 and board[pos_5] != 2:
        return pos_5
    elif check_6 and board[pos_6] != 1 and board[pos_6] != 2:
        return pos_6

    elif check_7 and board[pos_7] != 1 and board[pos_7] != 2:
        return pos_7
    elif check_8 and board[pos_8] != 1 and board[pos_8] != 2:
        return pos_8
    elif check_9 and board[pos_9] != 1 and board[pos_9] != 2:
        return pos_9

    return

def check_diagonals_bot():
    check_1 = board[0] == board[4] != 0
    pos_1 = 8
    check_2 = board[0] == board[8] != 0
    pos_2 = 4
    check_3 = board[4] == board[8] != 0
    pos_3 = 0

    check_4 = board[2] == board[4] != 0
    pos_4 = 6
    check_5 = board[2] == board[6] != 0
    pos_5 = 4
    check_6 = board[4] == board[6] != 0
    pos_6 = 2

    if check_1 and board[pos_1] != 1 and board[pos_1] != 2:
        return pos_1
    elif check_2 and board[pos_2] != 1 and board[pos_2] != 2:
        return pos_2
    elif check_3 and board[pos_3] != 1 and board[pos_3] != 2:
        return pos_3

    elif check_4 and board[pos_4] != 1 and board[pos_4] != 2:
        return pos_4
    elif check_5 and board[pos_5] != 1 and board[pos_5] != 2:
        return pos_5
    elif check_6 and board[pos_6] != 1 and board[pos_6] != 2:
        return pos_6
    return

# function to declare a1, a2, a3, etc
def declare(position):
    dic = {"a1": 0,
           "a2": 1,
           "a3": 2,
           "b1": 3,
           "b2": 4,
           "b3": 5,
           "c1": 6,
           "c2": 7,
           "c3": 8,
           }
    if position in dic:
        position = dic[position]
    else:
        return False
    return position

    display_board()


# picks a random name for the bot from a list
def picking_name():
    names = ["Miguel", "Diablo", "Tom", "Olaf", "Peter", "Sansa", "Diezel Ky", "Kal-El", "Satchel", "Buddy Bear",
             "Saint Lazslo"]
    return names[random.randint(0, len(names) - 1)]



if __name__ == '__main__':
    game()