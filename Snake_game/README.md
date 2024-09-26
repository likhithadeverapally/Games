# Snake Game

## Description
The **Snake Game** is a classic arcade game developed using Python and the Tkinter library. In this game, you control a snake that grows in length as it eats food. The goal is to collect as much food as possible while avoiding collisions with the snake's own body or the boundaries of the game window.

## How to Play
- Use the **arrow keys** on your keyboard to control the direction of the snake.
  - **Up Arrow**: Move up
  - **Down Arrow**: Move down
  - **Left Arrow**: Move left
  - **Right Arrow**: Move right
- The snake will grow in size after consuming the food.
- The game ends if the snake collides with its own body or the boundaries.

## Features
- Simple and clean interface using **Tkinter**.
- Automatically increasing score as the snake eats food.
- Game over message displayed when the snake collides with itself or the boundaries.
- The game automatically restarts after displaying "Game Over" for 2 seconds.

## Technologies Used
- Python
- Tkinter (for GUI)

## Prerequisites
- **Python 3.x** installed on your machine.
- **Tkinter** library (it comes pre-installed with most Python distributions).
  
If Tkinter is not installed, you can install it using:
```bash
pip install tk
```

## How to Run the Game
1. **Clone or Download** this repository and navigate to the `Snake_game` folder.
2. Run the `snakegame.py` file using Python:
   ```bash
   python snakegame.py
   ```
3. The game window will appear, and you can start playing by using the arrow keys to control the snake.

## Folder Structure
```
Snake_game/
│
├── snakegame.py       # Main Python script for the game
└── README.md          # Instructions and details about the game
```

## Code Explanation
- **Food Class**: Handles the random placement of food on the game canvas.
- **Snake Class**: Controls the snake's body, movement, and size.
- **next_turn()**: Manages the snake's movement, checks for collisions, and updates the score.
- **change_direction()**: Updates the snake's direction based on user input.
- **check_collisions()**: Detects collisions with the snake's body or the boundary walls.
- **game_over()**: Displays the "Game Over" message and stops the game.

## Future Improvements
- Adding difficulty levels where the speed increases as the snake grows.
- Adding sounds and visual effects.
- Implementing a high-score feature to save the top score across sessions.

## License
This project is open-source and free to use. Feel free to modify it for your personal projects.
