""" A module containing a car and Frame calss
    A car class encapsuates vehicle information in the the dataset
    A frame represents a frame in the dataset, which is composed of a bunch of cars"""

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    WHITE = '\033[37m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Car():
    def __init__(self, id, width, length, type, x_value, y_value):
        self.id = id
        self.width = width
        self.length = length
        self.type = type
        self.x_value = x_value
        self.y_value = y_value

    def get_id(self):
        return self.id

    def get_width(self):
        return self.width

    def get_length(self):
        return self.length

    def get_type(self):
        return self.type

    def get_x_value(self):
        return self.x_value

    def get_y_value(self):
        return self.y_value

    def __str__(self):
        result = Colors.OKGREEN + 'ID ' + Colors.WHITE + str(self.get_id()) + '\n'
        result += Colors.OKGREEN + 'Width ' + Colors.WHITE + str(self.get_width()) + '\n'
        result += Colors.OKGREEN + 'Length ' + Colors.WHITE + str(self.get_length()) + '\n'
        result += Colors.OKGREEN + 'Type ' + '\n' + Colors.WHITE + str(self.get_type()) + '\n'
        result += Colors.OKGREEN + 'x value ' + '\n' + Colors.WHITE + str(self.get_x_value() )+ '\n'
        result += Colors.OKGREEN + 'y value ' + '\n' + Colors.WHITE + str(self.get_y_value()) + '\n'
        return result

class Frame():
    def __init__(self, cars):
        self.cars = cars

    def get_cars(self):
        return self.cars


