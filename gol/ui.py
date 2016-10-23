import curses
from typing import Tuple


def show(board) -> None:
    screen = curses.initscr()
    screen.addstr(0, 0, str(board))
    screen.refresh()


def size() -> Tuple[int, int]:
    screen = curses.initscr()
    y, x = screen.getmaxyx()
    return int(x / 2), y
