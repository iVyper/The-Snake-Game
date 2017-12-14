# The Snake Game
The Snake Game is a classic arcade-style game reimagined using Python's turtle graphics. In this project, you control a snake that moves across the screen, eating food to grow longer. Each time the snake consumes a piece of food, the score increases and a new food item appears at a random location. The game ends when the snake collides with a wall or with its own body. The project is organized into several modules to handle different aspects of the game: food appearance, snake behavior, score tracking, and the main game loop.

## Features
- **Dynamic Food Generation:**
The food appears as a small yellow circle placed at a random position within the game boundaries.
When the snake eats the food (i.e., when the snake's head comes close enough to the food), it is refreshed to a new random location.

- **Snake Mechanics:**
The snake is made up of multiple segments that follow the head.
It moves continuously on the screen, and you can control its direction using the arrow keys.
Eating food causes the snake to extend by adding a new segment at its tail.

- **Scoreboard Display:**
The current score is tracked and displayed at the top of the screen.
A "GAME OVER" message is displayed when the snake collides with the wall or itself.

- **Collision Detection:**
The game monitors for collisions with the boundaries of the screen.
It also checks for collisions with the snake's own body, ending the game upon such an event.

- **Smooth Animation:**
The screen updates at controlled intervals, creating smooth and responsive gameplay.

## Modules Overview
- `food.py`:
Defines the Food class which inherits from Turtle. It creates a food object that appears as a small yellow circle at a random position and can be refreshed when consumed by the snake.

- `snake.py`:
Contains the Snake class that manages the snake’s movement, growth, and directional controls. The snake is made up of several Turtle segments that follow each other to simulate slithering.

- `scoreboard.py`:
Implements the Scoreboard class which extends Turtle to display the player’s current score at the top of the screen and shows a game over message once the game ends.

- `main.py`:
Serves as the entry point for the game. It sets up the game screen, instantiates objects for the snake, food, and scoreboard, and contains the main game loop. It also listens for keyboard events to control the snake’s movement.


## Installation

### Prerequisites

- **Python 3.x:** Ensure that Python 3 is installed on your system. You can download it from [Python's offical website](python.org).

- **Turtle Module:**
The turtle module is included with the standard Python distribution.

- **Time Module and Random Module:**
These are part of Python's standard library and are used for controlling game speed and generating random positions/movements respectively.

### How to Run

1. **Download the Code:** Clone the repository or make sure you have all the following files in the same directory:
   - main.py

   - food.py

   - snake.py

   - scoreboard.py

2. **Open Terminal/Command Prompt:** Navigate to the directory containing the file.

3. **Run the program:** Execute the following command:

    ```bash
    python3 main.py
    ```

4. **Play the Game:**
   - Use the arrow keys (Up, Down, Left, Right) to control the snake. 
   - Try to eat the food to increase your score and grow the snake. 
   - Avoid hitting the walls or colliding with your own body to keep playing. 
   - When a collision occurs, the game will end, and a game over message with your final score will be displayed.
 


## Demo
![The Snake Game Demo](screenshots/demo.gif)

## License

This project is open-source and available under the [MIT License](https://choosealicense.com/licenses/mit/).


## Authors

- Ivis Perdomo [@ivyper](https://www.github.com/ivyper)

