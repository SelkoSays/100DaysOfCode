from turtle import Turtle, Screen
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.screen.addshape("Snake_img\\snake_food.gif")
        self.shape("Snake_img\\snake_food.gif")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = randint(-280,280)
        rand_y = randint(-280,280)
        self.goto(rand_x,rand_y)