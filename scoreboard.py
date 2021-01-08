"""
Scoreboard Module

This module defines the Scoreboard class which tracks and displays:
- Current score
- High score (persisted in 'high_score.txt')
It also resets scores when the snake collides.
"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    """
    Displays the score and high score at the top of the screen.
    Can reset itself when the game restarts, updating the high score file if needed.
    """
    def __init__(self):
        super().__init__()
        self.score = 0
        # Load high score from file, defaulting to 0 if file is missing or invalid.
        with open("high_score.txt", mode="r") as f:
            self.high_score = int(f.read())
        self.hideturtle()
        self.color('white')
        self.penup()
        self.goto(0, 270)  # Position the text at the top center.
        self.show_score()

    def increase_score(self):
        """
        Increment the current score by one and update the on-screen display.
        """
        self.score += 1
        self.show_score()

    def show_score(self):
        """
        Clear previous text and write the updated current score and high score.
        """
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """
        Reset the current score to zero. If the current score exceeds the high score,
        update the high score in memory and write it to the file.
        Finally, refresh the display to show Score: 0 and the (new) high score.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.show_score()
