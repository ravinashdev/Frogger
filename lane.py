# IMPORTS
from turtle import Turtle
# CONSTANTS
DEFAULT_SET_HEADING = 180
DEFAULT_PEN_SIZE = 10

class Lane(Turtle):
    def __init__(self, default_screen_width, default_screen_height  ):
        super().__init__()
        self.screen_width = default_screen_width
        self.screen_height = default_screen_height
        self.speed(0)
        self.setheading(DEFAULT_SET_HEADING)
        self.hideturtle()
        self.pensize(DEFAULT_PEN_SIZE)
        self.penup()
        self.top_line()
        self.penup()
        self.bottom_line()
    def top_line(self):
        top_y_coordinate = (self.screen_height - 100)/2
        top_x_coordinate = self.screen_width/2
        self.setposition(top_x_coordinate, top_y_coordinate)
        for i in range(0, self.screen_width,100):
            self.pendown()
            self.forward(50)
            self.penup()
            self.forward(50)
    def bottom_line(self):
        bottom_y_coordinate = -1*(self.screen_height - 100)/2
        bottom_x_coordinate = self.screen_width/2
        self.setposition(bottom_x_coordinate, bottom_y_coordinate)
        for i in range(0, self.screen_width,100):
            self.pendown()
            self.forward(50)
            self.penup()
            self.forward(50)