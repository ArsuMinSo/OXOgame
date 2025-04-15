from player import Player
from board import Board


class AIPlayer(Player):
    """
    Represents an AI player using the minimax algorithm.
    """
    def __init__(self, symbol: str) -> None:
        super().__init__(symbol)

    def minimax(self, board: Board, depth: int, is_maximizing: bool) -> int:
        """
        Implements the minimax algorithm to determine the best move.
        :param board: The game board instance.
        :param depth: The current depth of recursion.
        :param is_maximizing: Boolean indicating of maximizing or minimizing.
        :return: The best score for the current state.
        """
        opponent = "O" if self.symbol == "X" else "X"
        if board.is_winner(self.symbol):
            return 1
        elif board.is_winner(opponent):
            return -1
        elif board.is_full():
            return 0

        if is_maximizing:
            best_score = -float("inf")
            for row, col in board.available_moves():
                board.make_move(row, col, self.symbol)
                score = self.minimax(board, depth + 1, False)
                board.undo_move(row, col)
                best_score = max(score, best_score)
            return best_score
        else:
            best_score = float("inf")
            for row, col in board.available_moves():
                board.make_move(row, col, opponent)
                score = self.minimax(board, depth + 1, True)
                board.undo_move(row, col)
                best_score = min(score, best_score)
            return best_score

    def get_move(self, board: Board) -> tuple[int, int]:
        """
        Determines the best move for the AI player.
        :param board: The game board instance.
        :return: A tuple (row, column) representing the best move.
        """
        best_score = -float("inf")
        best_move = None
        for row, col in board.available_moves():
            board.make_move(row, col, self.symbol)
            score = self.minimax(board, 0, False)
            board.undo_move(row, col)
            if score > best_score:
                best_score = score
                best_move = (row, col)
        return best_move
