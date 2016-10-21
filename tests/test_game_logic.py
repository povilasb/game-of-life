from mock import MagicMock, ANY, call

from game_of_life.main import Board, tick


def describe_tick():
    def it_applies_game_rules_for_every_cell():
        board = Board(2, 2)
        board.copy = MagicMock()

        new_board = tick(board)

        new_board.__setitem__.assert_has_calls(
            [
                call((0, 0), ANY),
                call((1, 0), ANY),
                call((1, 1), ANY),
                call((0, 1), ANY),
            ],
            any_order=True
        )
