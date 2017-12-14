"""
Main Module for The Snake Game

This module ties together the game components: Snake, Food, and Scoreboard.
It sets up the game screen, listens for user input, and runs the game loop until a collision occurs.
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
screen.tracer(0)  # Turn off automatic animation to control screen updates manually.

# Create game components.
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up keyboard bindings.
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop.
game = True
while game:
    screen.update()     # Refresh the screen.
    time.sleep(0.1)     # Pause the loop to control game speed.

    snake.move()        # Move the snake forward.

    # Check for collision with the food.
    if snake.head.distance(food) < 15:
        food.refresh()         # Move food to a new random location.
        snake.extend()         # Add a new segment to the snake.
        scoreboard.increase_score()  # Update the score.

    # Check for collision with the wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or \
       snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game = False
        scoreboard.game_over()

    # Check for collision with the snake's body.
    for body_part in snake.snake_body[1:]:
        if snake.head.distance(body_part) < 10:
            game = False
            scoreboard.game_over()

# Keep the game window open until clicked.
screen.exitonclick()
