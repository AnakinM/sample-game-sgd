"""
This task is not in the attacjed task list file `tasks.md`.
This was assigned as part of an online lecture.
The task is to draw a star using the pygame library by modifying
the original `drawing.py` file provided in the `examples` directory.
"""

import sys
import pygame
from pygame.locals import QUIT

DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)


def draw_star():
    star_points = [
        (200, 20),  # top
        (220, 110),
        (310, 110),
        (235, 165),
        (255, 260),  # bottom right
        (200, 200),
        (145, 260),  # bottom left
        (165, 165),
        (90, 110),
        (180, 110),
    ]
    pygame.draw.polygon(DISPLAYSURF, GREEN, star_points)


def main():
    pygame.init()

    # set up the window
    DISPLAYSURF.fill(WHITE)
    pygame.display.set_caption("Drawing")

    draw_star()

    # run the game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


if __name__ == "__main__":
    main()
