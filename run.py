
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
            print("%d|%s|" % (row_number, "|".join(row)))# from https://youtu.be/tF1WRCrd_HQ
            row_number += 1

    def build_fleet(self):
        """
        Takes one of each craft and asks for start point
        and direction. Builds full craft when looking at length
        and returns list
        """
        fleet = []
        taken_coords = []
        craft_obj = [
        #Need to fill in craft details from craft class
        ]
        for i in range(self.number_of_craft):
            if self.auto_place:
                #Create random setup
                random_start = (random.randint(0, 9), random.randint(0, 9))
                rand_direction = random.choice(["r", "d"])
                craft_inst = craft_obj[i](random_start, rand_direction, (random_start))

            else: 
                #manual setup
                self.print_board()
                start_point = input(
                    f"Commander {self.owner} where shall we place the {craft_obj[i].name}?\n"
                    f"It is {craft_obj[i].length} long."
                    "\nPlease enter your coordinates (e.g C4)\n"
                ).strip(" ")
                #checks coord input is valid and creates craft
                start_point = self.coord_valid(start_point)
                direction = self.direction_input()
                craft_inst = craft_obj[i](start_point, direction, (start_point))
            
            self.build_craft(self.auto, craft_inst, taken_coords)
            taken_coords.append(craft_inst.coordinates)

            self.manual_position(craft_inst, self.auto_place)

            fleet.append(craft_inst)
        if self.auto_place:
            if self.owner != "Computer":
                self.print_board()
        return fleet

    def build_craft(self, auto_placement, craft, taken_coords):
        """
        Builds craft in selected direction and lets User know if 
        space is taken. 
        """
        selected_placement = True

        while selected_placement:
            temp_craft = []
            temp_craft.append(craft.start_point)
            #checks which axis start point of craft is and adds 1
            for i in range(1, craft.length):
                if craft.direction == "d" or craft.direction == "down":
                    next_space = (craft.start_point[0] + i, craft.start_point[1])
                    add_idx = 0
            
                elif craft.direction == "r" or craft.direction == "right":
                    next_space = (craft.start_point[0], craft.start_point[1] + 1)
                    add_idx = 1

            taken_space = self.is_space_taken(ship, taken_coords, next_space)
            #check for craft leaving baord and asks for new start point if needs to
            if craft.start_point[add_idx] + \
                    (craft.length - 1) > 9:

                if auto_placement:
                    craft.start_point = (random.randint(0, 9), random.randint(0, 9))
                    craft.direction = random.choice(["r", "d"])
                    break
                else:
                    print("Would place craft out of bounds")
                    craft.start_point = input(
                        "Pick a different start coordinate for "
                        f"your {craft.name}. \nPlease enter row then column "
                        "e.g 1A: \n").strip(" ")
                    craft.start_point = self.coord_valid(craft.start_point)
                    craft.direction = self.direction_input()
                    break
            #If next space is not taken then add to temp list, check length
            #and if match then return to coords
            elif not taken_space:
                temp_craft.append(next_space)
                if len(temp_craft) == craft.length:
                    craft.coordinates = temp_craft
                    selected_placement = False
                    return craft.coordinates

            #check remainder of spaces and if any taken will ask for new coords
            else:
                if auto_placement:
                    craft.start_point = (random.randint(0, 9), random.randint(0, 9))
                    craft.direction = random.choice(["r", "d"]) 
                    break
                elif not auto_placement:
                    print("You already placed a craft there Commander")
                    craft.start_point = input(
                        "Pick a different start coordinate for "
                        f"your {craft.name}. \nPlease enter row then column "
                        "e.g 1A: \n").strip(" ")
                    craft.start_point = self.coord_valid(craft.start_point)
                    craft.direction = self.direction_input()
                    break
        return craft.coordinates                 

    def direction_input(self):
        """
        Ask user for direction to place craft. Only down or right as 
        full compass is illogical in this instance. Loops until valid
        inout given. 
        """
        invalid_input = True
        while invalid_input:
            craft.direction = input(
                "Which direction would you want the craft to face?\n"
                "To the (r)ight or (d)own: \n"
            ).lower().strip(" ")
            if craft.direction == "right" or craft.direction == "r":
                invalid_input = False
                return "right"
            elif craft.direction == "down" or craft.direction == "d":
                invalid_input = False
                return "down"
            else:
                print(
                    "I need a valid direction.\n"
                    'Please input "r", "d", "right" or "down":')

    @staticmethod
    def is_space_taken(craft, taken_space, next_space):
        """
        Check for taken space before ship can be placed
        """
        for list in taken_space:
            for _ in list:
                if next_space in list:
                    return True
                elif craft.start_point in list:
                    return True

    def fleet_coords(self):
        """
        Makes dict of fleet coordinates with the craft id
        """
        craft_record = {}
        for i in range(self.fleet_size):
            craft_record.update(
                dict(zip(self.fleet[i].coordinates, self.fleet[i].id_list)))
        return craft_record

    def manual_position(self, craft, auto_placement=False):
        """
        Prints board of chosen ship locations for manual placement
        """
        if self.owner != "Computer":
            for i in range(craft.length):
                self.board[craft.coordinates[i][0]][craft.coordinates[i][1]] = craft.id_list[i]
            if not auto_placement:
                if self.owner != "Computer":
                    self.print_board()

    def check_shot(self, guess):
        """
        Checks guess from fleet dictionary, 
        calls method to update damage of craft
        """
        result = self.fleet_map
        result = result.get(guess)
        craft = None
        if result:
            for i in range(5):
                craft = self.fleet[i]
                if result is self.fleet[i].id_list[0]:
                    self.update_damage(craft)
                    return True
        else:
            return False

    def update_damage():
        pass

    def update_board():
        pass

    def craft_remain():
        pass

    def is_fleet_destroyed():
        pass


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