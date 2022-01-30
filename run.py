
# Write your code to expect a terminal of 80 characters wide and 24 rows high
from classes.game import Game
from classes.helpers import ClearDisplayHelper

if __name__ == '__main__':
    ClearDisplayHelper.clear_terminal()
    game = Game()

# PLAYER_BOARD = [[" "] * 8 for i in range(8)]

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
