"""
Scoreboard Module

This module defines the Scoreboard class which handles displaying the current score on the screen.
It also shows a game over message when the game ends.
"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    """
    Represents the scoreboard that keeps track of the player's score.

    Inherits from Turtle. It displays the current score at the top of the screen and shows a game over message when needed.
    """

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()  # Hide the turtle shape.
        self.color('white')  # Score text color.
        self.penup()  # Don't draw lines when moving.
        self.goto(0, 270)  # Position the score near the top of the screen.
        self.show_score()  # Display the initial score.

    def increase_score(self):
        """
        Increases the current score by one and updates the display.
        """
        self.score += 1
        self.show_score()

    def show_score(self):
        """
        Clears the previous score and writes the new score on the screen.
        """
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Displays the game over message in the center of the screen.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
