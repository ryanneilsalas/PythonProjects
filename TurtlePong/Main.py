from turtle import Screen
from Paddle import paddle
from Ball import ball
from Scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(850, 550)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)
ball = ball()
paddle = paddle()
scoreboard = Scoreboard()
screen.update()


screen.onkeypress(paddle.up1, "w")
screen.onkeypress(paddle.down1, "s")
screen.onkeypress(paddle.up2, "i")
screen.onkeypress(paddle.down2, "k")
screen.listen()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    ball.ball_move()
    if ball.ycor() > 250 or ball.ycor() < -250:
        ball.bounce_y()
    if (ball.distance(paddle.number_paddle[0]) < 30 and ball.xcor() < -350 or
            ball.distance(paddle.number_paddle[1]) < 30 and ball.xcor() > 350):
        ball.bounce_x()

    if ball.xcor() > 430:
        ball.reset_position()
        scoreboard.r_scores()

    if ball.xcor() < -440:
        ball.reset_position()
        scoreboard.l_scores()

screen.exitonclick()

