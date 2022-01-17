from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)

    def bouncey(self):
        self.y_move *= -1
    def bouncex(self):
        self.x_move *= -1
    def reset_position(self):
        self.goto(0,0)
        self.bouncex()
