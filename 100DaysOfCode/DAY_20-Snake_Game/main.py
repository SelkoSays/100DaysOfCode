from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
sleep_time = 0.1
speed_score = 1

# Mode
difficulty = screen.textinput("Difficulty","Type in a level of difficulty. (Easy/Medium/Hard): ").lower()
#difficulty = "medium"

# Window on top
rootwindow = screen.getcanvas().winfo_toplevel()
rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
rootwindow.call('wm', 'attributes', '.', '-topmost', '0')


# Objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()
snake_speed = Scoreboard(False)
snake_difficulty = Scoreboard(False)
count_down = Scoreboard(False)
snake_speed.speed_borad(speed_score)
snake_difficulty.difficulty_board(difficulty)
snake.hideturtle()

count_down.countdown(5)


# Movements
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


# Code
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep_time)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        if difficulty == "hard":
            if sleep_time > 0.04 and scoreboard.score % 2 == 0:
                sleep_time -=0.005
                speed_score += 1
                snake_speed.speed_borad(speed_score)
        elif  difficulty == "medium":
            if sleep_time > 0.05 and scoreboard.score % 4 == 0:
                sleep_time -=0.005
                speed_score += 1
                snake_speed.speed_borad(speed_score)
        else:
            if sleep_time > 0.06 and scoreboard.score % 5 == 0:
                sleep_time -=0.005
                speed_score += 1
                snake_speed.speed_borad(speed_score)

    # Detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    #Detect collision with tail.
    for seg in snake.segments[1::]:
        if snake.head.distance(seg) < 10:
            game_is_on = False
            scoreboard.game_over()


# Exit
screen.exitonclick()