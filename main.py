from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)

    # Detect collision with the wall
    if ball.ycor() >= 285 or ball.ycor() <= -285:
        ball.rebound_y()

    # Detect collision with the right paddle
    if ball.xcor() >= 320 and ball.distance(r_paddle) <= 50:
        ball.rebound_x()

    # Detect collision with the left paddle
    if ball.xcor() <= -320 and ball.distance(l_paddle) <= 50:
        ball.rebound_x()

    # When the right player misses
    if ball.xcor() >= 380:
        ball.reset_position()
        scoreboard.l_point()

    # When the left player misses
    elif ball.xcor() <= -380:
        ball.reset_position()
        scoreboard.r_point()

    ball.move(ball.position())
    screen.update()

screen.exitonclick()
