# Tic Tac Toe Game with AI

This project is a Python implementation of a **Tic Tac Toe game**, featuring both human and AI players. It includes various types of players, such as a random move generator, a "genius" AI using the Minimax algorithm, and a human player. The game is interactive and allows for a variety of match configurations.

---

## Features
- **Interactive Gameplay**: Play against an AI or another human.
- **Three Player Types**:
  - `HumanPlayer`: Allows human input for moves.
  - `RandomComputerPlayer`: Makes random valid moves.
  - `GeniusComputerPlayer`: Uses the Minimax algorithm to play optimally.
- **Visual Board Display**: See the current board state during the game.
- **Winner Detection**: Determines the winner or declares a tie.
- **Simulation Mode**: Simulate multiple games to analyze AI performance.

---

## How to Run
1. Clone or download the repository.
2. Ensure you have Python 3.x installed.
## How to Play
- The board is represented as a 3x3 grid of numbers:

 ```| 0 | 1 | 2 |```
 ```| 3 | 4 | 5 |```
 ```| 6 | 7 | 8 |```


- When prompted, enter the number corresponding to the square where you want to make your move.

  ## Example Gameplay
# Start the game.
Choose your players (e.g., Human vs. GeniusComputerPlayer).
Play turns until there's a winner or the game ends in a tie.


Example Output:
``` | 0 | 1 | 2 |```
 ```| 3 | 4 | 5 |```
 ```| 6 | 7 | 8 |```

X's turn. Input move (0-8): 4
X makes a move to square 4
``` |  |  |  |```
 ```|  | x |  |```
 ```|  |  |  |```


## Future Enhancements
- Add a graphical user interface (GUI) for better user interaction.
- Allow for adjustable AI difficulty levels.
- Implement a multiplayer mode over the network.
