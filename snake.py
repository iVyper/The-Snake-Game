"""
Snake Module

This module defines the Snake class, which manages the snake's behavior including movement,
growth, and direction control.
"""

from turtle import Turtle

# Constants for snake initialization and movement.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial positions for the snake's segments.
MOVE_DISTANCE = 20  # Distance each segment moves per step.

# Direction constants in degrees.
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    """
    Represents the snake in the game.

    The snake is composed of multiple turtle segments that follow each other to create a moving snake.
    """

    def __init__(self):
        self.snake_body = []  # List that holds all segments of the snake.
        self.create_snake()  # Initialize the snake with default segments.
        self.head = self.snake_body[0]  # The head of the snake for movement and collision detection.

    def create_snake(self):
        """
        Creates the initial snake by adding segments at predefined starting positions.
        """
        for position in STARTING_POSITIONS:
            self.add_body_part(position)

    def add_body_part(self, position):
        """
        Adds a new segment to the snake at the given position.

        Args:
            position (tuple): The (x, y) coordinates where the new segment will be placed.
        """
        snake_body_part = Turtle(shape="square")
        snake_body_part.color("white")
        snake_body_part.penup()
        snake_body_part.goto(position)
        self.snake_body.append(snake_body_part)

    def extend(self):
        """
        Extends the snake by adding a new segment to its tail.
        """
        # Add a segment at the position of the last segment.
        self.add_body_part(self.snake_body[-1].position())

    def move(self):
        """
        Moves the snake forward by moving each segment to the position of the segment ahead of it.
        The head then moves forward by a fixed distance.
        """
        # Move each segment from tail to head.
        for body_part in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[body_part - 1].xcor()
            new_y = self.snake_body[body_part - 1].ycor()
            self.snake_body[body_part].goto(new_x, new_y)
        # Move the head forward.
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Changes the snake's direction to up if it's not currently moving down.
        """
        if self.head.heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        """
        Changes the snake's direction to down if it's not currently moving up.
        """
        if self.head.heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def left(self):
        """
        Changes the snake's direction to left if it's not currently moving right.
        """
        if self.head.heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        """
        Changes the snake's direction to right if it's not currently moving left.
        """
        if self.head.heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)
