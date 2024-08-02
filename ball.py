from turtle import Turtle
import random


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.move_speed = 0.1
        self.x_move = random.choice([15, -15])
        self.y_move = random.choice([10, -10])

    def move(self, position):
        self.goto(position[0] + self.x_move, position[1] + self.y_move)

    def rebound_y(self):
        self.y_move *= -1

    def rebound_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.rebound_x()
        self.rebound_y()
