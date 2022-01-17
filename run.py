
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('starcommand')

usernames = SHEET.worksheet('usernames')                           

user_data = usernames.get_all_values()

print(user_data)

SHIP_LENGTH = [2,3,3,4,5]
PLAYER_BOARD = [[" "] * 10 for i in range(10)]
PLAYER_GUESS_BOARD = [[" "] * 10 for i in range(10)]
COMP_BOARD = [[" "] * 10 for i in range(10)]
COMP_GUESS_BOARD = [[" "] * 10 for i in range(10)]
NUMBERS_TO_LETTERS = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 
'I':8, 'J':9}

def print_board(board):
    print("  A B C D E F G H I J")
    print("  +-+-+-+-+-+-+-+-+-+")
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
                orientation, row, column = random.choice(["H", "V"]), random.randint(0,9), random.randint(0,9)
                if check_ship_fit(ship_l, row, column, orientation)

def check_ship_fit():
    pass

def overlap():
    pass

def player_input():
    pass

def hit_count():
    pass

def turn(board):
    pass

# while True:

