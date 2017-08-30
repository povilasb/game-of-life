from typing import Tuple
from threading import Thread
import time

import pygame


class Pygame:
    def __init__(self, fullscreen: bool=False) -> None:
        self.cell_size = 20
        self.keep_running = True

        pygame.init()
        pygame.mixer.quit()

        flags = pygame.FULLSCREEN if fullscreen else 0
        self.screen = pygame.display.set_mode((0, 0), flags)

        self._input_thread = Thread(target=self._on_input)

    def __del__(self) -> None:
        pygame.quit()
        self._input_thread.join()

    def size(self) -> Tuple[int, int]:
        return (int(self.screen.get_width() / self.cell_size),
                int(self.screen.get_height() / self.cell_size))

    def show(self, grid) -> None:
        self.clear()
        for x, y in grid._cells:
            self.rect(x, y)
        pygame.display.flip()

    def rect(self, x: int, y: int) -> None:
        pygame.draw.rect(
            self.screen, 0xFFFFFF,
            [x * self.cell_size, y * self.cell_size, self.cell_size - 2,
                self.cell_size - 2],
            0,
        )

    def clear(self) -> None:
        self.screen.fill((0, 0, 0))

    def handle_input(self) -> None:
        """Starts new thread that listens for keyboard input."""
        self._input_thread.start()

    def _on_input(self) -> None:
        while self.keep_running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == 27:
                        self.keep_running = False
            time.sleep(0.25)
