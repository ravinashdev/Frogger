# IMPORTS
from turtle import Turtle
# CONSTANTS
MOVE = False
ALIGN = "center"
FONT = ("Courier", 24, "bold")
DEFAULT_LEVEL_POSITION = (-230, 260)

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setposition(DEFAULT_LEVEL_POSITION)
    def write_level(self):
        # Write the level on the top left of the screen
        self.write(f"LEVEL:{self.level}", align=ALIGN, font=FONT)
    def increase_level(self):
        # Increase the level every time traffic is passed
        self.level += 1
        # Clear the screen
        self.clear()
    def game_over(self):
        # Write Game Over when frog gets hit by traffic
        self.clear()
        message = f"Game Over!"
        self.setposition(0,0)
        self.write(message, MOVE, ALIGN, font=("Courier", 32, "bold"))