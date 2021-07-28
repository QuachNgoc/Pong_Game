from turtle import Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import ScoreBoard
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)  # when tracer is 0, means no animations

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_on = True

while game_on:
    sleep(ball.ball_speed)
    screen.update()  # upadate the animations
    ball.moving()

    # check y_border
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bouncing()

    # Detect collision with r_paddle
    if ball.distance(r_paddle) < 50 and (ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.x_bouncing()

    if ball.xcor() > 380:
        ball.reset()
        score.l_score_increased()
        if score.l_score == 3:
            player = "Player 2"
            score.win_the_game(player)
            game_on = False

    if ball.xcor() < -380:
        ball.reset()
        score.r_score_increased()
        if score.r_score == 3:
            player = "Player 1"
            score.win_the_game(player)
            game_on = False



screen.exitonclick()
