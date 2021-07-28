from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.dy = 10 # tham số để bóng di chuyển
        self.dx = 10
        self.ball_speed = 0.1

    def moving(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def y_bouncing(self):
        self.dy *= -1

    def x_bouncing(self):
        self.dx *= -1
        self.ball_speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.x_bouncing()

