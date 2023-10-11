from turtle import Turtle, Screen
import time
from paddles import Paddle
from ball import Ball
from score import Score
from line import Line


screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

line = Line()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
x = 0.05
game_is_on = True
while game_is_on:
    time.sleep(x)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()
        x *= 0.9

    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
        x = 0.05

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()
        x = 0.05

screen.exitonclick()
