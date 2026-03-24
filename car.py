from turtle import Turtle
import random
DEFAULT_MOVE_DISTANCE = 10
# RANDOM_Y_COORDINATES = [-230, -210, -190, -170, -150, -130, -110, ]
RANDOM_COLORS = ["red", "green", "blue", "yellow", "cyan", "magenta"]
DEFAULT_SHAPE = "square"
DEFAULT_CAR_STARTING_X_COORDINATE = 280
DEFAULT_SET_HEADING = 180

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()
    def create_car(self):
        self.shape(DEFAULT_SHAPE)
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(RANDOM_COLORS))
        # set the car heading WEST
        self.setheading(DEFAULT_SET_HEADING)
        self.setposition(DEFAULT_CAR_STARTING_X_COORDINATE, random.randrange(-230, 230, 40))
    def auto_move(self):
        self.forward(DEFAULT_MOVE_DISTANCE)