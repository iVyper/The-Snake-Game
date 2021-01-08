"""
Main Module for The Snake Game

This module ties together the game components: Snake, Food, and Scoreboard.
It sets up the game screen, listens for user input, and runs the game loop.
On collisions (with wall or self), the game resets instead of ending.
"""

from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the game screen.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)  # Disable automatic screen updates for manual control.

# Create game components.
snake = Snake()         # The moving snake
food = Food()           # The food pellet
scoreboard = Scoreboard()  # Score display and high score tracking

# Configure keyboard controls for snake direction.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop.
game = True
while game:
    screen.update()     # Manually refresh the screen.
    time.sleep(0.1)     # Control the game speed.

    snake.move()        # Advance the snake forward.

    # --- Food collision check ---
    # If the snake head is close enough to the food, "eat" it:
    if snake.head.distance(food) < 15:
        food.refresh()         # Reposition the food randomly.
        snake.extend()         # Grow the snake by one segment.
        scoreboard.increase_score()  # Increment and display score.

    # --- Wall collision check ---
    # If the head crosses the boundary, reset the game state:
    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        scoreboard.reset()     # Update high score if needed and reset display.
        snake.reset()          # Remove all segments and recreate the snake at start.

    # --- Self-collision check ---
    # If the head runs into any segment of its body, reset:
    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            break  # Exit the loop once reset has occurred

# Keep the window open until the user closes it.
screen.exitonclick()
