from turtle import Turtle
"""
width = 20
height = 100
x_pos = 350
y_pos = 0
up or down => 20px
"""

class Paddle(Turtle):
    def __init__(self,pos=(0,0)) -> None:
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1) # width and length initialy 20px
        self.penup()
        self.goto(pos)
            

    def move_up(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        if y_cor < 250:
            self.goto(x_cor,y_cor+20)
    def move_down(self):
        x_cor = self.xcor()
        y_cor = self.ycor()
        if y_cor > -250:
            self.goto(x_cor,y_cor-20)
        
