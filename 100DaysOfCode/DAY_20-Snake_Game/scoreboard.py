from turtle import Turtle
import time
N_FONT = ("Courier", 24, "normal")
B_FONT = ("Courier", 24, "bold")
S_FONT = ("Courier", 12, "normal")
COUNT_FONT = ("Courier", 72, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    
    def __init__(self,b_with = True):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        if b_with:
            self.goto(-20,250)
            self.update_scoreboard()
        

    def update_scoreboard(self):
            self.write(f"Score: {self.score}",align=ALIGNMENT,font=N_FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!",align=ALIGNMENT,font=B_FONT)
        
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    
    def speed_borad(self,spd=1):
        self.clear()
        self.goto(210,260)
        self.write(f"Speed: {spd}",align=ALIGNMENT,font=S_FONT)

    def difficulty_board(self,diff="I don't know"):
        self.goto(190,240)
        self.write(f"Difficulty: {diff.capitalize()}",align=ALIGNMENT,font=S_FONT)

    def countdown(self,count=3):
        self.goto(0,-36)
        for i in range(count,0,-1):
            self.write(i,align=ALIGNMENT,font=COUNT_FONT)
            time.sleep(1)
            self.clear()