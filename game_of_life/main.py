from copy import deepcopy
from typing import List, Tuple
import time

from . import ui


Matrix = List[List[int]]


class Board:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

        self.matrix = make_matrix(width, height)

    def __getitem__(self, xy: Tuple[int, int]) -> int:
        x, y = xy
        if (x < 0) or (x > self.width - 1) or (y < 0) or (y > self.height - 1):
            return 0
        return self.matrix[y][x]

    def __setitem__(self, xy: Tuple[int, int], value: int) -> None:
        self.matrix[xy[1]][xy[0]] = value

    def neighbours(self, x: int, y: int) -> int:
        return self[x - 1, y - 1] + \
            self[x - 1, y] + \
            self[x - 1, y + 1] + \
            self[x, y - 1] + \
            self[x, y + 1] + \
            self[x + 1, y - 1] + \
            self[x + 1, y] + \
            self[x + 1, y + 1]

    def copy(self):
        clone = Board(self.width, self.height)
        clone.matrix = deepcopy(self.matrix)
        return clone

    def all_coords(self) -> List[Tuple[int, int]]:
        return [(x, y) for y in range(self.height) for x in range(self.width)]

    def __str__(self) -> str:
        lines = [' '.join(['o' if alive else ' ' for alive in row]) \
                 for row in self.matrix]
        return '\n'.join(lines)


def make_beacon_board(width: int, height: int) -> Board:
    board = Board(width, height)
    board[4, 4] = 1
    board[4, 5] = 1
    board[5, 5] = 1
    board[5, 4] = 1

    board[6, 6] = 1
    board[6, 7] = 1
    board[7, 7] = 1
    board[7, 6] = 1

    return board


def make_tetramino_board(width: int, height: int) -> Board:
    board = Board(width, height)
    board[10, 10] = 1
    board[11, 10] = 1
    board[12, 10] = 1
    board[11, 9] = 1
    return board


def make_pentomino_board(width: int, height: int) -> Board:
    board = Board(width, height)
    board[20, 20] = 1
    board[21, 20] = 1
    board[20, 21] = 1
    board[19, 21] = 1
    board[20, 22] = 1
    return board


def tick(board: Board) -> Board:
    new_board = board.copy()

    for x_y in board.all_coords():
        new_board[x_y] = apply_rules_with(board.neighbours(*x_y),
                                          board[x_y])

    return new_board


def apply_rules_with(n: int, current_value: int) -> None:
    if n < 2 or n > 3:
        return 0

    if n == 3:
        return 1

    return current_value


def make_matrix(width: int, height: int) -> Matrix:
    return [[0 for _ in range(width)] for _ in range(height)]


def main():
    board = make_pentomino_board(*ui.size())
    ui.show(board)

    while True:
        time.sleep(0.75)
        board = tick(board)
        ui.show(board)


if __name__ == '__main__':
    main()
