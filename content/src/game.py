from board import Board
from player import Player
from aiplayer import AIPlayer


class Game:
    """
    Manages the flow of the Tic-Tac-Toe game.
    """
    def __init__(self) -> None:
        """
        Initializes the game with a board, human player, and AI player.
        """
        self.board: Board = Board()
        self.player: Player = Player("O")
        self.ai: AIPlayer = AIPlayer("X")

    def play(self) -> None:
        """
        Runs the game loop until there is a winner or a draw.
        """
        self.board.print_board()
        while True:
            row, col = self.player.get_move(self.board)
            self.board.make_move(row, col, self.player.symbol)
            self.board.print_board()
            if self.board.is_winner(self.player.symbol):
                print("Congratulations, you won.")
                break
            if self.board.is_full():
                print("Its draw.")
                break

            print("Computer thinking")
            row, col = self.ai.get_move(self.board)
            self.board.make_move(row, col, self.ai.symbol)
            self.board.print_board()
            if self.board.is_winner(self.ai.symbol):
                print("Computer won!")
                break
            if self.board.is_full():
                print("Its draw.")
                break
