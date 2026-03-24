from turtle import Turtle
# Frog starting position as a constant
INITIAL_POSITION = (0, -280)
DEFAULT_HEADING = 90
DEFAULT_SHAPE = "turtle"
DEFAULT_MOVE_DISTANCE = 20

class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(DEFAULT_SHAPE)
        self.penup()
        self.setheading(DEFAULT_HEADING)
        self.setposition(INITIAL_POSITION)
    # Frog can. move in any 2D direction
    def up_move(self):
        new_y_coordinate = self.ycor() + DEFAULT_MOVE_DISTANCE
        self.setposition(self.xcor(), new_y_coordinate)
    def down_move(self):
        new_y_coordinate = self.ycor() - DEFAULT_MOVE_DISTANCE
        self.setposition(self.xcor(), new_y_coordinate)
    def right_move(self):
        new_x_coordinate = self.xcor() + DEFAULT_MOVE_DISTANCE
        self.setposition(new_x_coordinate, self.ycor())
    def left_move(self):
        new_x_coordinate = self.xcor() - DEFAULT_MOVE_DISTANCE
        self.setposition(new_x_coordinate, self.ycor())