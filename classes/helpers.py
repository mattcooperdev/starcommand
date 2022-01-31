import os


class InputHelper():
    """
    Takes coordinate input from User and checks validity.
    Returns valid coordinate or asks for new input
    """
    def coord_valid(self, input):
        valid_input = False
        while not valid_input:
            try:
                if len(input) < 2 or len(input) > 3:
                    raise ValueError
                elif len(input) == 2:
                    input = (tuple(int(i) for i in input))
                    return input

                elif len(input) < 4:
                    if "," in input:
                        input = input.split(",")
                        input = (tuple(int(i) for i in input))
                        return input
                    else:
                        input = self.coord_error()
                        continue
            except ValueError:
                input = self.coord_error()

    @staticmethod
    def coord_error():
        """
        Notifies input is invalid, requests new input
        """
        give_again = input("Your input is not valid.\n"
                           "Please give two numbers for row and column \n"
                           "between 0 and 9\n").strip(" ")
        return give_again


class ClearDisplayHelper():

    # taken from https://www.geeksforgeeks.org/clear-screen-python/
    @staticmethod
    def clear_terminal():
        """"
        Clears the console
        """
        command = 'clear'
        if os.name in (
                'nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)