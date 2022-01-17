from ctypes import alignment
from turtle import Turtle

ALIGNMENT = "center"
B_FONT = ("Courier", 80, "bold")
N_FONT = ("Courier", 80, "normal")
S_B_FONT = ("Courier", 50, "bold")
S_N_FONT = ("Courier", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self,b_with = True) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        if b_with:
            self.update_scoreboard()
        
    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()
    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,180)
        self.write(self.l_score , align=ALIGNMENT , font=B_FONT)
        self.goto(100,180)
        self.write(self.r_score , align=ALIGNMENT , font=B_FONT)
        


    def draw_middle_line(self):
        self.pensize(5)
        self.goto(0,300)
        self.setheading(270)
        self.pendown()
        count = 1
        while self.ycor() > -300:
            if count % 2 == 0:
                self.penup()
            else:
                self.pendown()
            self.forward(20)
            count += 1
        self.penup()
            

    def game_over(self):
        self.goto(20,-50)
        if self.l_score > self.r_score:
            self.write("Game Over!\nLeft Wins!", align=ALIGNMENT, font=S_B_FONT)
        else:
            self.write("Game Over!\nRight Wins!", align=ALIGNMENT, font=S_B_FONT)