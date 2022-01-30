import random
import time
from .craft import AsteroidDodger, Blaster, CometKiller, StarChaser, Destroyer
from .helpers import InputHelper, ClearDisplayHelper

class Board(InputHelper, ClearDisplayHelper): 
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

    def update_damage(self, craft):
        """
        Runs through ship damage and 
        updates when necessary
        """
        craft.damaged_tiles.append(True)
        if len(craft.damaged_tiles) == craft.length:
            self.craft_remaining()

    def update_board(self, guess, result, opponent):
        """
        Updates board with hit or miss guess
        """
        if result is False:
            #miss
            self.guess_board[guess[0]][guess[1]] = "~"
            opponent.guess_board[guess[0]][guess[1]] = "~"
            #only show user view
            if self.owner != "Computer":
                self.print_board()
            else:
                opponent.board.print_board()
            print(f"{self.owner} missed!")
        
        else:
            #hit
            self.guess_board[guess[0]][guess[1]] = "X"
            opponent.guess_board[guess[0]][guess[1]] = "X"
            #only show user view
            if self.owner != "Computer":
                self.print_board()
            else:
                opponent.board.print_board()
            print(f"{self.owner} made a perfect Hit!")
            

    def craft_remaining(self):
        """
        Reduce fleet by 1
        """
        self.number_of_craft -= 1
        return self.number_of_craft

    def is_fleet_destroyed(self):
        if self.number_of_craft == 0:
            return False
        else:
            return True