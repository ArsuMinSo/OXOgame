from board import Board


def test_board_initialization():
    board = Board()
    assert len(board.available_moves()) == 9


def test_make_move():
    board = Board()
    assert board.make_move(0, 0, "X")
    assert not board.make_move(0, 0, "O")


def test_winner():
    board = Board()
    board.make_move(0, 0, "X")
    board.make_move(0, 1, "X")
    board.make_move(0, 2, "X")
    assert board.is_winner("X")


def test_full_board():
    board = Board()
    moves = [(r, c) for r in range(3) for c in range(3)]
    for i, (r, c) in enumerate(moves):
        board.make_move(r, c, "X" if i % 2 == 0 else "O")
    assert board.is_full()
