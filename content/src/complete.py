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
                    print(self.board[row][col])
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
        Prompts the player to enter a move (1-9) corresponding to the available cells.
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


class AIPlayer(Player):
    """
    Represents an AI player using the minimax algorithm to decide the best move.
    """
    def __init__(self, symbol: str) -> None:
        """
        Initializes the AI player with the given symbol ('X' or 'O') and uses the minimax algorithm for decision-making.
        :param symbol: The AI player's symbol.
        """
        super().__init__(symbol)

    def minimax(self, board: Board, depth: int, is_maximizing: bool) -> int:
        """
        Implements the minimax algorithm to determine the best move.
        :param board: The game board instance.
        :param depth: The current depth of recursion.
        :param is_maximizing: Boolean indicating of maximizing or minimizing.
        :return: The score for the current state (1 for win, -1 for loss, 0 for draw).
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
