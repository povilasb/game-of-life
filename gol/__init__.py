from functools import reduce
from typing import Tuple, Iterable


Cell = Tuple[int, int]


class Grid:
    def __init__(self, *cells):
        self._cells = set(cells)

    def next_generation(self):
        return Grid(
            *set(filter(lambda cell: self.live_neighbours(cell) in [2, 3],
                 self._cells)).union(self.newborns())
        )

    def crop(self, width: int, height: int):
        return Grid(
            *set(filter(lambda cell: cell[0] in range(0, width) and
                        cell[1] in range(0, height),
                        self._cells))
        )

    def live_neighbours(self, cell: Cell) -> int:
        return len(self._cells.intersection(neighbours(cell)))

    def newborns(self) -> Iterable[Cell]:
        return filter(
            lambda c: c not in self._cells and self.live_neighbours(c) == 3,
            reduce(lambda cells, c: set(cells).union(neighbours(c)),
                   self._cells, set())
        )

    def __eq__(self, other) -> bool:
        return self._cells == other._cells


def neighbours(cell: Cell) -> Iterable[Cell]:
    x, y = cell
    adjacent = [(x_, y_) for x_ in range(x - 1, x + 2)
                for y_ in range(y - 1, y + 2)]
    return filter(lambda c: c != cell, adjacent)
