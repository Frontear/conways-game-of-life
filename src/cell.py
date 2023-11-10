import pygame
from drawable import Drawable

class Cell(Drawable):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        
        self.neighbors = []

        image = pygame.Surface((width, height))
        image.fill((255, 255, 255)) # clear out surface

        self.die_image = image.copy()
        self.live_image = image.copy()

        pygame.draw.lines(self.die_image, (0, 0, 0), True, [(0, 0), (width - 1, 0), (width - 1, height - 1), (0, height - 1)]) # lines from corner to corner of cell, appears like a border
        self.live_image.fill((0, 0, 0))
        
        self.__alive = False
        self.image = self.die_image

        self.__mark_live = False
        self.__mark_die = False

    def isAlive(self):
        return self.__alive

    def update(self):
        if self.__mark_live:
            self.__mark_live = False
            self.__alive = True

        if self.__mark_die:
            self.__mark_die = False
            self.__alive = False

        if self.__alive and self.image != self.live_image:
            self.image = self.live_image

        if not self.__alive and self.image != self.die_image:
            self.image = self.die_image
    
    # TODO: separate into tick() method
    # Rules of Conway:
    # - live with < 2 living neighbors => die
    # - live with 2-3 living neighbors => lives
    # - live with > 3 living neighbors => die
    # - dead with = 3 living neighbors => lives
    def draw(self):
        ret = super().draw()

        living_neighbors = 0
        for neighbor in self.neighbors:
            coord, cell = neighbor

            if cell.isAlive():
                living_neighbors += 1

        if self.__alive:
            if living_neighbors < 2:
                self.die()
            elif living_neighbors <= 3:
                pass # lives on
            else:
                self.die()
        else:
            if living_neighbors == 3:
                self.live()

        return ret

    def die(self):
        self.__mark_die = True

    def live(self):
        self.__mark_live = True

    # neighbors list of tuples with a coordinate object + cell object
    def track(self, x, y, cell):
        self.neighbors.append(((x, y), cell))
