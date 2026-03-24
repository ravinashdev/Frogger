# IMPORTS
from turtle import Turtle
import random
# CONSTANTS
DEFAULT_MOVE_DISTANCE = 10
RANDOM_COLORS = ["red", "green", "blue", "yellow", "cyan", "magenta"]
DEFAULT_SHAPE = "square"
DEFAULT_CAR_STARTING_X_COORDINATE = 300
DEFAULT_SET_HEADING = 180
DEFAULT_CAR_SPEED = 1

class Traffic:
    def __init__(self):
        self.traffic = []
        self.speed = 1
    def create_car(self):
        # Randomize die throw to only generate a car on a roll of 6 in order to
        # limit the screen with too many cars being generated
        die_throw = random.randint(0, 6)
        if die_throw == 6:
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
    def increase_speed(self):
        new_speed = DEFAULT_CAR_SPEED + 1
        for each_car in self.traffic:
            each_car.speed(new_speed)