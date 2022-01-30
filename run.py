
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import time
import pprint

class Board: 
    board_size = 10
    fleet_size = 5

    def __init__(self, owner, auto_place=True):
        self.owner = owner
        self.auto_place = auto_place
        self.board = self.build_board()
        self.guess_board = self.build_guess_board()
        self.fleet = self.build_fleet()
        self.fleet_map = self.fleet_coords()

    def build_board(self):
        self.board = [] #creates empty list to store ships
        for row in range(self.board_size):
            self.board.append([])
            for _ in range(self.board_size):
                self.board[row].append(".")
        return self.board

    def build_guess_board(self):
        self.guess_board = [] #creates empty list to store player guess
        for row in range(self.board_size):
            self.guess_board.append([])
            for _ in range(self.board_size):
                self.guess_board[row].append(".")
        return self.guess_board

    def print_board(self):
        """
        Prints out both User and Guess board with headers
        """
        self.clear_terminal()
        print(f"{self.owner}'s Board")
        print("  A B C D E F G H I J")
        print("  +-+-+-+-+-+-+-+-+-+")
        row_number = 1
        for row in board:
            print("%d|%s|" % (row_number, "|".join(row)))
            row_number += 1


# SHIP_LENGTH = [2,3,3,4,5]
# PLAYER_BOARD = [[" "] * 8 for i in range(8)]
# PLAYER_GUESS_BOARD = [[" "] * 8 for i in range(8)]
# COMP_BOARD = [[" "] * 8 for i in range(8)]
# COMP_GUESS_BOARD = [[" "] * 8 for i in range(8)]
# NUMBERS_TO_LETTERS = {
#     'A':0, 
#     'B':1, 
#     'C':2, 
#     'D':3, 
#     'E':4, 
#     'F':5, 
#     'G':6, 
#     'H':7
#     }



# def place_ships(board):
#     #loop through length of ships
#     for ship_l in SHIP_LENGTH:
#         #loop until ship fits and doesn't overlap
#         while True:
#             if board == COMP_BOARD:
#                 orientation, row, column = random.choice(["H", "V"]), random.randint(0,7), random.randint(0,7)
#                 if check_ship_fit(ship_l, row, column, orientation):
#                     #check if ship overlaps
#                     if overlap(board, row, column, orientation, ship_l) == False:
#                         #place ship
#                         if orientation == "H":
#                             for i in range int((column, column + ship_l)-1):
#                                 board[row][i] = "X"
#                         else:
#                             for j in range int((row, row + ship_l)-1):
#                                 range -= 1
#                                 board[column][i] = "X"
#                         break
#             else:
#                 place_ships = True
#                 print('Place the ship with a length of ' + str(ship_l))
#                 row, column, orientation = player_input(place_ships)
#                 if check_ship_fit(ship_l, row, column, orientation):
#                     #check if ship overlaps
#                         if ship_overlaps(board, row, column, orientation, ship_l) == False:
#                             #place ship
#                             if orientation == "H":
#                                 for i in range(column, column + ship_l):
#                                     board[row][i] = "X"
#                             else:
#                                 for i in range(row, row + ship_l):
#                                     board[i][column] = "X"
#                             print_board(PLAYER_BOARD)
#                             break 

# def check_ship_fit(SHIP_LENGTH, row, column, orientation):
#     if orientation == "H":
#         if row + SHIP_LENGTH > 8:
#             return False
#         else:
#             return True
#     else:
#         if column + SHIP_LENGTH > 8:
#             return False
#         else:
#             return True

# def overlap(board, row, column, orientation, ship_l):
#     if orientation == "H":
#         for i in range(row, row + ship_l):
#             if board[row][i] == "X":
#                 return True
#     else:
#         for i in range(column, column + ship_l):
#             if board[column][i] == "X":
#                 return True
#     return False

# def player_input(place_ships):
#     if place_ships == True:
#         while True:
#             try:
#                 orientation = input("Would you like your craft to be placed (H)orizontally or (V)ertically?: ").upper()
#                 if orientation == "H" or orientation == "V":
#                     break
#             except TypeError:
#                 print('I did not understand your input. Please enter H or V.')
#         while True:
#             try:
#                 row = input("Which row would you like to place your craft? ")
#                 if row in '12345678':
#                     row = int(row) - 1
#                     break
#             except ValueError:
#                 print('I need a number between 1-8: ')
#         while True:
#             try:
#                 column = input('Now which column would you like to place your craft between A-H: ').upper()
#                 if column in 'ABCDEFGH':
#                     column = NUMBERS_TO_LETTERS[column]
#                     break
#             except KeyError:
#                 print('Commander I need a letter between A-H: ')
#         return row, column, orientation
#     else:
#         while True:
#             try:
#                 row = input("Which row would you like to place your craft? ")
#                 if row in '12345678':
#                     row = int(row) - 1
#                     break
#             except ValueError:
#                 print('I need a number between 1-8: ')
#         while True:
#             try:
#                 column = input('Now which column would you like to place your craft between A-H: ').upper()
#                 if column in 'ABCDEFGH':
#                     column = NUMBERS_TO_LETTERS[column]
#                     break
#             except KeyError:
#                 print('Commander I need a letter between A-H: ')
#         return row, column


# def hit_count():
#     count = 0
#     for row in board:
#         for column in row:
#             if column == "X":
#                 count += 1
#     return count

# def turn(board):
#     if board == PLAYER_GUESS_BOARD:
#         row, column = player_input(PLAYER_GUESS_BOARD)
#         #check if already guessed
#         if board[row][column] == "-": 
#             turn(board)
#         #check if already hit
#         elif board[row][column] == "X":
#             turn(board)
#         #check comp board for hit or miss
#         elif COMP_BOARD[row][column] == "X":
#             board[row][column] = "X"
#         else:
#             board[row][column] = "-"
#     else:
#         #random comp turn for valid hit or miss
#         row, column = random.randint(0, 7), random.randint(0, 7)
#         if board == PLAYER_GUESS_BOARD:
#             row, column = user_input(PLAYER_GUESS_BOARD)
#         if board[row][column] == "-":
#             turn(board)
#         elif board[row][column] == "X":
#             turn(board)
#         elif COMP_BOARD[row][column] == "X":
#             board[row][column] = "X"
#         else:
#             board[row][column] = "-"

# place_ships(COMP_BOARD)
# print_board(COMP_BOARD)
# print_board(PLAYER_BOARD)
# place_ships(PLAYER_BOARD)

# while True:
    #player turn
    # while True:
    #     print('Please give a location to strike')
    #     print_board(PLAYER_GUESS_BOARD)
    #     turn(PLAYER_GUESS_BOARD)
    #     break
    # if hit_count(PLAYER_GUESS_BOARD) == 17:
    #     print("You win!")
    #     break
    # #comp turn
    # while True:
    #     turn(COMP_GUESS_BOARD)
    #     break
    # print_board(COMP_GUESS_BOARD)
    # if hit_count(COMP_GUESS_BOARD) == 17:
    #     print("All of the fleet have been destroyed ")
    #     break

