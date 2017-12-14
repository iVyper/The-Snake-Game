"""
Food Module

This module defines the Food class, which represents the food for the snake.
Each food object is a small turtle graphics circle that randomly appears on the screen.
"""

from turtle import Turtle
import random


class Food(Turtle):
    """
    Represents the food that the snake can eat.

    Inherits from Turtle. Upon initialization, the food is set to appear at a random location.
    """

    def __init__(self):
        super().__init__()
        self.shape("circle")  # Set the shape to circle for a food-like appearance.
        self.penup()  # Prevent drawing when moving.
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)  # Resize the circle to be smaller.
        self.color("yellow")  # Set the food color.
        self.speed("fastest")  # Set the fastest animation speed.
        # Place the food at a random location on the screen.
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        """
        Moves the food to a new random location.

        Called when the snake eats the food, refreshing its position.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
