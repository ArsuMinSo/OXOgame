class Board:
    """
    Represents the Tic-Tac-Toe board and provides methods for game logic.
    """
    def __init__(self) -> None:
        """
        Initializes the board as a 3x3 grid filled with "-".
        """
        self.board: list[list[str]] = [
            ["-" for _ in range(3)]
            for _ in range(3)
        ]

    def print_board(self) -> None:
        """
        Prints the current state of the board with numbered positions.
        """
        for row in range(3):
            for col in range(3):
                if self.board[row][col] in "XO":
                    print(self.board[row][col], end=" ")
                else:
                    print(row * 3 + col + 1, end=" ")
            print("")

    def is_full(self) -> bool:
        """
        Checks if the board is full (i.e., no empty spaces left).
        :return: True if the board is full, False otherwise.
        """
        return all(cell in "XO" for row in self.board for cell in row)

    def is_winner(self, symbol: str) -> bool:
        """
        Checks if a given player has won the game.
        :param symbol: The player's symbol ('X' or 'O').
        :return: True if the player has won, False otherwise.
        """
        for i in range(3):
            if all(self.board[i][j] == symbol for j in range(3)) or \
               all(self.board[j][i] == symbol for j in range(3)):
                return True
        return (
            all(self.board[i][i] == symbol for i in range(3)) or
            all(self.board[i][2 - i] == symbol for i in range(3))
        )

    def available_moves(self) -> list[tuple[int, int]]:
        """
        Returns a list of available moves on the board.
        :return: List of tuples representing available (row, column) positions.
        """
        available = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "-":
                    available.append((row, col))

        return available

    def make_move(self, row: int, col: int, symbol: str) -> bool:
        """
        Places a move on the board if the position is available.
        :param row: Row index (0-2).
        :param col: Column index (0-2).
        :param symbol: The player's symbol ('X' or 'O').
        :return: True if the move was successful, False otherwise.
        """
        if self.board[row][col] == "-":
            self.board[row][col] = symbol
            return True
        return False

    def undo_move(self, row: int, col: int) -> None:
        """
        Reverts a move at the given position.
        :param row: Row index (0-2).
        :param col: Column index (0-2).
        """
        self.board[row][col] = "-"
