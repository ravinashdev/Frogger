# IMPORTS
from turtle import Screen
import time
from frog import Frog
from lane import Lane
from level import Level
from traffic import Traffic
from lane import Lane
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

# Initialize Lanes
lane = Lane(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
# # Listen for key events to invoke methods to change direction
screen.listen()
screen.onkey(frog.up_move, "Up")
screen.onkey(frog.down_move, "Down")
screen.onkey(frog.right_move, "Right")
screen.onkey(frog.left_move, "Left")

# Initialize Game
game_on = True
# Set initial sleep time to increase speed as levels increase
default_sleep_time = 0.1
while game_on:
    screen.update()
    time.sleep(default_sleep_time)
    # Create cars randomly on screen to make traffic and have it move automatically
    traffic.create_car()
    traffic.auto_move()
    # Detect if frog hits any cars
    for each_car in traffic.traffic:
        if frog.distance(each_car) < 20:
            game_on = False
            level.game_over()
    # When frog passes the finish line (250 px threshold)
    # 1) Increase the level by +1
    # 2) Write to screen
    # 3) Reset frog to initial starting position using the reset_position method
    # 4) Set a new default_sleep_time by dividing it by 1.1 and setting it to the new default_sleep_time
    if frog.ycor() > 250:
        level.increase_level()
        level.write_level()
        frog.reset_position()
        default_sleep_time = (default_sleep_time/1.5)
# Screen exit on click
screen.exitonclick()