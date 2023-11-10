import pygame

from cell import Cell

WHITE = (255, 255, 255)

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((25 * 25, 25 * 25))

    running = True

    cells = []

    cell_width = 25
    cell_height = 25

    for y in range(25):
        for x in range(25):
            cells.append(Cell(x * (1 + cell_width), y * (1 + cell_height), cell_width, cell_height))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.get_surface().fill(WHITE)

        for cell in cells:
            cell.draw()

        pygame.display.flip()

    pygame.quit()
