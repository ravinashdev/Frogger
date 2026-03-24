from turtle import Turtle
MOVE = False
ALIGN = "center"
FONT = ("Courier", 24, "bold")

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.setposition(-230,250)
    def write_level(self):
        # Write the level on the top left of the screen
        self.write(f"Level:{self.level}", align=ALIGN, font=FONT)
    def increase_level(self):
        # Increase the level every time traffic is passed
        self.level += 1
        # Clear the screen
        self.clear()