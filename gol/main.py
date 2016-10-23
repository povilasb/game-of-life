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


def main():
    gui = ui.Pygame()

    grid = gol.crop_grid(make_pentomino(), *gui.size())
    matrix = make_matrix(*gui.size())
    for x, y in grid:
        matrix[y][x] = 1

    gui.show(matrix)

    while True:
        time.sleep(0.75)
        grid = gol.crop_grid(gol.next_generation(grid), *gui.size())
        matrix = make_matrix(*gui.size())
        for x, y in grid:
            matrix[y][x] = 1

        gui.show(matrix)


if __name__ == '__main__':
    main()
