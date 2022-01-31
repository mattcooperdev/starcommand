import string
from time import sleep
from .player import Player
from.helpers import ClearDisplayHelper

class Game(ClearDisplayHelper):
    """
    Holds main game by calling objects from classes
    """
    def __init__(self):
        self.welcome()

    def welcome(self):


        print("""\u001b[32;1m
          _____ _                         
         / ____| |                                       
        | (___ | |_ __ _ _ __                              
         \___ \| __/ _` | '__|                             
         ____) | || (_| | |                                
        |_____/ \__\__,_|_|                              _ 
         / ____|                                        | |
        | |     ___  _ __ ___  _ __ ___   __ _ _ __   _ | |
        | |    / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |
        | |___| (_) | | | | | | | | | | | (_| | | | | (_| |
         \_____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|                                                      

        """)

        options_menu = True

        while options_menu:
            options = input("          Press the 'S' key to play: \n").lower().strip(" ")
            if options == "s":
                self.clear_terminal()
                self.set_players()
            else:
                print(" Your input was not recognised.")



    def set_players(self):
        """
        Asks for player name and creates objects
        """
        user = self.name_input()
        user = Player(user)
        computer_player = Player("Computer")
        print("\nLet's fight in the stars!!\n")

        self.take_turns(user, computer_player)

    def take_turns(self, player, computer):
        """
        Loops through turns of player and cpu marking relevant board
        until all ships sunk
        """
        play_round = True
        while play_round:

            player.player_turn(computer)
            play_round = computer.board.is_fleet_destroyed()
            #checks boolean, prints and exit
            if play_round is False:
                print(f"Well done Commander! \n"
                       "You defeated the alien threat")
                sleep(2)
                print("Press any key to go to the main menu")
                self.restart_game(player, computer)
                break

            #checks same for computer win
            computer.player_turn(player)
            play_round = player.board.is_fleet_destroyed()
            if play_round is False: 
                print("Your space fleet has been detroyed!\n")
                sleep(2)
                print("Press any key to go to the main menu")
                self.restart_game(player, computer)
                break

    @staticmethod
    def name_input():
        """
        Get name and check validity
        """
        valid_name = False
        while not valid_name:
            name = input("What is your name Commander? \n")

            if len(name.strip(" ")) == 0:
                print("I need to take something from you..\n")
                continue

            elif name.lower() == "computer":
                print("\nIf there is any computer on board \n"
                      "I would not think it was you!\n")
                sleep(2)
                print("Please select something other than that\n")
                continue

            name = string.capwords(name)
            print(f"\nWelcome Commander {name} \n")
            return name

    def restart_game(self, player1, player2):
        """
        Deletes all instances of player obj, ships and board.
        Takes user back to welcome
        """
        del(player1)
        del(player2)
        self.clear_terminal()
        self.welcome()