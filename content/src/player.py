from board import Board


class Player:
    """
    Represents a human player in the Tic-Tac-Toe game.
    """
    def __init__(self, symbol: str) -> None:
        """
        Initializes the player with a given symbol ('X' or 'O').
        :param symbol: The player's symbol.
        """
        self.symbol: str = symbol

    def get_move(self, board: Board) -> tuple[int, int]:
        """
        Prompts the player to enter a move.
        :param board: The game board instance.
        :return: A tuple (row, column) representing the player's move.
        """
        while True:
            try:
                move = int(input("Enter a number between 1 and 9: ")) - 1
                row, col = move // 3, move % 3
                if (row, col) in board.available_moves():
                    return row, col
                print("Invalid move, try again.")
            except ValueError:
                print("Enter a number between 1 and 9.")
