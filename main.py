import scoreboard
from food import Food

import time
from scoreboard import Scoreboard
from snake import Snake
from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600,height=620)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()
snake = Snake(screen)
scoreboard = Scoreboard()
difficulty = 0.1
snake.create_snake()
food = Food()

screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")



# restart functionality not working at this time
# def restart():
#     global difficulty
#     difficulty = 0.1
#     snake.snake_body = []
#     snake.create_snake()
#     scoreboard.score.clear()
#     food.ate()
#     play_game()
#
#
# screen.onkey(restart, "space")

def play_game():
    global difficulty
    snake.move()

    if snake.collision():
        scoreboard.game_over()
        return

    if snake.snake_body[0].distance(food) <= 20:
        food.ate()
        snake.create()
        scoreboard.increase_score()
        difficulty = max(0.05, difficulty - 0.005)  # Don't go lower than 0.05

    screen.update()
    screen.ontimer(play_game, int(difficulty * 1000))

play_game()

screen.mainloop()

