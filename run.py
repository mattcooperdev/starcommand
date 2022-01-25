
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

SHIP_LENGTH = [2,3,3,4,5]
PLAYER_BOARD = [[" "] * 10 for i in range(10)]
PLAYER_GUESS_BOARD = [[" "] * 10 for i in range(10)]
COMP_BOARD = [[" "] * 10 for i in range(10)]
COMP_GUESS_BOARD = [[" "] * 10 for i in range(10)]
NUMBERS_TO_LETTERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 
'F':5, 'G':6, 'H':7}

def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1

def place_ships(board):
    #loop through ship length list
    for ship_l in SHIP_LENGTH:
        #loop until ship fits and doesn't overlap
        while True:
            if board == COMP_BOARD: #cpu board will just be random
                orientation, row, column = random.choice(["H", "V"]), 
                random.randint(0,7), random.randint(0,7)
                if check_ship_fit(ship_l, row, column, orientation):
                    #check for overlap of ship
                    if overlap(board, row, column, orientation, ship_l) == False:
                        #place ship
                        if orientation == "H":
                            for i in range(column, column + ship_l):
                                board[row][i] = "X" 
                        else:
                            for i in range(row, row + ship_l):
                                board[column][i] = "X"
                        break
        else:
            place_ship = True
            #player guess to place
            #TODO: add ship names 
            print('Place the ship with a length of  ' + str(ship_l))
            row, column, orientation = player_input(place_ship)
            if check_ship_fit(ship_l, row, column, orientation):
               #check for overlap of ship
                    if overlap(board, row, column, orientation, ship_l) == False:
                        #place ship
                        if orientation == "H":
                            for i in range(column, column + ship_l):
                                board[row][i] = "X" 
                        else:
                            for i in range(row, row + ship_l):
                                board[column][i] = "X"
                        print_board(PLAYER_BOARD)
                        break 

def check_ship_fit(SHIP_LENGTH, row, column, orientation):
    if orientation == "H":
        if column + SHIP_LENGTH > 8:
            return False
        else:
            return True
    else:
        if row + SHIP_LENGTH > 8:
            return False
        else:
            return True

def overlap(board, row, column, orientation, ship_l):
    if orientation == "H":
        for i in range(column, column + ship_l):
            if board[row][i] == "X":
                return True
    else:
        for i in range(row, row + ship_l):
            if board[column][i] == "X":
                return True
    return False

def player_input(place_ship):
    if place_ship == True:
        while True:
            try:
                orientation = input("Would you like your craft to be placed (H)orizontally or (V)ertically?: ").upper()
                if orientation == "H" or orientation == "V":
                    break
            except TypeError:
                print('I did not understand your input. Please enter H or V.')
        while True:
            try:
                row = input("Which row would you like to place your craft? ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('I need a number between 1-8: ')
        while True:
            try:
                column = input('Now which column would you like to place your craft between A-H: ').upper()
                if column in 'ABCDEFGH':
                    column = NUMBERS_TO_LETTERS[column]
                    break
            except KeyError:
                print('Commander I need a letter between A-H: ')
        return row, column, orientation
    else:
        while True:
            try:
                row = input("Which row would you like to place your craft? ")
                if row in '12345678':
                    row = int(row) - 1
                    break
            except ValueError:
                print('I need a number between 1-8: ')
        while True:
            try:
                column = input('Now which column would you like to place your craft between A-H: ').upper()
                if column in 'ABCDEFGH':
                    column = NUMBERS_TO_LETTERS[column]
                    break
            except KeyError:
                print('Commander I need a letter between A-H: ')
        return row, column


def hit_count():
    pass

def turn(board):
    pass

# while True:

