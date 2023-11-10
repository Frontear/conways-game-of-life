import pygame
from drawable import Drawable

class Cell(Drawable):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)

        self.image = pygame.Surface((width, height))
        self.image.fill((255, 255, 255)) # clear out surface
        pygame.draw.lines(self.image, (0, 0, 0), True, [(0, 0), (width - 1, 0), (width - 1, height - 1), (0, height - 1)]) # lines from corner to corner of cell, appears like a border
