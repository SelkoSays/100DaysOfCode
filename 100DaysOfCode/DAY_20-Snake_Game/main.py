from turtle import Turtle, Screen
from snake import Snake
import time

# Setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# Objects
snake = Snake()

# Code
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()



# Exit
screen.exitonclick()