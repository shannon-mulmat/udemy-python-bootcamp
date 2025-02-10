"""
Project Description:
- Create the classic game of Pong

Completed: 2/10/2025
"""
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

LEFT_X = -350
RIGHT_X = 350

screen = Screen()
screen.title("Pong")
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)
screen.tracer(0)

scoreboard = Scoreboard()
left_paddle = Paddle(LEFT_X)
right_paddle = Paddle(RIGHT_X)
ball = Ball()

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top or bottom wall, bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle, bounce
    if ((ball.distance(right_paddle) < 50 and ball.xcor() > 320) or
            (ball.distance(left_paddle) < 50 and ball.xcor() < -320)):
        ball.bounce_x()

    # Detect miss on right, give point to left player
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    # Detect miss on left, give point to right player
    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()

screen.exitonclick()
