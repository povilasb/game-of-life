from functools import reduce
from typing import Set, Tuple, Iterable


Cell = Tuple[int, int]
Grid = Set[Cell]


def make_grid(*cells) -> Grid:
    return set(cells)


def crop_grid(grid: Grid, width: int, height: int) -> Grid:
    return set(filter(lambda cell: cell[0] in range(0, width) and
                                   cell[1] in range(0, height),
                      grid))


def next_generation(grid: Grid) -> Grid:
    return set(
        filter(lambda cell: live_neighbours(grid, cell) in [2, 3], grid)
    ).union(newborns(grid))


def newborns(grid: Grid) -> Iterable[Cell]:
    return filter(
        lambda c: c not in grid and live_neighbours(grid, c) == 3,
        reduce(lambda cells, c: set(cells).union(neighbours(c)), grid, set())
    )


def live_neighbours(grid: Grid, cell: Cell) -> int:
    return len(grid.intersection(neighbours(cell)))


def neighbours(cell: Cell) -> Iterable[Cell]:
    x, y = cell
    adjacent = [(x_, y_) for x_ in range(x - 1, x + 2)
                for y_ in range(y - 1, y + 2)]
    return filter(lambda c: c != cell, adjacent)
