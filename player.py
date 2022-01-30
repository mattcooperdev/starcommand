import random
from .board import Board

class Player():
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
            self.board = Board(name, auto)
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
                    f"I do not understand Commander {name}"
                    "Please type a valid input: \n"
                )
