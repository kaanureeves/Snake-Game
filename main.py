import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.upKey, "w")
screen.onkey(snake.downKey, "s")
screen.onkey(snake.leftKey, "a")
screen.onkey(snake.rightKey, "d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # collision with food#

    if snake.head.distance(food) < 15:  # snake.segment[0].distance(food)#
        food.set_new_loc()
        scoreboard.update()
        scoreboard.hit()
        snake.extend()

    # collision with walls #

    if (snake.head.xcor() > 290 or snake.head.xcor() < -290
            or snake.head.ycor() > 290 or snake.head.ycor() < -290):
        scoreboard.reset_sb()
        snake.snake_reset()

    # collision with own tail #

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_sb()
            snake.snake_reset()

screen.exitonclick()
