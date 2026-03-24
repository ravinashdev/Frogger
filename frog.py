from turtle import Turtle

class Frog(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.setposition(0,-280)
    # Frog can. move in any 2D direction
    def up_move(self):
        new_y_coordinate = self.ycor() + 20
        self.setposition(self.xcor(), new_y_coordinate)
    def down_move(self):
        new_y_coordinate = self.ycor() - 20
        self.setposition(self.xcor(), new_y_coordinate)
    def right_move(self):
        new_x_coordinate = self.xcor() + 20
        self.setposition(new_x_coordinate, self.ycor())
    def left_move(self):
        new_x_coordinate = self.xcor() - 20
        self.setposition(new_x_coordinate, self.ycor())