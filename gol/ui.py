from typing import Tuple

import pygame
from pygame.locals import *


class Pygame:
    def __init__(self) -> None:
        self.cell_size = 20

        pygame.init()
        self.screen = pygame.display.set_mode() # pygame.FULLSCREEN)

    def size(self) -> Tuple[int, int]:
        return (int(self.screen.get_width() / self.cell_size),
                int(self.screen.get_height() / self.cell_size))

    def show(self, matrix) -> None:
        self.clear()

        width, height = self.size()
        # TODO: use pyfunctional
        for y in range(height):
            for x in range(width):
                if matrix[y][x]:
                    self.rect(x, y)

        pygame.display.flip()

    def rect(self, x: int, y: int) -> None:
        pygame.draw.rect(self.screen, 0xFFFFFF,
            [x * self.cell_size, y * self.cell_size, self.cell_size - 2,
            self.cell_size - 2], 0)

    def clear(self) -> None:
        self.screen.fill((0, 0, 0))
