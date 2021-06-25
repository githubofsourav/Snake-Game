from turtle import Screen
from food import Food
import time
from Snake_Class import Snake
from scorecard import Score


screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor("black")
screen.title("Sourav's Snake Game")
# Used to avoid the animations
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    # Used to refresh the screen
    screen.update()
    # Used to delay the animation by 0.2 seconds
    time.sleep(0.1)
    snake.move()

    # Track score
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        score.update()

    # Detect collision with wall
    if snake.segments[0].xcor() > 295 or snake.segments[0].xcor() < -295 or snake.segments[0].ycor() > 230 \
            or snake.segments[0].ycor() < -230:
        game_is_on = False
        score.gameover()

    # Detect collision with body of snake
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False
            score.gameover()

screen.exitonclick()
