Module complete
===============

Classes
-------

`AIPlayer(symbol: str)`
:   Represents an AI player using the minimax algorithm to decide the best move.
    
    Initializes the AI player with the given symbol ('X' or 'O') and uses the minimax algorithm for decision-making.
    :param symbol: The AI player's symbol.

    ### Ancestors (in MRO)

    * complete.Player

    ### Methods

    `get_move(self, board: complete.Board) ‑> tuple[int, int]`
    :   Determines the best move for the AI player.
        :param board: The game board instance.
        :return: A tuple (row, column) representing the best move.

    `minimax(self, board: complete.Board, depth: int, is_maximizing: bool) ‑> int`
    :   Implements the minimax algorithm to determine the best move.
        :param board: The game board instance.
        :param depth: The current depth of recursion.
        :param is_maximizing: Boolean indicating of maximizing or minimizing.
        :return: The score for the current state (1 for win, -1 for loss, 0 for draw).

`Board()`
:   Represents the Tic-Tac-Toe board and provides methods for game logic.
    
    Initializes the board as a 3x3 grid filled with "-".

    ### Methods

    `available_moves(self) ‑> list[tuple[int, int]]`
    :   Returns a list of available moves on the board.
        :return: List of tuples representing available (row, column) positions.

    `is_full(self) ‑> bool`
    :   Checks if the board is full (i.e., no empty spaces left).
        :return: True if the board is full, False otherwise.

    `is_winner(self, symbol: str) ‑> bool`
    :   Checks if a given player has won the game.
        :param symbol: The player's symbol ('X' or 'O').
        :return: True if the player has won, False otherwise.

    `make_move(self, row: int, col: int, symbol: str) ‑> bool`
    :   Places a move on the board if the position is available.
        :param row: Row index (0-2).
        :param col: Column index (0-2).
        :param symbol: The player's symbol ('X' or 'O').
        :return: True if the move was successful, False otherwise.

    `print_board(self) ‑> None`
    :   Prints the current state of the board with numbered positions.

    `undo_move(self, row: int, col: int) ‑> None`
    :   Reverts a move at the given position.
        :param row: Row index (0-2).
        :param col: Column index (0-2).

`Game()`
:   Manages the flow of the Tic-Tac-Toe game.
    
    Initializes the game with a board, human player, and AI player.

    ### Methods

    `play(self) ‑> None`
    :   Runs the game loop until there is a winner or a draw.

`Player(symbol: str)`
:   Represents a human player in the Tic-Tac-Toe game.
    
    Initializes the player with a given symbol ('X' or 'O').
    :param symbol: The player's symbol.

    ### Descendants

    * complete.AIPlayer

    ### Methods

    `get_move(self, board: complete.Board) ‑> tuple[int, int]`
    :   Prompts the player to enter a move (1-9) corresponding to the available cells.
        :param board: The game board instance.
        :return: A tuple (row, column) representing the player's move.