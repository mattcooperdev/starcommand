class Craft:
    """
    Creates properties of class that are shared
    by the subclasses to initialise a craft object
    """

    def __init__(self, start_point, direction, coordinates):
        self.start_point = start_point
        self.direction = direction
        self.coordinates = coordinates
        self.damaged_tiles = []
        self.is_destroyed = False


class AsteroidDodger(Craft):
    name = "Asteroid Dodger"
    length = 5
    id_list = ["A"] * length


class Blaster(Craft):
    name = "Blaster Ship"
    length = 4
    id_list = ["B"] * length


class CometKiller(Craft):
    name = "Comet Killer"
    length = 3
    id_list = ["C"] * length


class StarChaser(Craft):
    name = "Star Chaser"
    length = 3
    id_list = ["S"] * length


class Destroyer(Craft):
    name = "Destroyer"
    length = 2
    id_list = ["D"] * length
