# IMPORTS
from turtle import Turtle
import random
# CONSTANTS
DEFAULT_MOVE_DISTANCE = 10
# RANDOM_Y_COORDINATES = [-230, -210, -190, -170, -150, -130, -110, ]
RANDOM_COLORS = ["red", "green", "blue", "yellow", "cyan", "magenta"]
DEFAULT_SHAPE = "square"
DEFAULT_CAR_STARTING_X_COORDINATE = 300
DEFAULT_SET_HEADING = 180

class Traffic:
    def __init__(self):
        self.traffic = []
    def create_car(self):
        new_car = Turtle()
        new_car.shape(DEFAULT_SHAPE)
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(RANDOM_COLORS))
        # set the car heading WEST
        new_car.setheading(DEFAULT_SET_HEADING)
        new_car.setposition(DEFAULT_CAR_STARTING_X_COORDINATE, random.randrange(-230, 230, 40))
        self.traffic.append(new_car)
    def auto_move(self):
        for each_car in self.traffic:
            each_car.forward(DEFAULT_MOVE_DISTANCE)
