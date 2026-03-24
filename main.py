from turtle import Screen
import time
from frog import Frog
from level import Level
from car import Car
# CONSTANTS
DEFAULT_SCREEN_WIDTH = 600
DEFAULT_SCREEN_HEIGHT = 600
DEFAULT_SCREEN_COLOR = "white"
DEFAULT_SCREEN_TITLE = "Frogger"
# Initialize Screen Object
screen = Screen()
screen.setup(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
screen.bgcolor(DEFAULT_SCREEN_COLOR)
screen.title(DEFAULT_SCREEN_TITLE)
screen.tracer(0)

# Initialize Frog Character
frog = Frog()

# Initialize Level Board
level = Level()
level.write_level()

# # Listen for key events to invoke methods to change direction
screen.listen()
screen.onkey(frog.up_move, "Up")
screen.onkey(frog.down_move, "Down")
screen.onkey(frog.right_move, "Right")
screen.onkey(frog.left_move, "Left")

# Initialize Game
game_on = True
# Create Traffic List
traffic = []
while game_on:
    screen.update()
    time.sleep(0.2)
    car = Car()
    traffic.append(car)
    for each_car in traffic:
        each_car.auto_move()

# Screen exit on click
screen.exitonclick()