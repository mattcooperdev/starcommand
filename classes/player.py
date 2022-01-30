import random
from .board import Board
from .helpers import InputHelper, ClearDisplayHelper

class Player(InputHelper, ClearDisplayHelper):
    """
    Creates player object, chooses craft setup, takes a shot
    and creates board object for the Player
    """

    def __init__(self, name):
        self.name = name
        if self.name == "Computer":
            self.board = Board(name)
        else:
            auto_place = self.quick_start()
            self.board = Board(name, auto_place)
        self.guesses = []

    @staticmethod
    def quick_start():
      """
      Asks player if they want manual or auto setup of craft
      """
      invalid_input = True
      while invalid_input:
            setup_type = input(
              "How would you like to setup your craft?\n"
              "(Q)uickly or (M)anually?\n").lower().strip(" ")
            if setup_type == "quick" or setup_type == "q":
                invalid_input = False
                return True
            elif setup_type == "manual" or setup_type == "m":
                invalid_input = False
                return False
            else:
                print(
                    f"I do not understand Commander\n"
                    "Please type a valid input: \n")

    def take_shot(self):
        """
        Takes guess coordinates randomly or by input
        and returns the guess
        """
        valid_guess = False
        while not valid_guess:
            if self.name == "Computer":
                guess_coord = (random.randint(0, 9), random.randint(0, 9))
                previous_guess = guess_coord in self.guesses
                if previous_guess:
                    continue

                self.guesses.append(guess_coord)
                valid_guess = True
            else:
                guess_coord = input(
                    f"Commander {self.name}, what are your coordinates? \n"
                    "Enter row then column e.g. 5,4: \n").strip(" ")

                guess_coord = self.coord_valid(guess_coord)
                previous_guess = guess_coord in self.guesses

                if previous_guess:
                    print(
                        "Commander you have already fired there..."
                    )
                    continue
                else:
                    self.board.print_board()
                    self.guesses.append(guess_coord)
                    valid_guess = True
        return guess_coord

    def player_turn(self, opponent):
        """
        User guess and then relevant board is updated
        """
        print(f"{self.name}'s turn")
        guess = self.take_shot()
        guess_hit_check = opponent.board.check_shot(guess)
        #update board
        self.board.update_board(guess, guess_hit_check, opponent)
        if self.name != "Computer":
            self.board.print_board()

        else:
            opponent.board.print_board()

