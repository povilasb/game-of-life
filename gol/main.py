from copy import deepcopy
from typing import List, Tuple
import time

from . import ui
import gol


Matrix = List[List[int]]


def make_beacon():
    return gol.make_grid((4, 4), (4, 5), (5, 5), (5, 4),
                         (6, 6), (6, 7), (7, 7), (7, 6))


def make_tetramino():
    return gol.make_grid((10, 10), (11, 10), (12, 10), (11, 9))


def make_pentomino():
    return gol.make_grid((20, 20), (21, 20), (20, 21), (19, 21), (20, 22))


def make_matrix(width: int, height: int) -> Matrix:
    return [[0 for _ in range(width)] for _ in range(height)]


def matrix_to_str(matrix: Matrix) -> str:
    lines = [' '.join(['o' if cell else ' ' for cell in row]) \
             for row in matrix]
    return '\n'.join(lines)



def main():
    grid = gol.crop_grid(make_tetramino(), *ui.size())
    matrix = make_matrix(*ui.size())
    for x, y in grid:
        matrix[y][x] = 1
    ui.show(matrix_to_str(matrix))

    while True:
        time.sleep(0.75)
        grid = gol.crop_grid(gol.next_generation(grid), *ui.size())
        matrix = make_matrix(*ui.size())
        for x, y in grid:
            matrix[y][x] = 1
        ui.show(matrix_to_str(matrix))


if __name__ == '__main__':
    main()
