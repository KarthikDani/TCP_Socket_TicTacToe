# Tic Tac Toe Multiplayer - Terminal based Multiplayer Game

Welcome to the Tic Tac Toe multiplayer game implemented in Python! This game allows two players to play the classic Tic Tac Toe game using the terminal. It's a fun and engaging way to challenge your friends and test your strategic skills.

## Gameplay Video

[Watch the Gameplay Video](https://youtu.be/vtFu-hCKIs8?si=rU0mlWHTKssmv9oG)


## Table of Contents
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Features](#features)
- [Server](#server)
- [Client](#client)
- [Contributing](#contributing)
- [License](#license)

## Installation

Before you can start playing, you need to set up the game on your local machine. Follow these steps to get started:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/KarthikDani/TCP_Socket_TicTacToe.git
   ```

2. **Navigate to the Project Directory**:

   ```bash
   cd TCP_Socket_TicTacToe
   ```

3. **Run the Server**:

   Open a terminal window and run the server script:

   ```bash
   python3 server.py
   ```

4. **Run the Client**:

   Open another terminal window and run the client script:

   ```bash
   python3 client.py
   ```

Now you're ready to play Tic Tac Toe with your friend!

## How to Play

Tic Tac Toe is a two-player game, where one player is "X" and the other is "O." Here's how to play:

1. **Game Board**:

   The game board is a 3x3 grid, and each cell is numbered from 1 to 9. Players will take turns to choose a cell where they want to place their symbol.

   ```bash
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```

2. **Player's Turn**:

   - The game starts with "O." The "O" player enters a number (1 to 9) to place their symbol in the corresponding cell.
   - The "X" player goes next, and the game continues in this alternating fashion until one player wins or the game ends in a draw.

3. **Winning**:

   The first player to get three of their symbols in a row, column, or diagonal wins the game. The game will display a message indicating the winner.

4. **Draw**:

   If all the cells are filled, and no player has won, the game ends in a draw.

## Features

- **Multiplayer**: Play against a friend in real-time.
- **Terminal-Based**: Enjoy the classic game in your terminal.
- **Win Detection**: The game automatically detects and announces the winner.
- **Draw Detection**: Recognizes when the game ends in a draw.
- **Illegal Move Handling**: Prevents players from making illegal moves.

## Server

The `server.py` script sets up the game server, allowing two players to connect and play. It manages the game board, checks for a win or draw, and handles incoming moves from clients.

## Client

The `client.py` script represents a player in the game. It connects to the server, takes player input, and sends moves to the server. The client also displays the current state of the game board, so players can see the game's progress.

## Contributing

Contributions are welcome! If you have ideas for improvements or want to fix a bug, please fork the repository, create a new branch, make your changes, and submit a pull request. Your contributions will help make this game even better.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.

Enjoy playing Tic Tac Toe with your friends, and have fun coding! If you have any questions or encounter issues, feel free to reach out to the project's maintainers.
