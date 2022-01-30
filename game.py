import pprint
# from getch import pause

class Game:
    """
    Holds main game by calling objects from classes
    """
    def __init__(self):
        self.welcome()

    def welcome(self):


        print("""
                                            
                 / ____| |                                         
                | (___ | |_ __ _ _ __                              
                 \___ \| __/ _` | '__|                             
                ____) | || (_| | |                                
               |_____/ \__\__,_|_|                              _ 
                / ____|                                        | |
                | |     ___  _ __ ___  _ __ ___   __ _ _ __   _| |
               | |    / _ \| '_ ` _ \| '_ ` _ \ / _` | '_ \ / _` |
               | |___| (_) | | | | | | | | | | | (_| | | | | (_| |
                \_____\___/|_| |_| |_|_| |_| |_|\__,_|_| |_|\__,_|                                                      

        """)

        options_menu = True

        while options_menu:
            options = input("Press the 'S' key to play").lower().strip(" ")
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
        print("Let's fight in the stars!!")
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
                print(f"Well done Commander {name}! You defeated"
                        "the alien threat")
                pause("Press any key to go to the main menu")
                self.restart_game(player, computer)
                break

            #checks same for computer win
            computer.player_turn(player)
            play_round = player.board.is_fleet_destroyed()
            if play_round is False: 
                print("Your space fleet has been detroyed!")
                pause("Press any key to go to the main menu")
                self.restart_game(player, computer)
                break

    @staticmethod
    def name_input():
        """
        Get name and check validity
        """
        valid_name = False
        while not valid_name:
            name = input("What is your name Commander?")

            if len(name.strip(" ")) == 0:
                print("I need to take something from you..")
                continue

            elif name.lower() == "computer":
                print("If there is any computer on board I would"
                "not think it was you!"
                "Please select something other than that")
                continue

            name = string.capwords(name)
            print(f"Welcome Commader {name} ")
            return name

