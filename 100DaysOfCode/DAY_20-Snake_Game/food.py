from turtle import Turtle, Screen
from random import randint

#"""
FOOD = {"f":"Snake_img/snake_food.gif"}
"""
FOOD = {"f":"Snake_img1/snake_food.gif"}
#"""
F = FOOD["f"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.screen.addshape(F)
        self.shape(F)
        self.penup()
        self.shapesize(stretch_len=0.2,stretch_wid=0.2)
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = randint(-270,270)
        rand_y = randint(-270,240)
        self.goto(rand_x,rand_y)