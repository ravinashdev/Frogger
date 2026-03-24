from turtle import Screen
import time
from typing import List

from frog import Frog
from level import Level
from car import Car

# Initialize Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Frogger")
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
    time.sleep(0.1)
    car = Car()
    traffic.append(car)
    for each_car in traffic:
        each_car.auto_move()

# Screen exit on click
screen.exitonclick()