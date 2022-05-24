from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

R_STARTING_POSITION = [(350, 40), (350, 20), (350, 0), (350, -20), (350, -40)]
L_STARTING_POSITION = [(-350, 40), (-350, 20), (-350, 0), (-350, -20), (-350, -40)]

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(R_STARTING_POSITION)
l_paddle = Paddle(L_STARTING_POSITION)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect paddle collision
    if ball.distance(r_paddle.segment[2]) < 50 and ball.xcor() > 330 or ball.distance(
            l_paddle.segment[2]) < 50 and ball.xcor() < -330:
        ball.bounce_x()

    # Detect out of boundary
    if ball.xcor() > 400:
        scoreboard.l_point()
        time.sleep(0.5)
        ball.reset()

    if ball.xcor() < -400:
        scoreboard.r_point()
        time.sleep(0.5)
        ball.reset()


screen.exitonclick()
