import time

import click

from . import ui
from gol import Grid


def make_beacon():
    return Grid((4, 4), (4, 5), (5, 5), (5, 4),
                (6, 6), (6, 7), (7, 7), (7, 6))


def make_tetramino():
    return Grid((10, 10), (11, 10), (12, 10), (11, 9))


def make_pentomino():
    return Grid((20, 20), (21, 20), (20, 21), (19, 21), (20, 22))


@click.command()
@click.option('--fullscreen', '-f', 'fullscreen', default=False, type=bool,
              help='Run in fullscreen.', is_flag=True)
def main(fullscreen: bool) -> None:
    gui = ui.Pygame(fullscreen=fullscreen)
    gui.handle_input()

    grid = make_pentomino().crop(*gui.size())
    gui.show(grid)

    while gui.keep_running:
        time.sleep(0.75)
        grid = grid.next_generation().crop(*gui.size())
        gui.show(grid)


if __name__ == '__main__':
    main()
