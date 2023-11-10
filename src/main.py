import pygame

from cell import Cell

WHITE = (255, 255, 255)

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_mode((25 * 26, 25 * 26))

    running = True
    fpsClock = pygame.time.Clock()

    cells = []

    cell_width = 25
    cell_height = 25

    for y in range(25):
        row = []
        for x in range(25):
            row.append(Cell(x * (1 + cell_width), y * (1 + cell_height), cell_width, cell_height))

        cells.append(row)

    for y in range(25):
        for x in range(25):
            cell = cells[y][x]

            neighbor_left = x - 1 >= 0
            neighbor_right = x + 1 < 25
            neighbor_top = y - 1 >= 0
            neighbor_bottom = y + 1 < 25

            if neighbor_left:
                cell.track(x - 1, y, cells[y][x - 1])

            if neighbor_right:
                cell.track(x + 1, y, cells[y][x + 1])

            if neighbor_top:
                cell.track(x, y - 1, cells[y - 1][x])

            if neighbor_bottom:
                cell.track(x, y + 1, cells[y + 1][x])

            if neighbor_left and neighbor_top:
                cell.track(x - 1, y - 1, cells[y - 1][x - 1])

            if neighbor_right and neighbor_top:
                cell.track(x + 1, y - 1, cells[y - 1][x + 1])

            if neighbor_left and neighbor_bottom:
                cell.track(x - 1, y + 1, cells[y + 1][x - 1])

            if neighbor_right and neighbor_bottom:
                cell.track(x + 1, y + 1, cells[y + 1][x + 1])

    for y in range(5, 10 + 1):
        for x in range(5, 10 + 1):
            cells[y][x].live()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.get_surface().fill(WHITE)

        for row in cells:
            for cell in row:
                cell.update()

        for row in cells:
            for cell in row:
                cell.draw()

        pygame.display.flip()
        fpsClock.tick(2)

    pygame.quit()
