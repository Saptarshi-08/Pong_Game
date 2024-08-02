from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, cor_tup):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.resizemode("user")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.goto(cor_tup)

    def move_up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
