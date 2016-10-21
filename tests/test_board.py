from hamcrest import assert_that, is_
import pytest

from game_of_life.main import Board


def describe_board():
    def describe__setitem__():
        def it_sets_value_for_cell_using_x_y_notation():
            board = Board(6, 2)
            board[4, 0] = 1

            assert_that(board[4, 0], is_(1))

    def describe__getitem__():
        def describe_when_coords_are_out_of_board_bounds():
            @pytest.mark.parametrize('coords', [
                (-1, 0),
                (0, -1),
                (3, 0),
                (0, 3),
            ])
            def it_returns_0(coords):
                board = Board(2, 2)
                board[0, 0] = 1
                board[1, 0] = 1
                board[0, 1] = 1
                board[1, 0] = 1

                x, y = coords
                value = board[x, y]

                assert_that(value, is_(0))

    def describe_all_coords():
        def it_returns_a_list_of_coordinates_of_all_cells():
            board = Board(3, 2)

            cells = board.all_coords()

            assert_that(cells,
                is_([(0, 0), (1, 0), (2, 0), (0, 1), (1, 1), (2, 1)]))
