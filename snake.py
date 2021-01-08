"""
Snake Module

This module defines the Snake class, which manages the snake’s segments,
movement, growth, and resetting upon collision.
"""

from turtle import Turtle

# Configuration constants.
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # Initial segment locations.
MOVE_DISTANCE = 20  # Distance the head moves each step.

# Heading angles.
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake:
    """
    Represents the player-controlled snake. Handles its segments, movement,
    growth, and resetting when collisions occur.
    """
    def __init__(self):
        self.snake_body = []        # List to hold the turtle segments.
        self.create_snake()         # Populate initial segments.
        self.head = self.snake_body[0]  # Reference to the first segment as the head.

    def create_snake(self):
        """
        Build the initial snake by placing segments at starting positions.
        """
        for position in STARTING_POSITIONS:
            self.add_body_part(position)

    def add_body_part(self, position):
        """
        Create a new square segment at the given position and add it to the body list.

        Args:
            position (tuple): (x, y) coordinates for the new segment.
        """
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.snake_body.append(segment)

    def extend(self):
        """
        Add a new segment to the end of the snake at the last segment’s position.
        """
        self.add_body_part(self.snake_body[-1].position())

    def move(self):
        """
        Update all segments to follow the one in front, then move the head forward.
        """
        # Move each body segment to the position of the one ahead of it.
        for idx in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[idx - 1].xcor()
            new_y = self.snake_body[idx - 1].ycor()
            self.snake_body[idx].goto(new_x, new_y)
        # Advance the head segment.
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """
        Turn the snake’s head north unless it’s currently moving south.
        """
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """
        Turn the snake’s head south unless it’s currently moving north.
        """
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """
        Turn the snake’s head west unless it’s currently moving east.
        """
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """
        Turn the snake’s head east unless it’s currently moving west.
        """
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset(self):
        """
        Remove all existing segments off-screen, clear the body list,
        and recreate the snake in its starting configuration.
        """
        for segment in self.snake_body:
            segment.goto(1000, 1000)  # Move off-screen
        self.snake_body.clear()       # Clear segment list
        self.create_snake()           # Rebuild initial snake
        self.head = self.snake_body[0]  # Reset head reference
