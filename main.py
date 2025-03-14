from turtle import Screen, Turtle
import time
from snake_class import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


#create snake
snake = Snake()
food = Food()

#add keybaord controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

scoreboard = Scoreboard()
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


#detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.update_score()

#detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
#detect collision with tail
#if head collides with any segment in the tail:
    #triggger game over

    for segment in snake.segments[:1]:
        if snake.head.distance(segment):
            game_is_on = False
            scoreboard.game_over()










screen.exitonclick()