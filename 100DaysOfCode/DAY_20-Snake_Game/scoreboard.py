from turtle import Turtle
N_FONT = ("Courier", 24, "normal")
B_FONT = ("Courier", 24, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,260)
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