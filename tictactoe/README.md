# Tic-Tac-Toe Game

## Description
The **Tic-Tac-Toe Game** is a simple, two-player game built using HTML, CSS, and JavaScript. Players take turns marking spaces on a 3x3 grid, aiming to get three of their symbols (either 'X' or 'O') in a row horizontally, vertically, or diagonally to win the game.

## How to Play
- The game is designed for **two players**.
- One player marks the grid spaces with **X** and the other with **O**.
- Players take turns clicking on the grid to mark their spots.
- The game ends when:
  - One player gets three symbols in a row (horizontal, vertical, or diagonal).
  - All grid spaces are filled with no winner (resulting in a draw).
- The game resets automatically after a win or a draw, allowing the players to play again.

## Features
- Interactive user interface using **HTML** and **CSS**.
- Smooth gameplay using **JavaScript** for the game logic.
- Displays the winner or announces a draw at the end of the game.
- Option to restart the game after each round.
  
## Technologies Used
- **HTML**: For the structure of the game.
- **CSS**: For styling the game board and layout.
- **JavaScript**: For implementing the game logic and player interactions.

## How to Run the Game
1. **Clone or Download** this repository and navigate to the `TicTacToe_game` folder.
2. Open the `index.html` file in any modern web browser (such as Chrome, Firefox, Edge).
3. The Tic-Tac-Toe game will load, and two players can begin playing by clicking on the grid.

## Folder Structure
```
TicTacToe_game/
│
├── index.html          # Main HTML file for the game
├── style.css           # CSS file for styling the game
├── script.js           # JavaScript file for game logic
└── README.md           # Instructions and details about the game
```

## Code Explanation
- **HTML (index.html)**: 
  - Sets up the 3x3 grid using `<div>` elements for each cell.
  - Includes a section to display the game's current status (e.g., whose turn it is, or if someone has won).
  
- **CSS (style.css)**:
  - Styles the grid and cells to create a visually appealing layout.
  - Adds colors and spacing for clarity and visual feedback when players select a spot.

- **JavaScript (script.js)**:
  - Handles the game logic, including:
    - Switching turns between the two players.
    - Detecting a win or draw by checking for three matching symbols in a row.
    - Resetting the game board for a new round.
  
## Game Logic
1. **Player Turns**: Players alternate turns after selecting an available space on the grid.
2. **Win Detection**: The game checks all possible win conditions after each move (rows, columns, and diagonals).
3. **Draw Condition**: If the grid is full and no player has won, the game declares a draw.
4. **Game Reset**: After a win or draw, the board resets, allowing players to start a new game.

## Future Improvements
- Adding a feature to track and display the number of wins for each player.
- Implementing an AI opponent for single-player mode.
- Enhancing the UI with animations or sound effects for a more interactive experience.

## License
This project is open-source and free to use. You are welcome to modify and adapt it for your own purposes.
