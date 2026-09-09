import random
from turtle import Turtle


class Food(Turtle):
    """A small blue dot that appears at a random grid position."""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280) // 20 * 20
        random_y = random.randint(-280, 280) // 20 * 20
        self.goto(random_x, random_y)