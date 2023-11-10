import pygame

from abc import abstractmethod, ABC

class Drawable(ABC):
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    # TODO: make self.image requirement clear
    def draw(self):
        pygame.display.get_surface().blit(self.image, (self.x, self.y))
