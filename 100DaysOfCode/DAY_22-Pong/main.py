from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Setup
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# Objects
p1 = Paddle((350,0))
p2 = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard1 = Scoreboard(False)


# Movement controls
screen.listen()
screen.onkeypress(key="Up",fun=p1.move_up)
screen.onkeypress(key="Down",fun=p1.move_down)
screen.onkeypress(key="w",fun=p2.move_up)
screen.onkeypress(key="W",fun=p2.move_up)
screen.onkeypress(key="s",fun=p2.move_down)
screen.onkeypress(key="S",fun=p2.move_down)


# Middle line
scoreboard1.draw_middle_line()

i_ball_speed = 0.1
ball_speed = i_ball_speed
game_is_on = True
while game_is_on:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bouncey()
    
    
    # Detect collision with paddle
    if (ball.distance(p1) < 50 and ball.xcor() > 320) or (ball.distance(p2) < 50 and ball.xcor() < -320):
        ball.bouncex()
        if ball_speed > 0.04:
            ball_speed -= 0.005

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        ball_speed = i_ball_speed

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        ball_speed = i_ball_speed
    
    if scoreboard.l_score == 5 or scoreboard.r_score == 5:
        scoreboard.game_over()
        scoreboard1.clear()
        game_is_on = False



# Exit
screen.exitonclick()