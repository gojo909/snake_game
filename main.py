import time
from turtle import Screen, Turtle, Terminator

from food import Food
from scoreboard import Scoreboard
from snake import Snake

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 700  # 600px play field + 50px header strip
DIVIDER_Y = 300
WALL_LIMIT = 280

screen = Screen()
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Divider between the header strip (scoreboard) and the play field.
divider = Turtle()
divider.hideturtle()
divider.color("white")
divider.pensize(2)
divider.penup()
divider.goto(-SCREEN_WIDTH // 2, DIVIDER_Y)
divider.pendown()
divider.goto(SCREEN_WIDTH // 2, DIVIDER_Y)
divider.penup()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

game_is_on = True


def restart():
    global game_is_on
    scoreboard.reset()
    snake.reset()
    game_is_on = True


def quit_game():
    screen.bye()


screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")
screen.onkeypress(restart, "r")
screen.onkeypress(quit_game, "q")

try:
    while True:
        screen.update()
        time.sleep(0.1)

        # After game over the loop keeps running so R / Q keys still work.
        if not game_is_on:
            continue

        snake.move()

        # Eat food: grow the snake and score a point.
        if snake.head.distance(food) < 15:
            food.refresh()
            snake.extend()
            scoreboard.increase_score()

        # Wall collision.
        if (
            abs(snake.head.xcor()) > WALL_LIMIT
            or abs(snake.head.ycor()) > WALL_LIMIT
        ):
            scoreboard.game_over()
            game_is_on = False

        # Tail collision (skip the head itself).
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                scoreboard.game_over()
                game_is_on = False
                break
except Terminator:
    pass
except KeyboardInterrupt:
    pass