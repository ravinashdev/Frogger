from turtle import Turtle
import random
DEFAULT_MOVE_DISTANCE = 20
RANDOM_Y_COORDINATES = []
RANDOM_COLORS = ["red", "green", "blue", "yellow", "cyan", "magenta"]

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()
    def create_car(self):
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(RANDOM_COLORS))
        # set the car heading WEST
        self.setheading(180)
        self.setposition(280, random.randint(-300, 300))
    def auto_move(self):
        self.forward(DEFAULT_MOVE_DISTANCE)