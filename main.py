# IMPORTS
from turtle import Screen
import time
from frog import Frog
from level import Level
from traffic import Traffic
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

# Initialize Traffic
traffic = Traffic()
# # Listen for key events to invoke methods to change direction
screen.listen()
screen.onkey(frog.up_move, "Up")
screen.onkey(frog.down_move, "Down")
screen.onkey(frog.right_move, "Right")
screen.onkey(frog.left_move, "Left")

# Initialize Game
game_on = True

while game_on:
    screen.update()
    time.sleep(0.2)
    # Create cars randomly on screen to make traffic and have it move automatically
    traffic.create_car()
    traffic.auto_move()
    # Detect if frog hits any cars
    for each_car in traffic.traffic:
        if frog.distance(each_car) < 20:
            game_on = False
            level.game_over()
    if frog.ycor() > 230:
        level.increase_level()
        level.write_level()
        frog.reset_position()
        traffic.increase_speed()
# Screen exit on click
screen.exitonclick()