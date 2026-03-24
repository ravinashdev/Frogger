from turtle import Screen
import time
from frog import Frog

# Initialize Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Frogger")
screen.tracer(0)

# Initialize Frog Character
frog = Frog()

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
    time.sleep(0.1)

# Screen exit on click
screen.exitonclick()